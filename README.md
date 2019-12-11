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

