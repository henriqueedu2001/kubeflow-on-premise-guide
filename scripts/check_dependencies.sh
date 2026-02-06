#!/bin/bash

RED='\e[0;31m'
GREEN='\e[0;32m'
NC='\e[0m'

dependencies=(
    nvidia-smi
    docker
    kind
    kubectl
    kustomize
    helm
    go
)

success_count=0
fail_count=0

echo CHECKING KUBEFLOW DEPENDENCIES

check_dep() {
    cmd=$1
    index=$2
    if command -v "$cmd" >/dev/null 2>&1; then
        success_count=$((success_count + 1))
        echo -e "${GREEN}\t[$index] $cmd: installed.${NC}"
    else
        echo -e "${RED}\t[$index] $cmd: not installed.${NC}"
        fail_count=$((fail_count + 1))
    fi
}

index=1
for dependency in ${dependencies[@]}; do
    check_dep $dependency $index
    index=$((index + 1))
done

total=$((success_count + fail_count))

echo -e "${GREEN}$success_count/$total successfully installed dependencies.${NC}"
echo -e "${RED}$fail_count dependencies not installed.${NC}"