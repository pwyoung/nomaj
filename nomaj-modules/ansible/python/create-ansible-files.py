#!/usr/bin/env python3

# Goal:
#   Create Ansible files using data in 'config.yaml'

import os
import sys
import argparse
import io
from jinja2 import Environment, FileSystemLoader
import yaml
from git.repo.base import Repo
from pathlib import Path
import stat


class AnsibleFileCreator:
    def __init__(self, cfg):
        self.template_path = cfg.template_path
        self.config_file = cfg.config_file
        self.ansible_dir = cfg.ansible_dir
        self.inventory_file = os.path.normpath(os.path.join(cfg.ansible_dir, "inventory.yaml"))
        self.requirements_file = os.path.normpath(os.path.join(cfg.ansible_dir, "requirements.yaml"))
        self.playbook_dir = os.path.normpath(os.path.join(cfg.ansible_dir, "playbooks"))
        self.run_playbooks_script = os.path.normpath(os.path.join(cfg.ansible_dir, "run-playbooks.sh"))
        self.roles_dir = os.path.normpath(os.path.join(cfg.ansible_dir, "roles"))
        self.extra_vars_file = os.path.normpath(os.path.join(cfg.ansible_dir, "extra_vars.yaml"))

    def readConfigData(self):
        """ Read the config file and
            populate self.config_data
        """
        config_file_data = {}
        with open(self.config_file, 'r') as stream:
            try:
                self.config_data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def createInventoryFile(self):
        """ Create The inventory file
        """

        data = self.config_data['ansible']['inventory']

        with open(self.inventory_file, 'w') as out_file:
            yaml.dump(data, out_file, default_flow_style=False)

        # TODO: Finish adding support for dynamic IPs
        replacements = []
        replacements.append({"old": "192", "new": "192"})
        if len(replacements) > 0:
            with open(self.inventory_file, 'r') as in_file:
                data = in_file.read()
            for d in replacements:
                data = data.replace(d["old"], d["new"])
            with open(self.inventory_file, 'w') as out_file:
                out_file.write(data)

    def createRequirementsFile(self):
        """ Create The requirements file
        """
        file_loader = FileSystemLoader(self.template_path)
        env = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)
        template = env.get_template('requirements.yaml.j2')
        self.requirements_output = template.render(
            roles=self.config_data['ansible']['roles']
        )
        with open(self.requirements_file, 'w') as out_file:
            out_file.write(self.requirements_output)

    def createPlaybookFiles(self):
        """ Fetch the playbooks as defined in config.yaml
            Also, create a script to execute the playbooks (in the order listed in config.yaml)
        """
        data = self.config_data['ansible']['playbooks']
        for item in data:
            src = item['src']
            name = item['name']
            version = item['version']
            dest = os.path.normpath(os.path.join(self.playbook_dir, name))
            if not os.path.exists(dest):
                print("Cloning " + src + " to " + dest)
                Repo.clone_from(src, dest)
            repo = Repo(dest)
            if len(version) == 0:
                version = 'master'
            repo.git.fetch  # Get all commits (don't "pull" in case there are conflicting local edits)
            repo.git.checkout(version)  # Switch to our branch
            repo.git.reset('--hard')  # Remove any local edits
            repo.git.pull()  # Pull in the latest commits for this branch (merge is insufficient here)

    def createRunPlaybooksScript(self):
        """ Create a script to runt the playbooks
            Maintain the order in the config file
        """
        file_loader = FileSystemLoader(self.template_path)
        env = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)
        template = env.get_template('run-playbooks.sh.j2')
        self.run_playbooks_script_output = template.render(
            playbooks=self.config_data['ansible']['playbooks'],
            playbook_dir=self.playbook_dir,
            inventory_file=self.inventory_file,
            extra_vars_file=self.extra_vars_file,
            ansible_dir=self.ansible_dir
        )
        with open(self.run_playbooks_script, 'w') as out_file:
            out_file.write(self.run_playbooks_script_output)
        f = Path(self.run_playbooks_script)
        f.chmod(f.stat().st_mode | stat.S_IEXEC)

    def createExtraVarsFile(self):
        """ Create the extra_vars.yml file
        """
        data = self.config_data['ansible']['extra_vars']
        with open(self.extra_vars_file, 'w') as out_file:
            yaml.dump(data, out_file, default_flow_style=False)


def read_cli_args(argv):
    """ Read the CLI args and return sane settings
    """

    # For readability, the variables are declared here and initialized to their default values
    # Set paths so that this works even if no parameters are given
    script_dir = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.normpath(os.path.join(script_dir, "templates"))
    config_file = os.path.normpath(os.path.join(script_dir, "..", "..", "..", "build", "config.yaml"))
    ansible_dir = os.path.normpath(os.path.join(script_dir, "..", "..", "..", "build", "ansible"))

    # Parse the args
    parser = argparse.ArgumentParser(description='Create Inventory file.')
    parser.add_argument('-t', '--template-path',
                        action='store', type=str, dest="template_path",
                        help='Path to templates dir. Detault:' + template_path,
                        default=template_path)
    parser.add_argument('-c', '--config-file',
                        action='store', type=str, dest="config_file",
                        help='Path to Config file to read. Default:' + config_file,
                        default=config_file)
    parser.add_argument('-a', '--ansible-dir',
                        action='store', type=str, dest="ansible_dir",
                        help='Path to Inventory file to create. Default:' + ansible_dir,
                        default=ansible_dir)
    args = parser.parse_args()
    return args


def main(argv):
    """ This is called when this is run from the CLI
    """
    app_cfg = read_cli_args(argv)

    app = AnsibleFileCreator(app_cfg)
    app.readConfigData()
    app.createInventoryFile()
    app.createRequirementsFile()
    app.createPlaybookFiles()
    app.createRunPlaybooksScript()
    app.createExtraVarsFile()


if __name__ == "__main__":
    main(sys.argv[1:])
