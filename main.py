from electrycityconsumption.electricity_consumption_prediction import logger_1
from electrycityconsumption.pipeline.stage_one_data_ingestion import DataIngestionTrainingPipeline
from electrycityconsumption.pipeline.stage_two_prepare_base_model import PrepareBaseModelTrainingPipeline
STAGE_NAME = "Data Ingestion Stage"


try:
    logger_1.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger_1.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger_1.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"

try:
    logger_1.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger_1.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger_1.exception(e)
    raise e
