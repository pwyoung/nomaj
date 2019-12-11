# DESCRIPTION
There's no magic here.

# GOAL
The goal of this project is to allow a user to manage an entire project with:
- a single config file
- a single override file (e.g. to force local environment settings)
- a simple, flexible, intuitive way to process the config file

# DOCS
- See ./docs/algorithm.md for details of how the program works
- See ./tests/examples/ for example usage:
  - ./tests/examples/example-basic/README.md
  - ./tests/examples/example-k8s-via-kubespray/README.md

# TODO
- Additional Tests
  - Demonstrate how to add a local user-defined module
    - Just create a dir in ~/.nomaj/...
    - Run the code
- Additional built-in modules:
  - Terraform
  - DockerCompose
- Test (and tweak to run)
  - on Mac
  - on Windows

# TESTING
This has been tested on:
- Fedora31
- PopOS 19.10

# REQUIREMENTS
- Python
  - python3
  - pip3
  - modules:
    - see ./requirements.txt
- Vagrant Module
  - vagrant (2.2.3)
  - vagrant-libvirt (0.0.45-2) [ on Linux ]
- Ansible Module (2.8.3)
- Testing
  - Some tests require passwordless-ssh to localhost
    e.g. 'ssh localhost whoami' should work

# SETUP EXAMPLES
- PopOS-19.10:
  - Requirements were satisfied with:
    - sudo apt-get install python3-venv vagrant-libvirt ansible
    - cd ./<nomaj_dir> && make deps
  - Convenience/Optional:
    - virt-manager was installed
    - Python 'venv' was configured

# Compiling and Testing
To install the Python modules required and run the tests:
- cd ./<nomaj_dir> && make