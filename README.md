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

# HIGH-LEVEL REQUIREMENTS
- Python
- Ansible
- Vagrant
- Something to run VMs

# DETAILED REQUIREMENTS
- "Nomaj Ansible Module" requires:
  - Ansible (2.8.3+)
  - Python version 3 with pip3
  - /usr/bin/python should exist
  - Password-less SSH to localhost (e.g. "ssh localhost whoami") should work
- "Nomaj Vagrant Module" requires:
  - vagrant (2.2.3+)
  - On Linux
    - Libvirt (5.4.0+) with working QEMU/Session
- Local execution of VMs requires a Virtual Machine Manager:
  - Supported for Linux:
    - KVM/QEMU
    - VirtualBox
  - Supported for Mac/OS:
    - VirtualBox
  - Supported for Windows:
    - HyperV
    - VirtualBox

# Examples of how to meet requirements
- On PopOS/Ubuntu, just fetch and run this script:
    - https://github.com/pwyoung/computer-setup/blob/master/home/bin/setup-popos-computer.sh

# Installation
Put something like the following in your login script
```
NOMAJ_HOME=/home/$USER/git/nomaj
if [ -e $NOMAJ_HOME ]; then
    export PATH=$PATH:$NOMAJ_HOME;
fi
```
Run setup and tests via
```
cd $NOMAJ_HOME && make
``` 

# Running nomaj
There are documents on nomaj [here](../docs/) 

# A simple example of running nomaj
Nomaj is designed to be run normally with no arguments so that it can assume a few things, such as that the config file is in the current directory.

You can see examples of this by calling the unit tests manually by going into their directories and just running "nomaj". 

An example of doing this would be:

```
# Go to where we installed nomaj
cd /home/$USER/git/nomaj
# Go to the unit test
cd ./tests/unit-tests/module-vagrant
# Run nomaj
nomaj
```

Nomaj intentionally exposes what it does so that you can directly use the underlying tools it manages. An example of that would be to follow up the above run with
```
# Ensure we are in the same directory as before
cd /home/$USER/git/nomaj/tests/unit-tests/module-vagrant
# Go into the directory for the component nomaj set up for us
cd ./build/vagrant
vagrant status
```

