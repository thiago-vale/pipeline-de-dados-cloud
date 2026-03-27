from unittest.mock import patch
import subprocess

def run_script(file):
    subprocess.run(["python3", file], check=True)

def test_run_script_calls_subprocess():
    with patch("dags.test_dag.subprocess.run") as mock_run:
        run_script("script.py")

        mock_run.assert_called_once_with(
            ["python3", "script.py"],
            check=True
        )