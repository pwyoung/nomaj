# Example of how to add a box
# Vagrant-Libvirt seems to not fetch them automatically (but vagrant-virtualbox does)
BOX='generic/ubuntu1804'
PROVIDER='libvirt'
vagrant box add $BOX --provider=$PROVIDER

