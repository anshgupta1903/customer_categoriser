import os
from xgboost import XGBClassifier
import joblib
from src.utils.logger import logger
from src.utils.exception import CustomException

class ModelTrainer:
    """
    Trains XGBClassifier and saves the model.
    """
    def __init__(self):
        self.model_path = os.path.join("artifacts", "model.pkl")

    def train(self, X_train, y_train):
        try:
            logger.info("Starting model training with XGBClassifier")

            model = XGBClassifier(
                n_estimators=100,
                learning_rate=0.1,
                max_depth=5,
                random_state=42
            )
            model.fit(X_train, y_train)

            os.makedirs("artifacts", exist_ok=True)
            joblib.dump(model, self.model_path)

            logger.info(f"Model saved at: {self.model_path}")
            return model

        except Exception as e:
            logger.error(f"Error during model training: {str(e)}")
            raise CustomException("Model training failed", e)
