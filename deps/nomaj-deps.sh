#!/bin/bash

# GOAL:
#   Install deps for nomaj
#
# Requirements
# - This was tested on Ubuntu-22.04

set -e

PKGS="emacs-nox tree glances htop dmidecode"
PKGS+=" gnome-boxes virt-manager"
PKGS+=" python3-pip vagrant "
PKGS+=" python-is-python3 python3-venv"
#PKGS+=" xdg-utils"
#PKGS+=" xfsprogs"
# For local certs, esp on K8S
# https://github.com/cloudflare/cfssl
#PKGS+=" golang-cfssl"

install_packages() {
    sudo apt update
    sudo apt install -y $PKGS
}

# Support this user running "user sessions" with KVM/Qemu
# See: https://mike42.me/blog/2019-08-how-to-use-the-qemu-bridge-helper-on-debian-10
# See: https://www.linuxtechi.com/how-to-install-kvm-on-ubuntu-22-04/
configure_qemu_helper() {
    # This didn't exist
    sudo mkdir -p /etc/qemu
    sudo chown root /etc/qemu
    sudo chmod 0755 /etc/qemu

    echo 'allow virbr0' | sudo tee /etc/qemu/bridge.conf
    sudo chown root.$USER /etc/qemu/bridge.conf
    sudo chmod 0664 /etc/qemu/bridge.conf
    #
    sudo chmod u+s /usr/lib/qemu/qemu-bridge-helper
    #
    sudo chgrp $USER /etc/qemu/bridge.conf

    if ! sudo systemctl status libvirtd.service | grep 'active (running)'; then
        cat <<EOF
        # Setup libvirt daemon
        systemctl enable libvirtd.service
        systemctl start libvirtd.service
EOF
        exit 1
    fi

    if ! ip addr show virbr0 | grep '192.168.122.1'; then
        cat <<EOF
        # Create "virbr0" as the default bridge for Libvirt/KVM/Qemu
        sudo virsh net-autostart --network default
        sudo virsh net-start --network default
EOF
        exit 1
    fi


    # instead of "-c qemu:///session"
    export LIBVIRT_DEFAULT_URI="qemu:///session"
    virsh list --all

    # ls -l /var/run/libvirt/libvirt-sock
    # srwxrwx--- 1 root libvirt 0 Dec  7 20:40 /var/run/libvirt/libvirt-sock
    #
    # sudo usermod -G libvirt-qemu -a $USER
    # sudo usermod -G libvirt -a $USER
    # sudo usermod -G kvm -a $USER
    # reboot

    #
    # Setup libvirtd to run as non-root
    #   https://computingforgeeks.com/use-virt-manager-as-non-root-user/
    #
    # sudo emacs /etc/libvirt/libvirtd.conf
    # unix_sock_group = "libvirt"
    # unix_sock_rw_perms = "0770"
    #
    # sudo systemctl restart libvirtd.service
    # systemctl status libvirtd.service

    # e ~/.profile.d/kvm.sh


}

setup_ansible() {
    if ! ansible-galaxy --version; then
        sudo apt install software-properties-common -y
        sudo apt-add-repository ppa:ansible/ansible
        sudo apt update -y
        sudo apt install ansible -y
        ansible --version
        ansible-galaxy --version
    fi
}

setup_ssh() {
    # SSH
    if [ ! -e ~/.ssh/id_ed25519 ]; then
        echo "Make ed25519 SSH key"
        ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519
    fi

    # SSH
    sudo apt-get install -y openssh-server
    sudo systemctl enable ssh --now

    # Passwordless-SSH should work
    ssh localhost hostname

    # SSH-config
    SSHCFG=$HOME/.ssh/config
    test -f $SSHCFG || echo "creating $SSHCFG" && touch $SSHCFG
}



main() {
    install_packages
    configure_qemu_helper
    setup_ansible
    setup_ssh
}

main
