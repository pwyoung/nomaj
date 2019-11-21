# Vagrant module
This module has two scripts:
- run
- clean

# Script: run
This will:
  - Read the config file
  - Generate a Make file
  - Execute 'make'

The Makefile has the following targets:
- all:
  - This will run the supported modules if their respective configuration sections 
  are present in the config file.
- clean:
  - This will clean the supported modules if their respective configuration sections 
  are present in the config file. 

See the template (Makefile.j2) for details.

# Script: clean
This will:
  - Execute 'make clean'
  