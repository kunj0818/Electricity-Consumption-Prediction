from electrycityconsumption.config_1.configuration import ConfigurationManager
from electrycityconsumption.components.model_evaluation import Evaluation
from electrycityconsumption.electricity_consumption_prediction import logger_1



STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()




if __name__ == '__main__':
    try:
        logger_1.info(f"*******************")
        logger_1.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger_1.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger_1.exception(e)
        raise e
            