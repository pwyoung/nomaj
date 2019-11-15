#!/usr/bin/env python3

# Goal:
#   Create a Makefile (for our purposes) from a given yaml config file

import os
import sys
import argparse
import io
from jinja2 import Environment, FileSystemLoader
import yaml

debug = True


class MakefileCreator:
    def __init__(self, cfg):
        self.make_file = cfg.make_file
        self.template_path = cfg.template_path
        self.config_file = cfg.config_file
        if debug:
            print("config_file = " + self.config_file)
            print("teplate_path = " + self.template_path)
            print("make_file = " + self.make_file)

    def createMakeFile(self):
        """ Create the Makefile using the config file and template
        """
        # Read the config file
        with open(self.config_file, 'r') as stream:
            try:
                cfg = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        # This should always be non-null
        project_namespace = cfg['generic']['project_namespace']
        print("Makefile has project namespace: " + project_namespace)

        # Path to this script
        script_dir = os.path.dirname(os.path.realpath(__file__))
        nomaj_app = os.path.normpath(os.path.join(script_dir,
                                                  "..",
                                                  "..",
                                                  "..",
                                                  "nomaj"))

        # Populate self.make_output from the template
        file_loader = FileSystemLoader(self.template_path)
        env = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)
        template = env.get_template('Makefile.j2')
        make = cfg
        output_data = template.render(
            project_namespace=project_namespace,
            cfg=cfg,
            nomaj_app=nomaj_app
        )

        # Write the make output data to the Makefile
        with open(self.make_file, 'w') as out_file:
            out_file.write(output_data)


def read_cli_args(argv):
    """ Read the CLI args and return sane settings
    """

    # For readability, the variables are declared here and initialized to their default values
    # Set paths so that this works even if no parameters are given
    script_dir = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.normpath(os.path.join(script_dir, "templates"))
    config_file = os.path.normpath(os.path.join(script_dir,
                                                "..",
                                                "..",
                                                "tests",
                                                "module-make",
                                                "build",
                                                "config.yaml"))
    make_file = os.path.normpath(os.path.join(script_dir,
                                              "..",
                                              "..",
                                              "tests",
                                              "module-make",
                                              "build",
                                              "Makefile"))
    # Parse the args
    parser = argparse.ArgumentParser(description='Create Makefile from template and config file.')
    parser.add_argument('-m', '--make-file',
                        action='store', type=str, dest="make_file",
                        help='Path to Makefile to create. Default:' + make_file,
                        default=make_file)
    parser.add_argument('-c', '--config-file',
                        action='store', type=str, dest="config_file",
                        help='Path to Config file to read. Default:' + config_file,
                        default=config_file)
    parser.add_argument('-t', '--template-path',
                        action='store', type=str, dest="template_path",
                        help='Path to templates dir. Detault:' + template_path,
                        default=template_path)
    args = parser.parse_args()
    return args


def main(argv):
    """ This is called when this is run from the CLI
    """
    app_cfg = read_cli_args(argv)

    app = MakefileCreator(app_cfg)
    app.createMakeFile()


if __name__ == "__main__":
    main(sys.argv[1:])
