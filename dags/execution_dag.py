from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
from utils import fetch_and_store_execution_dag_run


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2022, 3, 21),
    "retries": 0,
}


with DAG("execution", default_args=default_args, schedule_interval="0 6 * * *", catchup = False) as dag:

    t1 = DummyOperator(task_id = "check_dag")

    t2 = PythonOperator(task_id = "fetch_execution_data_and_store", python_callable = fetch_and_store_execution_dag_run)
    
    t1 >> t2
