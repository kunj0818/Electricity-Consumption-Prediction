from electrycityconsumption.constants.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from electrycityconsumption.utils.common import read_yaml, create_directories
from electrycityconsumption.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig
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