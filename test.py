import mlflow
print("printing tracking URI scheme below")
print(mlflow.get_tracking_uri())
print("\n")
mlflow.set_tracking_uri("https://127.0.0.1:5000")
print("printing new tracking URI schemes below")
print(mlflow.get_tracking_uri())
print("\n")