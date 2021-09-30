#! /usr/bin/env bash

eksctl create cluster --name=igti-cluster --managed --spot --instance-types=m5.xlarge \
    --nodes=2 --alb-ingress-access --node-private-networking --region=us-east-1 \
    --nodes-min=2 --nodes-max=3 --full-ecr-access --asg-access --nodegroup-name=ng-igticluster

#ariflowenem
eksctl create cluster --name=igti-cluster-1 --managed --spot --instance-types=m5.xlarge \
    --nodes=5 --alb-ingress-access --node-private-networking --region=us-east-1a \
    --nodes-min=3 --nodes-max=6 --full-ecr-access --asg-access --nodegroup-name=ng-igticluster
#scalling
eksctl scale nodegroup --cluster igti-cluster-1 --name ng-igticluster  --nodes 5 --nodes-max 6 --nodes-min 3