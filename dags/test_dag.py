from airflow.models import DagBag

def test_dag_loaded():
    dag_bag = DagBag()

    dag = dag_bag.get_dag(dag_id="run_pipeline")

    assert dag is not None
    assert dag.dag_id == "run_pipeline"


def test_dag_tasks():
    dag_bag = DagBag()
    dag = dag_bag.get_dag("run_pipeline")

    task_ids = [task.task_id for task in dag.tasks]

    assert "run_raw_to_trusted" in task_ids