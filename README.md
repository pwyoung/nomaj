# DESCRIPTION
There's no magic here. 

# GOAL
The goal of this project is to allow a user to manage an entire project with:
- a single config file
- a single override file (e.g. to force local environment settings)
- a simple, flexible, intuitive way to process the config file

# DOCS
-  See ./docs/algorithm.md for details of how the program works
-  See ./test/vagrant-and-ansible/Makefile for example usage

# EXAMPLES
- Pattern
  - This is currently being used to develop and test all code I'm doing.
  - For each component, I have a config file (at the top level or in a subdir of
    the project) and I simply issue a single command to create all dependencies I
    need for development.
- K8S App Dev:
  - This will:
    - Create VMs on Vagrant and KVM/QEMU
    - Provision a multi-node K8S cluster on the VMs
    - Configure the cluster
    - Add various dependencies needed





