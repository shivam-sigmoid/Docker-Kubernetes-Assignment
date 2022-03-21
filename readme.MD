# Docker-Kubernetes Assignment by Shivam Raj

### Docker task

- Write a simple airflow dag to connect with db(postgres) and add entry in db for each execution (Time of dag execution)
- Add the given dag into the container and install dependencies.
- Use docker compose to launch airflow and postgres
- Schedule the dag
- Validate entry in postgres

### Kubernetes Task

- Create deployment and service for above airflow and postgres (you can use postgres helm chart for postgres deployment)
- Deploy airflow and postgres
- Schedule the dag
- Validate entry in postgres


### Set up
```
# Create a kubernetes cluster of 1 control plane and 3 worker nodes
kind create cluster --name airflow-cluster --config kind-cluster.yaml

# Check the cluster info
kubectl cluster-info

# Check the nodes with kubectl
kubectl get nodes -o wide

# Add the official repository of the Airflow Helm Chart
helm repo add apache-airflow https://airflow.apache.org

# Update the repo
helm repo update

# Create namespace airflow
kubectl create namespace airflow

# Check the namespace 
kubectl get namespaces

# Install the Airflow Helm Chart
helm install airflow apache-airflow/airflow --namespace airflow --debug

# Get pods
kubectl get pods -n airflow

# Check release
helm ls -n airflow

# If for some reasons the release is stuck in pending-install or timed out
# Resinstall the chart
helm delete airflow --namespace airflow
helm install airflow apache-airflow/airflow --namespace airflow --debug —timeout 10m0s

# Port forward 8080:8080
kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow --context kind-airflow-cluster
```