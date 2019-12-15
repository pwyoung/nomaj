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

# TESTING
This has been tested on:
- Fedora31
- PopOS 19.10

# REQUIREMENTS
- Python
  - python3
  - pip3
  - modules:
    - see ./requirements.txt
- Nomaj Ansible Module
  - Ansible (2.8.3)
- Nomaj Vagrant Module
  - vagrant (2.2.3)
  - On Linux
    - If using (default) Libvirt Virtualization
      - Libvirt (5.4.0)
      - vagrant-libvirt (0.0.45-2) [ on Linux ]
      - Working QEMU/Session (see below)
- Testing
  - Some tests require passwordless-ssh to localhost
    e.g. 'ssh localhost whoami' should work

# SETUP EXAMPLES
- PopOS-19.10:
  - Requirements were satisfied with:
    - Python, Ansible, Vagrant, QEMU/KVM/Libvirt/BridgeUtils, and Virt-Manager
      - sudo apt-get install python3-venv vagrant-libvirt ansible qemu qemu-kvm bridge-utils virt-manager
    - QEMU/Session (for Libvirt/KVM as non-root)
      - sudo mkdir -p /etc/qemu
      - echo 'allow virbr0' | sudo tee /etc/qemu/bridge.conf
      - sudo chmod u+s /usr/lib/qemu/qemu-bridge-helper
      - sudo ln -s /etc/apparmor.d/usr.sbin.libvirtd /etc/apparmor.d/disable/usr.sbin.libvirtd && reboot
        - Details/Rationale for the above...
          - Address a Known Bug...
            - Bug:
              - https://bugs.launchpad.net/ubuntu/+source/libvirt/+bug/1754871
                - Clearly, Ubuntu folks are not addressing Libvirt/KVM/QEMU as it is part of RHEL,
                  but podman, CGroups-v2, and so on are part of the future of Linux, IMO.
              - Symptom/Error when running vagrant-libvirt with qemu/session:
                - "internal error: /usr/lib/qemu/qemu-bridge-helper"
                - "failed to write fd to unix socket: Socket operation on non-socket"
            - Workaround:
              - Option A: disable AppArmor for libvirtd
                - https://askubuntu.com/questions/741035/disabling-apparmor-for-kvm
                  - sudo ln -s /etc/apparmor.d/usr.sbin.libvirtd /etc/apparmor.d/disable/usr.sbin.libvirtd
                  - reboot
              - Option B: (not done)
                - https://www.redhat.com/archives/libvir-list/2018-April/msg00534.html
    - Nomaj Python Modules and tests
      - cd ./<nomaj_dir> && make
  - Convenience/Optional:
    - Python 'venv' was configured
  - "Install" nomaj in $PATH
    - sudo ln -s ...<path-to>/nomaj/nomaj /usr/local/bin/

# Testing
To install the Python modules required and run the tests:
- cd ./<nomaj_dir> && make
