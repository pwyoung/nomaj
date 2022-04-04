#!/bin/bash


setup_qemu() {
    # Setup QEMU t o support user-sessions
    if cat /etc/qemu/bridge.conf | grep 'virbr0'; then
        echo "It looks like you set up KVM/QEMU user session support already."
    else
        echo "Allow non-root user to use the QEMU/Session resources"
        sudo mkdir -p /etc/qemu
        echo 'allow virbr0' | sudo tee /etc/qemu/bridge.conf
        sudo chmod u+s /usr/lib/qemu/qemu-bridge-helper
        cat <<EOF
- TODO:
  - Add user (i.e. non-rot) Connection
    - libvirt GUI -> File -> Add Connection -> Hypervisor -> KVM/QEMU user session
    - Test this easily using something like gnome-boxes to make a new VM
EOF
        sleep 9
    fi


    # Deal with OS updates changing perms on the helper
    if ls -l /usr/lib/qemu/qemu-bridge-helper | egrep '^-rwsr'; then
      echo "OK, qemu-bridge-helper permissions seem fine."
    else
      sudo chmod u+s /usr/lib/qemu/qemu-bridge-helper
    fi
}

setup_qemu
