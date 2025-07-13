import os
import numpy as np
import pandas as pd
import joblib
from src.utils.logger import logger
from src.utils.exception import CustomException
from src.components.data_transformation import DataTransformation


# class PredictionPipeline:
#     """
#     Loads model and transformer, predicts cluster for new customer data.
#     """

#     def __init__(self):
#         self.model_path = os.path.join("artifacts", "model.pkl")

#         self.transformer_path = os.path.join("artifacts", "transformer.pkl")

#     def predict(self, input_data: pd.DataFrame):
#         try:
#             logger.info("Loading model and transformer for prediction")

#             model = joblib.load(self.model_path)

#             transformer = joblib.load(self.transformer_path)
#             logger.info("Transforming input data")
#             # transformer = DataTransformation()
#             transformed_data = transformer.transform(input_data)


#             logger.info("Making Predictions")
#             preds = model.predict(transformed_data)

#             return preds
        
#         except Exception as e:
#             logger.error(f"Prediction failed: {str(e)}")
#             raise CustomException("prediction Failed ", e)
        


# src/pipelines/prediction_pipeline.py
import joblib

class PredictionPipeline:
    def __init__(self):
        self.transformer = joblib.load("artifacts/transformer.pkl")
        self.model = joblib.load("artifacts/model.pkl")

    def predict(self, input_df):
        transformed = self.transformer.transform(input_df)
        return self.model.predict(transformed)
