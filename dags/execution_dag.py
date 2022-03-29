from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
# from utils import fetch_and_store_execution_dag_run

import psycopg2


def fetch_and_store_execution_dag_run():
    try:
        conn = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow", port='5432')
        cursor = conn.cursor()
        drop_table = """drop table IF EXISTS execution_table"""
        cursor.execute(drop_table)
        conn.commit()
        create_query = """create table execution_table as select dag_id, execution_date from dag_run order by execution_date;"""
        cursor.execute(create_query)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2022, 3, 21),
    "retries": 0,
}

with DAG("execution", default_args=default_args, schedule_interval="0 6 * * *", catchup=False) as dag:
    t1 = DummyOperator(task_id="check_dag")

    t2 = PythonOperator(task_id="fetch_execution_data_and_store", python_callable=fetch_and_store_execution_dag_run)

    t1 >> t2
