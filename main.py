from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainignPipeline

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