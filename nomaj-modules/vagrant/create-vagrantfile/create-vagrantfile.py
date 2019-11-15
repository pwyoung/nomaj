#!/usr/bin/env python3

# Goal:
#   Create a Vagrantfile (for our purposes) from a given yaml config file
# Motivation:
#   - The resulting file can contain only what is needed
#   - The resulting file is easy to review manually
#   - The resulting file is easy to to test
#     - we can compare the resulting file to an expected file
#   - Vagrantfiles (especially with Closures) are a bit tricky to deal with.
#   - Jinja2 templating is used since Ansible uses it and most other code will be Ansible.

import os
import sys
import argparse
import io
from jinja2 import Environment, FileSystemLoader
import yaml

debug = True

class VagrantfileCreator:
  def __init__(self, cfg):
      self.vagrant_file = cfg.vagrant_file
      self.template_path = cfg.template_path
      self.config_file = cfg.config_file
      if debug:
          print("config_file = " + self.config_file)
          print("teplate_path = " + self.template_path)
          print("vagrant_file = " + self.vagrant_file)

  def createVagrantFile(self):
      """ Create the Vagrantfile using the config file and template
      """
      # Read the config file
      with open(self.config_file, 'r') as stream:
          try:
             cfg = yaml.safe_load(stream)
          except yaml.YAMLError as exc:
              print(exc)

      # This should always be non-null
      project_namespace = cfg['generic']['project_namespace']
      print("Vagrantfile has project namespace: " + project_namespace)

      # Populate self.vagrant_output from the template
      file_loader = FileSystemLoader(self.template_path)
      env = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)
      template = env.get_template('Vagrantfile.j2')
      vagrant = cfg['vagrant']
      output_data = template.render(
        project_namespace = project_namespace,
        vagrant = vagrant
      )

      # Write the vagrant output data to the Vagrantfile
      with open(self.vagrant_file, 'w') as out_file:
         out_file.write(output_data)

def read_cli_args(argv):
    """ Read the CLI args and return sane settings
    """

    # For readability, the variables are declared here and initialized to their default values
    # Set paths so that this works even if no parameters are given
    script_dir = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.normpath(os.path.join(script_dir, "templates"))
    config_file = os.path.normpath(os.path.join(script_dir, "..", "test", "build", "config.yaml"))
    vagrant_file = os.path.normpath(os.path.join(script_dir, "..", "test", "build", "Vagrantfile"))

    # Parse the args
    parser = argparse.ArgumentParser(description='Create Vagrantfile from template and config file.')
    parser.add_argument('-v', '--vagrant-file',
                        action='store', type=str, dest="vagrant_file",
                        help='Path to Vagrantfile to create. Default:' + vagrant_file,
                        default=vagrant_file)
    parser.add_argument('-c', '--config-file',
                        action='store', type=str, dest="config_file",
                        help='Path to Config file to read. Default:' + config_file,
                        default=config_file)
    parser.add_argument('-t', '--template-path',
                        action='store', type=str, dest="template_path",
                        help='Path to templates dir. Detault:' + template_path,
                        default=template_path)
    args=parser.parse_args()
    return args

def main(argv):
    app_cfg = read_cli_args(argv)

    app = VagrantfileCreator(app_cfg)
    app.createVagrantFile()

if __name__ == "__main__":
   main(sys.argv[1:])
