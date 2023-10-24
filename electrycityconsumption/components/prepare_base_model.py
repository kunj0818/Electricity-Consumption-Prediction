import tensorflow as tf
from pathlib import Path
from electrycityconsumption.entity.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config
    
    def create_lstm_model(self):
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.LSTM(50, input_shape=tuple(self.config.input_shape), return_sequences=True))
        model.add(tf.keras.layers.LSTM(50, return_sequences=True))
        model.add(tf.keras.layers.Dense(1))
        model.compile(optimizer='adam', loss='mean_squared_error')
        self.save_model(path=self.config.base_model_path, model=model)
    def save_model(self, path: Path, model: tf.keras.Model):
        model.save(path)

