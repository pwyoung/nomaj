
# GOAL
This demonstrates running 'nomaj -m vagrant'.
The vagrant module creates a Vagrantfile from the config yaml and then
executes 'vagrant up' against it.

# Details

- By default the Vagrantfile includes support for libvirt and virtualbox.
- To simplify the resulting Vagrantfile, one can set the 'enabled: False'
in the section of the provider to omit.
- The Vagrantfile includes support for nvme disks.

# Libvirt-specific details

The libvirt provider is set to use QEMU/Session.
This allow the module to create and use qemu disk image files as the current user.
With QEMU/System, that's more complicated.

