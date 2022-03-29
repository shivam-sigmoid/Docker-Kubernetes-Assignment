# Docker-Kubernetes Assignment by Shivam Raj

### Docker task

- Write a simple airflow dag to connect with db(postgres) and add entry in db for each execution (Time of dag execution)
- Add the given dag into the container and install dependencies.
- Use docker compose to launch airflow and postgres
- Schedule the dag
- Validate entry in postgres

###  Steps
- Run the docker compose command
- Go to localhost:8080
- Trigger the dag

### Kubernetes Task

- Create deployment and service for above airflow and postgres (you can use postgres helm chart for postgres deployment)
- Deploy airflow and postgres
- Schedule the dag
- Validate entry in postgres

### Steps
- Start minikube by ```minikube start``` cmd
- Mount the dags folder ```minikube mount ./dags/:/mnt/airflow/dags```
- Apply all the file by ```./script-apply.sh```
- Get all details by ```kubectl get pods,deploy,svc,pv,pvc```
- To access webserver ```minikube service airflow-webserver```
- Port forward by ```kubectl port-forward svc/<servicename> 8080:8080```