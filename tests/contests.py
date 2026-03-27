import pytest
from airflow.models import DagBag

@pytest.fixture
def dag_bag():
    return DagBag()


@pytest.fixture
def dag(dag_bag):
    return dag_bag.get_dag("run_pipeline")