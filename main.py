from networksecurity.components.data_ingetion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import os
import sys


if __name__=='__main__':
    try:
        
        trainingPipelineConfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingPipelineConfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingPipelineConfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Intiate data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)
        data_transforamtion_config=DataTransformationConfig(trainingPipelineConfig)
        logging.info("data transformation started")
        data_transformation=DataTransformation(data_validation_artifact, data_transforamtion_config)
        data_transforamtion_artifact=data_transformation.initiate_data_transformation()
        print(data_transforamtion_artifact)
        logging.info("data transformation completed")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)