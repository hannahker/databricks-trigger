import argparse
from src.trigger_workflow_dispatch import trigger_workflow

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--job_name")
    args = parser.parse_args()

    inputs = {"job_name": args.job_name}
    action_name = "databricks_update.yml"
    repo_name = "databricks_trigger"
    account_name = "hannahker"

    trigger_workflow(account_name, repo_name, action_name, inputs)
