# DESCRIPTION
There's no magic here.

# GOAL
The goal of this project is to allow a user to manage an entire project with:
- a single config file
- a single override file (e.g. to force local environment settings)
- a simple, flexible, intuitive way to process the config file

# DOCS
- See ./docs/algorithm.md for details of how the program works
- See ./tests/* for example usage
  - Test Details:
    - ./tests/example-nomaj-in-path:
      - The Makefile here should be useful as-is for using nomaj to run vagrant and then ansible
        in other projects.
    - ./tests/example-vagrant-and-ansible
      - This is similar to ./tests/example-nomaj-in-path but calls the vagrant and ansible modules
        directly without using the 'make' module.
    - ./tests/example-k8s-via-kubespray
      - This shows a complex example which will:
        - Create a set of Vagrant boxes, each with multiple virtual NVME disk drives.
	- Set up SSH to each box (by editing ~/.ssh/config)
	- Install Kubespray (the Kubernetes installer) on the first master node
	- Run ansible, using the variables in the configuration file to control the run

# TODO
- Additional built-in modules:
  - Terraform
  - DockerCompose
