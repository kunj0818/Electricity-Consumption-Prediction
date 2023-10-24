from electrycityconsumption.config_1.cofiguration import ConfigurationManager
from electrycityconsumption.components.prepare_base_model import PrepareBaseModel
from electrycityconsumption.electricity_consumption_prediction import logger_1

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(prepare_base_model_config)
        prepare_base_model.create_lstm_model()

if __name__ == '__main__':
    try:
        logger_1.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger_1.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger_1.exception(e)
        raise e