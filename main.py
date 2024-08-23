from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

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
 