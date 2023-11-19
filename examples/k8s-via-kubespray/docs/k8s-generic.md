# Admission Controllers
kubectl get --raw /apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations | jq

# Mutating web-hooks
kubectl get --raw /apis/admissionregistration.k8s.io/v1/mutatingwebhookconfigurations | jq
