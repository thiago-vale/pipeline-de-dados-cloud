from unittest.mock import patch
from dags.test_dag import run_script

def test_run_script_calls_subprocess():
    with patch("dags.test_dag.subprocess.run") as mock_run:
        run_script("script.py")

        mock_run.assert_called_once_with(
            ["python3", "script.py"],
            check=True
        )