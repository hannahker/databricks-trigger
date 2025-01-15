# Databricks / GitHub Actions Integration

This repo integrates the execution of Databricks Jobs with GitHub Actions pipelines. 

When any of the ERA5, IMERG, Floodscan, or SEAS5 Databricks update jobs run, subsequent GitHub Actions can be triggered using the intermediate `databricks_update.yml` action in this repo. 

## Usage

To trigger a follow up GitHub Action in a separate repository: 

1. Select the appropriate script in `updates/` for the dataset that you care about. Eg. to listen for `IMERG` updates, you'll need to open up the `updates/imerg.py` script. 

2. Add a new `trigger_workflow()` function call in the script For example: 

```
trigger_workflow(
    account_name = "hannahker", 
    repo_name = "imerg-monitoring-repo",
    action_name = "run_monitoring.yml"
)
```

will trigger this monitoring script to run: https://github.com/hannahker/imerg-monitoring-repo/blob/main/.github/workflows/run_monitoring.yml. 