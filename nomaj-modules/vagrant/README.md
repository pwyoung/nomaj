# Vagrant module
This module has two scripts:
- run
- clean

# Script: run
This will:
  - Read the config file
  - Generate a vagrant file
  - Start the VMs via (e.g. via 'vagrant up')
  - Update ~/.ssh/config to enable SSH to the boxes
    via their vagrant box name.

# Script: clean
This will:
  - Destroy the Vagrant boxes (e.g. via 'vagrant destroy')
