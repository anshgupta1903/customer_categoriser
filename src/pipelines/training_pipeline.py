# from src.components.data_ingestion import DataIngestion
# from src.components.data_transformation import DataTransformation
# from src.components.model_trainer import ModelTrainer
# from src.components.model_evaluation import ModelEvaluation

# from src.utils.logger import logger

# if __name__ == "__main__":
#     try:
#         logger.info("🚀 Starting training pipeline")

#         # Ingest data 
#         df = DataIngestion().ingest_data()
#         logger.info(f"✅ Data shape: {df.shape}")

#         # Transform data 
#         transformer = DataTransformation()
#         X_train, X_test, y_train, y_test = transformer.transform(df)
#         logger.info(f"✅ Data transformed. Train shape: {X_train.shape}, Test shape: {X_test.shape}")

#         # Train model
#         trainer = ModelTrainer()
#         model = trainer.train(X_train, y_train)
#         logger.info("✅ Model trained and saved.")

#         # Evaluate
#         evaluator = ModelEvaluation()
#         results = evaluator.evaluate(model, X_test, y_test)

#         logger.info("🎉 Training pipeline completed successfully")
#         logger.info(f"Accuracy: {results['accuracy']:.4f}")
#         logger.info(f"Classification Report:\n{results['report']}")

#         print("🚀 Training pipeline completed successfully")
#         print(f"Accuracy: {results['accuracy']:.4f}")
#         print(f"Classification Report:\n{results['report']}")

#     except Exception as e:
#         logger.error(f"❌ Pipeline failed: {str(e)}")
#         print(f"Pipeline failed: {str(e)}")


# src/pipelines/training_pipeline.py
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

def train():
    print("🚀 Starting training pipeline...")

    # 1. Load data
    df = pd.read_csv('data.csv')  # replace with your actual file or ingestion code

    # 2. Separate features & target
    target_column = 'cluster'
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # 3. Build transformer
    numeric_features = X.columns.tolist()
    transformer = ColumnTransformer([
        ('num', Pipeline([('scaler', StandardScaler())]), numeric_features)
    ])

    # 4. Fit transformer & save
    transformer.fit(X)
    os.makedirs("artifacts", exist_ok=True)
    joblib.dump(transformer, "artifacts/transformer.pkl")
    print("✅ Transformer fitted & saved.")

    # 5. Transform data
    X_transformed = transformer.transform(X)

    # 6. Split
    X_train, X_test, y_train, y_test = train_test_split(
        X_transformed, y, test_size=0.2, random_state=42
    )

    # 7. Train model
    model = XGBClassifier()
    model.fit(X_train, y_train)

    # 8. Save model
    joblib.dump(model, "artifacts/model.pkl")
    print("✅ Model trained & saved.")

if __name__ == "__main__":
    train()
