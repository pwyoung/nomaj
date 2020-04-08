This module has one script:
- run

# Script: run
This will:
  - Read the config file
  - Generate a set of Terraform files:
    - The files generally follow the layout described here: https://www.terraform.io/docs/cloud/workspaces/repo-structure.html
    - This will also create 'run-terraform.sh' which will run the terraform job (plan and then apply).
  - Execute run-terraform.sh
