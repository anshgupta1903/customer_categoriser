# Customer Segmentation Project

An end-to-end machine learning project to predict customer segments using FastAPI, MongoDB, Docker, and a simple HTML frontend.

---

##  Features
- Predicts customer cluster from user input
- Stores predictions and errors in MongoDB
- Built with Docker for easy local running
- Includes a simple HTML frontend to test the API

---

## Requirements
- Docker installed ([Download here](https://www.docker.com/get-started))
- MongoDB URI (from MongoDB Atlas or local)

---

##  Setup & Run (Local Demo)

### 1 Clone this repo
```
git clone https://github.com/anshgupta1903/customer_categoriser/
cd customer_categoriser
```

# 2 Create .env file
In the root folder, create a .env file:

MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>?retryWrites=true&w=majority



# 3 Run with Docker
Build Docker image

docker build -t customer-segmentation-api .
Run container

docker run --env-file .env -p 8000:8000 customer-segmentation-api

## you can also create docker-compose.yml and use the command 
#### docker-compose up --build
#### once built you can run just by a single command
#### docker-compose up



#### Now your API is running at:📍 http://127.0.0.1:8000


## Test with frontend Open index.html in your browser. Fill out the form → click Predict Cluster. See the predicted cluster below the form.

# 🚀 Running locally (without Docker)
### Start backend (FastAPI):

uvicorn src.app:app --reload
It will run on http://127.0.0.1:8000.

### Start frontend:

Open frontend/index.html directly in your browser.



# API Endpoints
Method	URL	Description
GET	/	Health check
POST	/predict	Predict customer cluster


# 📂 Project structure

```plaintext
customer_categoriser/
├── artifacts/                   # ML artifacts (trained models, transformers)
│   ├── model.pkl
│   └── transformer.pkl
├── customer_categoriser/        # Python virtual environment (should be ignored)
│   ├── ~gboost/
│   ├── etc/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── share/
│   └── pyvenv.cfg
├── frontend/                    # Frontend (HTML app)
│   ├── Dockerfile
│   └── index.html
├── notebooks/                   # Jupyter notebooks & data exploration
│   ├── data/
│   ├── EDA.ipynb
│   ├── Feature_engineering.ipynb
│   ├── Feature_Selection_and_Modeling.ipynb
│   └── marketing_campaign.ipynb
├── src/                         # Backend FastAPI app and ML pipeline
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_evaluation.py
│   │   └── model_trainer.py
│   ├── pipelines/
│   │   ├── prediction_pipeline.py
│   │   └── training_pipeline.py
│   ├── utils/
│   ├── app.py
│   └── db.py
├── .env                         # Environment variables
├── .gitignore                   # Files/folders to ignore in git
├── docker-compose.yml           # Docker Compose file
├── Dockerfile                   # Backend Dockerfile
├── main.py                      # Entry script if needed
├── requirements.txt             # Python dependencies
└── test.py                      # Test script
```
# Author
## Ansh Gupta