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

