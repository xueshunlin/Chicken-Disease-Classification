from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logger

STAGE_NAME = "evaluation"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info(f"Running stage: {STAGE_NAME}")
        pipeline = EvaluationPipeline()
        pipeline.main()
        logger.info(f"Stage: {STAGE_NAME} completed successfully")
    except Exception as e:
        logger.error(f"Failed to run stage: {STAGE_NAME}")
        logger.error(e)
        raise e