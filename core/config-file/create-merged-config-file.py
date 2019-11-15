#!/usr/bin/env python3

# PURPOSE:
#   - Produce the merged config file.
#     The result of applying the overrides to the given config file
#     will be written to the build directory.
#   - Assign the project namespace.
#     The namespace will be taken from the config file if it exists,
#     otherwise it will be derived from git.
#     The calculated project namespace will be inserted into the 
#     merged config file.

import os
import sys
import argparse
import yaml
from pathlib import Path

debug = False


class MergeFileCreator:
    def __init__(self, cfg):
        self.config_file = cfg.config_file
        self.override_file = cfg.override_file
        self.merged_file = cfg.merged_file

    def createMergedConfigFile(self):
        """ Read the config file and override file and
          create the merged file
        """
        # Read config data
        if os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as stream:
                try:
                    cfg = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
            if debug:
                print("Using Config file: " + self.config_file)
        else:
            if debug:
                print("Config file does not exist: " + self.config_file)
            exit(1)

        # If project namespace was not in the config file, set a default
        if (cfg is not None
                and 'generic' in cfg
                and 'project_namespace' in cfg['generic']
                and cfg['generic']['project_namespace'] is not None
                and len(cfg['generic']['project_namespace']) > 0):
            if debug:
                print("Using specified namespace")
        else:
            conf_dir = os.path.dirname(self.config_file)
            cmd = "cd " + conf_dir + ' && basename `git rev-parse --show-toplevel`'
            try:
                result_bytes = subprocess.check_output(cmd,
                                                       timeout=300,
                                                       shell=True)
                project_namespace = result_bytes.decode('UTF-8').rstrip()
                if debug:
                    print("Derived namespace from git: " + project_namespace)
            except subprocess.CalledProcessError as e:
                if debug:
                    print("Error deriving project namespace from git: ", e.output)
                sys.exit(1)
            # Insert the project_namespace into the config data
            if cfg is None:
                cfg = {}
            if 'generic' not in cfg:
                cfg['generic'] = {}
            cfg['generic']['project_namespace'] = project_namespace

        # Confirm project namespace
        if debug:
            print("Project Namespace: " + cfg['generic']['project_namespace'])

        # Read overrides
        override_file_data = {}
        if os.path.isfile(self.override_file):
            with open(self.override_file, 'r') as stream:
                try:
                    override_file_data = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)

        # Created merged data
        self.config_data = cfg
        # print("Applying override_file_data: " + str(override_file_data))
        if override_file_data is not None:
            self.config_data = merge(self.config_data, override_file_data)

        # Ensure parent directory for merged file exists
        directory = Path(self.merged_file).parent
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Created merged file
        with open(self.merged_file, 'w') as out_file:
            yaml.dump(self.config_data, out_file)


def merge(a, b, path=None, update=True):
    """ Merge 'b' into 'a'
        https://stackoverflow.com/questions/7204805/dictionaries-of-dictionaries-merge
    """
    # print("\nMerging: a=" + str(a) + " b=" + str(b) + " path=" + str(path) )
    if path is None:
        path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass  # same leaf value
            elif isinstance(a[key], list) and isinstance(b[key], list):
                for idx, val in enumerate(b[key]):
                    a[key][idx] = merge(a[key][idx],
                                        b[key][idx],
                                        path + [str(key), str(idx)],
                                        update=update)
            elif update:
                a[key] = b[key]
            else:
                raise Exception('Conflict at %s' %
                                '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a


def read_cli_args(argv):
    """ Read the CLI args and return sane settings
    """

    # Working defaults
    cur_dir = os.getcwd()
    config_file = os.path.normpath(os.path.join(cur_dir, "config.yaml"))
    override_file = os.path.normpath(os.path.join(cur_dir, "overrides.yaml"))
    merged_file = os.path.normpath(os.path.join(cur_dir, "build", "config.yaml"))
    # Parse the args
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config-file',
                        action='store', type=str, dest="config_file",
                        help='Path to Config file to read. Default:'
                             + config_file,
                        default=config_file)
    parser.add_argument('-o', '--override-file',
                        action='store', type=str, dest="override_file",
                        help='Path to override file. Default:'
                             + override_file,
                        default=override_file)
    parser.add_argument('-m', '--merged-file',
                        action='store', type=str, dest="merged_file",
                        help='Path to output of this script. Default:'
                             + merged_file,
                        default=merged_file)
    args = parser.parse_args()
    return args


def main(argv):
    app_cfg = read_cli_args(argv)

    app = MergeFileCreator(app_cfg)
    app.createMergedConfigFile()


if __name__ == "__main__":
    main(sys.argv[1:])
