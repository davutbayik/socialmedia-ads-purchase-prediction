from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

# Initialize FastAPI
app = FastAPI()

# Load the ML model
with open("model/xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define the input data model for prediction
class UserData(BaseModel):
    Gender: str
    Age: int
    EstimatedSalary: int

@app.get("/")
def read_root():
    return {"message": "Social Network Ad Purchasing Predictor API is running. Use POST /predict to get predictions."}

@app.post("/predict")
def predict(user_data: UserData):
    # Prepare data for prediction
    data = pd.DataFrame({
        'Gender': [user_data.Gender],
        'Age': [user_data.Age],
        'EstimatedSalary': [user_data.EstimatedSalary]
    })
    
    prediction = model.predict(data)
    
    # Return the prediction result (1 for Purchased, 0 for Not Purchased)
    return {"purchase": "Purchased" if prediction[0] == 1 else "Not Purchased"}
