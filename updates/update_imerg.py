from src.trigger_workflow_dispatch import trigger_workflow

if __name__ == "__main__":
    action_name = "run_monitoring.yml"
    repo_name = "imerg-monitoring-repo"
    account_name = "hannahker"
    trigger_workflow(account_name, repo_name, action_name)
