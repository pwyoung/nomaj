# Pod Security Admission
- [It's on by default in Kubernetes v1.23+.](https://neonmirrors.net/post/2022-06/examining-pod-security/)

# Admission Controllers
```
kubectl get --raw /apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations | jq
```

# Mutating web-hooks
```
kubectl get --raw /apis/admissionregistration.k8s.io/v1/mutatingwebhookconfigurations | jq
```

