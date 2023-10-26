import tensorflow as tf
from pathlib import Path
import mlflow
import pandas as pd
import mlflow.keras
from urllib.parse import urlparse
from sklearn.model_selection import train_test_split
from electrycityconsumption.utils.common import save_json 
from electrycityconsumption.entity.config_entity import EvaluationConfig

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def load_training_data(self,training_data_path):
        try:
            # Load your training data from the provided CSV file
            data = pd.read_csv(training_data_path)

            # Assuming your data has columns for features and a target variable 'Usage_kWh'
            # Replace with the actual column names from your data
            X = data.drop(columns=['Usage_kWh'])  # Exclude the target variable
            y = data['Usage_kWh']  # Target variable
            X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)
            X_train = tf.convert_to_tensor(X_train, dtype=tf.float32)
            X_valid = tf.convert_to_tensor(X_valid, dtype=tf.float32)
            y_train = tf.convert_to_tensor(y_train, dtype=tf.float32)
            y_valid = tf.convert_to_tensor(y_valid, dtype=tf.float32)
            X_train = tf.reshape(X_train, [-1, 32, 14])
            y_train = tf.reshape(y_train, [-1, 32, 1])
            X_valid = tf.reshape(X_valid, [-1, 32, 14])
            y_valid = tf.reshape(y_valid, [-1, 32, 1])
          

            return X_valid,y_valid
        except Exception as e:
            print(f"Error loading training data: {str(e)}")
            return None, None

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        X_valid, y_valid = self.load_training_data(self.config.training_data)
        self.score = self.model.evaluate(X_valid, y_valid)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score}
        save_json(path=Path("scores.json"), data=scores)

    
    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"loss": self.score}
            )
            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.keras.log_model(self.model, "model", registered_model_name="LSTMmodel")
            else:
                mlflow.keras.log_model(self.model, "model")
