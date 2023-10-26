from electrycityconsumption.constants.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from electrycityconsumption.utils.common import read_yaml, create_directories, save_json
from electrycityconsumption.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig,TrainingConfig,EvaluationConfig
from pathlib import Path


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self):
        data_ingestion_config = DataIngestionConfig(
            root_dir=self.config.data_ingestion.root_dir,
            local_data_path=self.config.data_ingestion.local_data_path
        )

        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])
        

        prepare_base_model_config = PrepareBaseModelConfig(
        root_dir=Path(config.root_dir),
        base_model_path=Path(config.base_model_path),
        params_learning_rate=float(self.params.LEARNING_RATE),
        input_shape=self.params.input_shape
        )

        return prepare_base_model_config
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training_model
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = Path(self.config.data_ingestion.local_data_path)
       

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            base_model_path=Path(prepare_base_model.base_model_path),
            training_data= training_data,
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_loss_function=params.LOSS_FUNCTION,
            params_optimizer=params.OPTIMIZER

        )

        return training_config
    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model="artifacts/training/model.h5",
            training_data="artifacts/data_ingestion/cleaned_data1.csv",
            mlflow_uri="https://dagshub.com/kunj0818/Electricity-Consumption-Prediction.mlflow",
            all_params=self.params
        )
        return eval_config
