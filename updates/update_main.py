import argparse
from src.trigger_workflow_dispatch import trigger_workflow

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--job_name")
    args = parser.parse_args()
    
    trigger_workflow(
        account_name = "hannahker", 
        repo_name = "databricks-trigger", 
        action_name = "databricks_update.yml", 
        action_inputs = {"job_name": args.job_name}
    )
