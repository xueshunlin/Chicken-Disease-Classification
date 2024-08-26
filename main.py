from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainignPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:
    logger.error(f"Failed {STAGE_NAME}")
    logger.error(e)
    raise e
 
STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"Starting {STAGE_NAME}")
    pipeline = PrepareBaseModelTrainignPipeline()
    pipeline.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(e)
    raise e


STAGE_NAME = "Training"
try:
    logger.info(f"Starting {STAGE_NAME} stage")
    pipeline = ModelTrainingPipeline()
    pipeline.main()
    logger.info(f"Completed {STAGE_NAME} stage")
except Exception as e:
    logger.exception(e)
    raise e