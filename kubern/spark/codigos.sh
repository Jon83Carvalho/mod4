kubectl create secret generic aws-credentials --from-literal=aws_access_key_id=AKIA4FAFXNKDR5DEQKUX --from-literal=aws_secret_access_key=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 -n processing
kubectl apply -f spark/spark-operator.yaml -n processing