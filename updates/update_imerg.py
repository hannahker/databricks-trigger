from src.trigger_workflow_dispatch import trigger_workflow

if __name__ == "__main__":
    
    trigger_workflow(
        account_name = "hannahker", 
        repo_name = "imerg-monitoring-repo",
        action_name = "run_monitoring.yml"
    )
