from electrycityconsumption.constants.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from electrycityconsumption.utils.common import read_yaml, create_directories
from electrycityconsumption.entity.config_entity import DataIngestionConfig

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