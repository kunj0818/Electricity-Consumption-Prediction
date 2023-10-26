import tensorflow as tf
from pathlib import Path
from sklearn.model_selection import train_test_split
from electrycityconsumption.entity.config_entity import TrainingConfig
import pandas as pd

class Training:
    def __init__(self, config : TrainingConfig):
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.base_model_path
        )

    def save_model(self, path: Path, model: tf.keras.Model):
        model.save(path)

    def load_training_data(self,training_data_path):
        try:
            # Load your training data from the provided CSV file
            data = pd.read_csv(training_data_path)

            # Assuming your data has columns for features and a target variable 'Usage_kWh'
            # Replace with the actual column names from your data
            X = data.drop(columns=['Usage_kWh'])  # Exclude the target variable
            y = data['Usage_kWh']  # Target variable

          

            return X,y
        except Exception as e:
            print(f"Error loading training data: {str(e)}")
            return None, None

    
    
    
    def train(self):
        self.get_base_model()
        #Load your training data
        X, y = self.load_training_data(self.config.training_data)
        #print(y)
        # Split your data into training and validation sets
        X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)
        X_train = tf.convert_to_tensor(X_train, dtype=tf.float32)
        X_valid = tf.convert_to_tensor(X_valid, dtype=tf.float32)
        y_train = tf.convert_to_tensor(y_train, dtype=tf.float32)
        y_valid = tf.convert_to_tensor(y_valid, dtype=tf.float32)
        X_train = tf.reshape(X_train, [-1, 32, 14])
        y_train = tf.reshape(y_train, [-1, 32, 1])
        X_valid = tf.reshape(X_valid, [-1, 32, 14])
        y_valid = tf.reshape(y_valid, [-1, 32, 1])
        # Train your model
        self.model.fit(X_train, y_train, epochs=self.config.params_epochs, validation_data=(X_valid, y_valid))

        # Save your trained model
        self.save_model(self.config.trained_model_path, self.model)