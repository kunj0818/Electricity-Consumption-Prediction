from electrycityconsumption.config_1.cofiguration import ConfigurationManager
from electrycityconsumption.components.model_training import Training
from electrycityconsumption.electricity_consumption_prediction import logger_1



STAGE_NAME = "Training"



class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train()



if __name__ == '__main__':
    try:
        logger_1.info(f"*******************")
        logger_1.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger_1.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger_1.exception(e)
        raise e
        




