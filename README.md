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

# REQUIREMENTS
- Python3 with pip3
- "Nomaj Ansible Module" requires:
  - Ansible (2.8.3+)
  - /usr/bin/python should exist
  - The test for this module requires passwordless-ssh to localhost
    e.g. 'ssh localhost whoami' should work
- "Nomaj Vagrant Module" requires:
  - vagrant (2.2.3+)
  - On Linux
    - Libvirt (5.4.0+) with working QEMU/Session
  - ~/.ssh/config should exist

# Examples of how to meet requirements
- On PopOS/Ubuntu
  - sudo apt update && sudo apt install python3-pip ansible vagrant gnome-boxes
  - Allow non-root user to use the QEMU/Session resources
    - Note: VirtualBox works too if the security implications bother you.
    - echo 'allow virbr0' | sudo tee /etc/qemu/bridge.conf
    - sudo chmod u+s /usr/lib/qemu/qemu-bridge-helper

# Installation
- Put something like the following in your login script
```
NOMAJ_HOME=/home/$USER/git/nomaj
if [ -e $NOMAJ_HOME ]; then 
    export PATH=$PATH:$NOMAJ_HOME; 
fi