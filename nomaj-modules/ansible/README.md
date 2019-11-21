This module has one script:
- run

# Script: run
This will:
  - Read the config file
  - Generate a set of Ansible files:
    - The files generally follow the layout described here: https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html#directory-layout#
    - This will also create 'run-playbooks.sh' which will run the playbooks from the config file in the order specified
      in the config file.
  - Execute run-playbooks.sh
