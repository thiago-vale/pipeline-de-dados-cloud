from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import os

caminho1 = "/home/thiago-vale/Documentos/GitHub/pipeline-de-dados-cloud/shared_dir/pipeline/raw_to_trusted.py"
#caminho2 = "/home/thiago-vale/Documentos/GitHub/pipeline-de-dados-cloud/shared_dir/pipeline/trusted_to_refined"
# Função que será chamada pelo PythonOperator

def run_script(file):
    script_path = file
    os.system(f"python3 {script_path}")

# Definir os argumentos da DAG
default_args = {
    'owner': 'airflow',
    'start_date': '',
    'retries': 1,
    'retry_delay':'@once',
}

# Criar a DAG
dag = DAG(
    'run_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
)

# Criar o operador PythonOperator
raw_to_trusted_task = PythonOperator(
    task_id='run_raw_to_trusted',
    python_callable=run_script,
    op_args=caminho1,
    dag=dag,
)

# Definir a ordem dos operadores
raw_to_trusted_task
