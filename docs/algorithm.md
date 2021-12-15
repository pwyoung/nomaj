# Algorithm for the code

'nomaj'
  Manages the run.
  It is based on a few key parameters and some conventions.
 ```
  INPUTS:
    - CONFIG_FILE:
        user-specified input file
        The default is $(pwd)/config.yaml
    - OVERRIDE_FILE:
        user-specified overrides of CONFIG_FILE
        The default is $(pwd)/overrides.yaml
    - BUILD_DIR:
        user-specified output directory for the project
        defaults to $(pwd)/build
    - MODULE
        Module to execute
        The default is 'make'
    - MODULE_SCRIPT
        Specifies the script in the module to run
        The default is 'run'
  OUTPUTS:
    - MERGED_CONFIG_FILE
        Result of merging CONFIG_FILE and OVERRIDE_FILE
        Stored in BUILD_DIR/config.yaml
```

The module nomaj runs defaults to 'make' but it can be specified.
Modules are processed as follows.
Given an execution "nomaj -m MODULE", nomaj will do the following
```
- Find the local ./config.yaml
- Look for an optional ./overrides.yaml
- Create ./build/config.yaml with the merged result of the two files
- Look for a handler for MODULE.
  The search path is:
  - custom-local: $(pwd)/nomaj-modules/<module>
  - custom-global: ~/.nomaj/nomaj-modules/<module>
  - built-in: <Path to the nomaj script>/nomaj-modules/<module>
- Execute the module
  - Create the module dir, BUILD_DIR/<module>
  - Set the working dir to the module dir
  - Run the script for the module
```
See the tests for example usage.
