# Random notes


# Nginx-Proxy details

## Nginx-Proxy runs on all the worker nodes
kubectl get all --all-namespaces | grep nginx
kube-system   pod/nginx-proxy-k-3                            1/1     Running            0                 16h
kube-system   pod/nginx-proxy-k-4                            1/1     Running            0                 16h
kube-system   pod/nginx-proxy-k-5                            1/1     Running            0                 16h

## Nginx-Proxy runs as a static pod
cat ./config.yaml  | grep -i static
staticPodPath: /etc/kubernetes/manifests

ls /etc/kubernetes/manifests
nginx-proxy.yml

cat /etc/kubernetes/manifests/nginx-proxy.yml
sudo cat /etc/kubernetes/manifests/nginx-proxy.yml

