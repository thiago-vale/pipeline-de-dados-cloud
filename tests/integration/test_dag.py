from airflow.models import DagBag


def test_dag_loaded():
    dag_bag = DagBag(dag_folder="dags/", include_examples=False)

    assert len(dag_bag.import_errors) == 0, f"Erros: {dag_bag.import_errors}"

    dag = dag_bag.get_dag(dag_id="primeira_dag")

    assert dag is not None
    assert dag.dag_id == "primeira_dag"


def test_dag_tasks():
    dag_bag = DagBag(dag_folder="dags/", include_examples=False)

    dag = dag_bag.get_dag("primeira_dag")

    assert dag is not None  # 👈 importante

    task_ids = [task.task_id for task in dag.tasks]

    assert "run_raw_to_trusted" in task_ids