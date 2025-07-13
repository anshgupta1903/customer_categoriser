import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
from src.utils.logger import logger
from src.utils.exception import CustomException

class DataTransformation:
    """
    Transforms data: scaling numeric features.
    """
    def __init__(self):
        self.transformer_path = os.path.join("artifacts", "transformer.pkl")

    def transform(self, df):
        try:
            logger.info("Starting data transformation")

            # target column
            target_column = 'cluster'

            # separate features & target
            X = df.drop(columns=[target_column])
            y = df[target_column]
            # numeric columns only (since your dataset now is numeric)
            numeric_features = X.columns.tolist()

            logger.info(f"Numeric features: {numeric_features}")

            numeric_pipeline = Pipeline([
                ('scaler', StandardScaler())
            ])

            preprocessor = ColumnTransformer([
                ('num', numeric_pipeline, numeric_features)
            ])

            # fit & transform
            X_transformed = preprocessor.fit_transform(X)

            # save transformer
            os.makedirs("artifacts", exist_ok=True)
            joblib.dump(preprocessor, self.transformer_path)
            logger.info(f"Saved transformer at {self.transformer_path}")

            # split
            X_train, X_test, y_train, y_test = train_test_split(
                X_transformed, y, test_size=0.2, random_state=42
            )

            return X_train, X_test, y_train, y_test

        except Exception as e:
            logger.error(f"Error in data transformation: {str(e)}")
            raise CustomException("Data transformation failed", e)
