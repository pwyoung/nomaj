
# GOAL
This demonstrates a complex project run via 'nomaj'.

# Details
At a high level, this will:
- Create a number of VMs using Vagrant
- Configure the VMs with Ansible

Specifically it will:
- Create a Vagrantfile (./build/Vagrantfile) and execute it to produce the VMs
- Update ~/.ssh/config to allow 'ssh <node-name>' to work
- Create a set of Ansible files (./build/ansible/*) to install Kubespray
- A Bash script will be created to run the local Ansible job
- The local Ansible job will:
  - Install Kubespray on the first node in the inventory
  - Leverage the config file's 'extra_vars' yaml block.
    - This will become a file used by the Kubespray Ansible job.

# Assumptions
This assumes:
- 'nomaj' is in PATH
- nomaj is run while the current working directory contains config.yaml
