#!/bin/bash

# Assume the default works. Or use this
# export KUBECONFIG=~/.kube/config.local


# TODO
#   IMG='nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda10.2'
#   ngc registry image pull $IMG

NS='nvidia-test'

create_namespace() {
    TMP=~/.tmp-k8s-nvidia-pod-test.file

    cat <<EOF > $TMP
apiVersion: v1
kind: Namespace
metadata:
  name: $NS
EOF

    kubectl apply -f $TMP

    kubectl get ns

}

# Test K8S basic functionality
test_generic_kubectl_run_pod() {
    POD='test'
    IMG='hello-world'
    kubectl -n $NS run --restart=Never --image=$IMG -it $POD
    kubectl -n $NS logs $POD
    kubectl -n $NS delete $POD
}

# kubectl -n $NS run --rm -it --restart=Never --image=nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda10.2 cuda-samples-test
test_kubectl_apply_of_cuda_operation() {
    IMG='nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda10.2'
    POD='gpu-test'
    CN='gpu-test-container'

    # Make sure the pod doesn't exist
    kubectl -n $NS delete pod $POD &>/dev/null

    TMP=~/.tmp-k8s-nvidia-pod-test.file

    cat <<EOF > $TMP
apiVersion: v1
kind: Pod
metadata:
  name: $POD
spec:
  restartPolicy: OnFailure
  containers:
  - name: $CN
    image: $IMG
    resources:
      limits:
         nvidia.com/gpu: 1
EOF

    kubectl -n $NS apply -f $TMP
    sleep 2

    kubectl -n $NS logs $POD | tee $TMP
    if ! grep 'Test Passed' $TMP; then
        echo "The test succeeded!"
        kubectl -n $NS delete pod $POD
    else
        echo "The test failed!"
        exit 1
    fi

}

test_images_via_kubectl_run() {
    # Basic pod test cleanup
    #kubectl -n $NS delete pod gpu-test

    # Test Nvidia containers
    # https://catalog.ngc.nvidia.com/orgs/nvidia/containers/cuda
    # https://gitlab.com/nvidia/container-images/cuda/blob/master/doc/supported-tags.md
    # WORKS
    #
    # RHEL8
    # kubectl -n $NS run --rm gpu-test --restart=Never --image=nvcr.io/nvidia/cuda:11.1.1-devel-ubi8 -it -- nvidia-smi
    # kubectl -n $NS run --rm gpu-test --restart=Never --image=nvcr.io/nvidia/cuda:11.1.1-devel-ubi8 -it -- bash
    #
    # UBUNTU
    #
    # CUDA
    # kubectl -n $NS run --rm gpu-test --restart=Never --image=nvcr.io/nvidia/cuda:12.2.2-devel-ubuntu22.04 -it -- nvidia-smi
    # kubectl -n $NS run --rm -it --restart=Never --image=nvcr.io/nvidia/cuda:12.3.0-devel-ubuntu22.04 gpu-test -- nvidia-smi
    #
    # CUDA-SAMPLES
    # https://catalog.ngc.nvidia.com/orgs/nvidia/teams/k8s/containers/cuda-sample
    #kubectl -n $NS run --rm -it --restart=Never --image=nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda10.2 gpu-test #-- nvidia-smi
    kubectl -n $NS run --rm -it --restart=Never --image=nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda10.2 gpu-test -- nvidia-smi


    #POD='gpu-test'; kubectl -n $NS logs $POD; kubectl -n $NS delete pod $POD
}

create_namespace
#test_generic_kubectl_run_pod
#test_kubectl_apply_of_cuda_operation
test_images_via_kubectl_run
