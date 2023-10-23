from electrycityconsumption.electricity_consumption_prediction import logger_1
from electrycityconsumption.pipeline.stage_one_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"


try:
    logger_1.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger_1.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger_1.exception(e)
    raise e

