
# GOAL
This demonstrates a complex project run via 'nomaj'.

# Details
At a high level, this will:
- Create a number of VMs using Vagrant
- Configure the VMs with Ansible

Specifically it will:
- Create a Vagrantfile (./build/Vagrantfile) and execute it to produce the VMs
- Update ~/.ssh/config to allow 'ssh <node-name>' to work
- Create a set of Ansible files (./build/ansible/*) to install Kubespray
- A Bash script will be created to run the local Ansible job
- The local Ansible job will:
  - Install Kubespray on the first node in the inventory
  - Leverage the config file's 'extra_vars' yaml block.
    - This will become a file used by the Kubespray Ansible job.

# Assumptions
This assumes:
- 'nomaj' is in PATH
- nomaj is run while the current working directory contains config.yaml

# K8S cheatsheet
https://kubernetes.io/docs/reference/kubectl/cheatsheet/

# Notes

After this runs, you can log into the deployment node with:
ssh k-1
sudo su -

Then run some commands (as root):
cat ~/.kube/config
kubectl config view
kubectl get pods --all-namespaces -o wide
kubectl get services --sort-by=.metadata.name --all-namespaces
apt  install jq
kubectl get service --namespace kube-system kubernetes-dashboard -o yaml


# Copy the config from the cluster
mkdir -p ~/.kube && ssh k-1 "sudo su - -c 'cat /root/.kube/config' 2>/dev/null" > ~/.kube/config.2
# Use it
KUBECONFIG=$HOME/.kube/config.2 kubectl config view
KUBECONFIG=$HOME/.kube/config.2 kubectl get all --all-namespaces

TODO:
- Advanced Secret management (various providers/plugins)
- Advanced DNS setup (custom domains)
- Advanced Identity management (e.g. FreeIPA)
- Advanced Network Routing (span multiple clouds/clusters)
- Add Helm and/or its alternatives (https://github.com/SwissDataScienceCenter/renku/issues/671)


