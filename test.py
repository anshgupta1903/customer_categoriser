from src.pipelines.prediction_pipeline import PredictionPipeline
import pandas as pd

if __name__ == "__main__":
    data = {
        "Age": [45],
        "Education": [2],
        "Marital Status": [1],
        "Parental Status": [1],
        "Children": [2],
        "Income": [60000],
        "Total_Spending": [1500],
        "Days_as_Customer": [2000],
        "Recency": [20],
        "Wines": [500],
        "Fruits": [50],
        "Meat": [300],
        "Fish": [40],
        "Sweets": [30],
        "Gold": [100],
        "Web": [5],
        "Catalog": [2],
        "Store": [10],
        "Discount Purchases": [1],
        "Total Promo": [2],
        "NumWebVisitsMonth": [4]
    }
    df = pd.DataFrame(data)

    pipeline = PredictionPipeline()
    preds = pipeline.predict(df)
    print(f"Predicted cluster: {preds}")
