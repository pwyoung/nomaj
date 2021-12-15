
# NOTES
- Hypervisors:
  - Native bare-metal hypervisors (e.g. KVM and HyperV) are generally:
    - significantly faster at starting VMs
    - more efficient (in terms of CPU and Memory) when running the VMs
- OS choices (when possible):
  - Docker (and containers in general) operate on a set of Linux-based technology,
    so Linux is preferred for Docker/Container work due to performance and visiblity advantages.
  - Mac has no true native bare metal hypervisor,
    so Linux or Windows is preferred for VM work for performance and visibility advantages.
  - VirtualBox is less efficient than Containers or Native VMs, but it does work on Mac, Linux, and Windows,
    so Virtualbox is supported with Nomaj.

