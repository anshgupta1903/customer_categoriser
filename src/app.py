# from fastapi import FastAPI
# from pydantic import BaseModel
# import pandas as pd
# import joblib
# from fastapi.middleware.cors import CORSMiddleware

# from pymongo import MongoClient
# from datetime import datetime
# from src.db import predictions_collection, logs_collection
# # Replace with your actual URI
# # client = MongoClient(
# #     "mongodb+srv://admin:secret123@cluster0.g5xhf.mongodb.net/customer_segmentation?retryWrites=true&w=majority"
# # )

# # # Database & collections
# # db = client["customer_segmentation"]
# # predictions_collection = db["predictions"]
# # logs_collection = db["logs"]
# # users_collection = db["users"]

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ✅ Load transformer & model once
# transformer = joblib.load("artifacts/transformer.pkl")
# model = joblib.load("artifacts/model.pkl")

# class InputData(BaseModel):
#     Age: int
#     Education: int
#     Marital_Status: int
#     Parental_Status: int
#     Children: int
#     Income: float
#     Total_Spending: float
#     Days_as_Customer: int
#     Recency: int
#     Wines: float
#     Fruits: float
#     Meat: float
#     Fish: float
#     Sweets: float
#     Gold: float
#     Web: int
#     Catalog: int
#     Store: int
#     Discount_Purchases: int
#     Total_Promo: int
#     NumWebVisitsMonth: int

# @app.post("/predict")
# def predict(data: InputData):
#     try:
#         data_dict = data.dict()
#         df = pd.DataFrame([{
#             'Age': data_dict['Age'],
#             'Education': data_dict['Education'],
#             'Marital Status': data_dict['Marital_Status'],
#             'Parental Status': data_dict['Parental_Status'],
#             'Children': data_dict['Children'],
#             'Income': data_dict['Income'],
#             'Total_Spending': data_dict['Total_Spending'],
#             'Days_as_Customer': data_dict['Days_as_Customer'],
#             'Recency': data_dict['Recency'],
#             'Wines': data_dict['Wines'],
#             'Fruits': data_dict['Fruits'],
#             'Meat': data_dict['Meat'],
#             'Fish': data_dict['Fish'],
#             'Sweets': data_dict['Sweets'],
#             'Gold': data_dict['Gold'],
#             'Web': data_dict['Web'],
#             'Catalog': data_dict['Catalog'],
#             'Store': data_dict['Store'],
#             'Discount Purchases': data_dict['Discount_Purchases'],
#             'Total Promo': data_dict['Total_Promo'],
#             'NumWebVisitsMonth': data_dict['NumWebVisitsMonth'],
#         }])

#         # ✅ Use already-loaded transformer & model
#         transformed = transformer.transform(df)
#         pred = model.predict(transformed)

#         return {"predicted_cluster": int(pred[0])}

#     except Exception as e:
#         return {"error": f"Prediction failed: {str(e)}"}

# @app.get("/")
# def read_root():
#     return {"message": "Customer Segmentation API is running"}




from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from datetime import datetime
from src.db import predictions_collection, logs_collection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load artifacts once
transformer = joblib.load("artifacts/transformer.pkl")
model = joblib.load("artifacts/model.pkl")

class InputData(BaseModel):
    Age: int
    Education: int
    Marital_Status: int
    Parental_Status: int
    Children: int
    Income: float
    Total_Spending: float
    Days_as_Customer: int
    Recency: int
    Wines: float
    Fruits: float
    Meat: float
    Fish: float
    Sweets: float
    Gold: float
    Web: int
    Catalog: int
    Store: int
    Discount_Purchases: int
    Total_Promo: int
    NumWebVisitsMonth: int

@app.post("/predict")
def predict(data: InputData):
    try:
        data_dict = data.dict()
        df = pd.DataFrame([{
            'Age': data_dict['Age'],
            'Education': data_dict['Education'],
            'Marital Status': data_dict['Marital_Status'],
            'Parental Status': data_dict['Parental_Status'],
            'Children': data_dict['Children'],
            'Income': data_dict['Income'],
            'Total_Spending': data_dict['Total_Spending'],
            'Days_as_Customer': data_dict['Days_as_Customer'],
            'Recency': data_dict['Recency'],
            'Wines': data_dict['Wines'],
            'Fruits': data_dict['Fruits'],
            'Meat': data_dict['Meat'],
            'Fish': data_dict['Fish'],
            'Sweets': data_dict['Sweets'],
            'Gold': data_dict['Gold'],
            'Web': data_dict['Web'],
            'Catalog': data_dict['Catalog'],
            'Store': data_dict['Store'],
            'Discount Purchases': data_dict['Discount_Purchases'],
            'Total Promo': data_dict['Total_Promo'],
            'NumWebVisitsMonth': data_dict['NumWebVisitsMonth'],
        }])

        transformed = transformer.transform(df)
        pred = model.predict(transformed)
        predicted_cluster = int(pred[0])

        # Save prediction to MongoDB
        predictions_collection.insert_one({
            "input": data_dict,
            "predicted_cluster": predicted_cluster,
            "timestamp": datetime.utcnow()
        })

        return {"predicted_cluster": predicted_cluster}

    except Exception as e:
        logs_collection.insert_one({
            "error": str(e),
            "timestamp": datetime.utcnow()
        })
        return {"error": f"Prediction failed: {str(e)}"}

@app.get("/")
def read_root():
    return {"message": "Customer Segmentation API is running"}
