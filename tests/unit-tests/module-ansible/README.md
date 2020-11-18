
# GOAL
This demonstrates running 'nomaj -m ansible'.
The ansible module creates a set of Ansible native files from
the config yaml, including a Bash script that can be called
to run the playbooks in the order specified in the config.


# REQUIREMENTS
This requires that ssh to localhost works, without a password.
For example, the following should work:
    ssh localhost echo 'hi'
    