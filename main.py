from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f">>>>> Stage {STAGE_NAME} started...")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} completed successfully<<<<\n\nx=====x.")
except Exception as e:
        logger.error(f"An error occurred in {STAGE_NAME} stage: {str(e)}")
        raise e