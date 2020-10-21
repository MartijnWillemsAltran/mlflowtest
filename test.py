import mlflow
import os
#remote_server_uri = "http://localhost:5000" # set to your server URI
#mlflow.set_tracking_uri(remote_server_uri)
# Note: on Databricks, the experiment name passed to mlflow_set_experiment must be a
# valid path in the workspace
# mlflow.set_experiment("/mlflowtest")
with mlflow.start_run():
    mlflow.log_param("a", 1)
    mlflow.log_metric("b", 2)
    mlflow.set_tag("test", "testValue!")
    mlflow.set_tag("Tracking URI", mlflow.get_tracking_uri())
    mlflow.set_tag("Artifact URI", mlflow.get_artifact_uri())

    # Log an artifact (output file)
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")
    mlflow.log_artifacts("outputs")

    mlflow.log_artifact("outputs/test.txt")

    print(f"artifact_uri={mlflow.get_artifact_uri()}")