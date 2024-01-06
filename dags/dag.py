from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def execute_python_file(file_path):
    exec(open(file_path).read())

start_date = datetime.now()

with DAG(
    "execute_python_files",
    start_date=datetime(2023, 6, 4),
    schedule_interval=timedelta(minutes=5)
) as dag:

    task_source_to_raw = PythonOperator(
        task_id="execute_source_to_raw",
        python_callable=execute_python_file,
        op_kwargs={"file_path": "/root/shared_dir/pipeline/source_to_raw.py"},
        owner="thiago"
    )

    task_raw_to_trusted = PythonOperator(
        task_id="execute_raw_to_trusted",
        python_callable=execute_python_file,
        op_kwargs={"file_path": "/root/shared_dir/pipeline/raw_to_trusted.py"},
        owner="thiago"
    )

task_source_to_raw >> task_raw_to_trusted

