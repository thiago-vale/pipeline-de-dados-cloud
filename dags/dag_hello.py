from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def print_hello():
    print("Hello, World!")

# Definir os argumentos da DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
}

# Criar a DAG
dag = DAG(
    'hello_world',
    default_args=default_args,
    schedule_interval=timedelta(days=1)  # Executar diariamente
)

# Criar a tarefa PythonOperator
hello_task = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
    owner="thiago"
)

# Definir a ordem dos operadores
hello_task