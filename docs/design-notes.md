# General Notes

# Choices

- Support Vagrant for local boxes:
  - It's great for managing QEMU/KVM on Linux
  - It's great for managing Virtualbox on OSX

- Avoid dependence on Vagrant Plugins when possible.
  - Vagrant Plugins are vulnerable to bit-rot and Ruby lib conflicts.
  - I've already found that I can not install certain Vagrant Plugins
    simultaneously.
  - Example:
    On Fedora (currently) one can not INSTALL 'vagrant-vbguest'
    because it requires PRECISELY fog-core=2.1.2
    while vagrant requires fog-core~>1.43.0
  - But they're great...
    Yes they are, if you use only a small, controlled set of them on a per-project
    and per-platform basis (i.e. don't try to switch OSes or Providers and hope you
    don't get a conflict).
  - But there's a workaround:
    Sure, maybe, in a certain case. But this sort of hassle is never-ending.
    Liberal use of plugins increases the odds of a problem geometrically.
  - Always avoid them?
    No. The included util 'create-custom-virtualbox-boxes' does use 'vagrant-vbguest'
    to add VirtualBox GuestAdditions to boxes on OSX.

- Prefer Libvirt/QEMU/KVM for dev work
  - GuestAdditions (or any paravirtualization) maintenance is a time sink.
  - VirtualBox can only provision boxes serially.
  - VirtualBox only supports 1 NVME controller.

# Likely Questions

- What about extension?
  - To add another nomaj-module, just:
    - A) Add the module to this project in nomaj-modules
    - B) Create a global module in ~/.nomaj/nomaj-modules
    - C) Create a per-project module in your <dir-you-call-nomaj-from>/nomaj-modules/

# TODO

- Support Terraform for remote (cloud) boxes:
  - It's currently a popular way to provision boxes
    and just about any other cloud resource.

- Consider adding support for Windows
  - Resources
    - https://www.vagrantup.com/docs/other/wsl.html
  - Virtualbox would be an easy starting point
  - HyperV should be possible
    - https://www.vagrantup.com/docs/hyperv/
  - See how many dependencies would be required and the odds
    a corp/windows environment would allow installation of any dep.

- Consider Adding VMware support for parallel provisioning on Mac.

- Add support for Docker
  - Adding a section for docker-compose data would be easy.
