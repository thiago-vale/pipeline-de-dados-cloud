from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def say_hello():
    print("Olá Mundo!")

with DAG(
    "primeira_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval=timedelta(minutes=5)
) as dag:

    task_hello = PythonOperator(
        task_id="say_hello_task",
        python_callable=say_hello,
        owner="thiago"
    )

    task_ola = PythonOperator(
        task_id="say_ola_task",
        python_callable=say_hello,
        owner="thiago"
    )

    task_oi = PythonOperator(
        task_id="say_oi_task",
        python_callable=say_hello,
        owner="thiago"
    )

    task_hello >> [task_ola,task_oi]

