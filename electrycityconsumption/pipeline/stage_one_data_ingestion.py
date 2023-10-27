from electrycityconsumption.config_1.configuration import ConfigurationManager
from electrycityconsumption.components.data_ingestion import DataIngestion
from electrycityconsumption.electricity_consumption_prediction import logger_1

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.copy_local_data()

if __name__ == '__main__':
    try:
        logger_1.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger_1.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger_1.exception(e)
        raise e


