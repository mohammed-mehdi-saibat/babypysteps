from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Initialize the API application
app = FastAPI(title="Titanic Survival Prediction API")

# 1. Load the trained model into the server's memory at startup
model = joblib.load('titanic_model.pkl')

# 2. Define the strict JSON schema expected from the user
class Passenger(BaseModel):
    Pclass: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Sex_female: int
    Sex_male: int
    Embarked_C: int
    Embarked_Q: int
    Embarked_S: int

# Our original health-check endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Titanic API! The server is running perfectly."}

# 3. The new Machine Learning endpoint
@app.post("/predict")
def predict_survival(passenger: Passenger):
    # Convert the incoming JSON into a Pandas DataFrame
    # .model_dump() turns the Pydantic object into a standard dictionary
    data = pd.DataFrame([passenger.model_dump()])
    
    # Pass the single passenger through the Logistic Regression model
    prediction = model.predict(data)
    
    # The model returns an array like [0] or [1]. We grab the first item and cast it to a boolean.
    survived = bool(prediction[0])
    
    return {"survived": survived}