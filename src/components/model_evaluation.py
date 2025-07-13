from sklearn.metrics import accuracy_score, classification_report
from src.utils.logger import logger
from src.utils.exception import CustomException

class ModelEvaluation:
    """
    Evaluates trained model on test set.
    """
    def __init__(self):
        pass

    def evaluate(self, model, X_test, y_test):
        try:
            logger.info("Starting model evaluation")

            y_pred = model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred)

            logger.info(f"Accuracy on test set: {acc:.4f}")
            logger.info(f"Classification Report:\n{report}")

            return {"accuracy": acc, "report": report}

        except Exception as e:
            logger.error(f"Error during model evaluation: {str(e)}")
            raise CustomException("Model evaluation failed", e)
