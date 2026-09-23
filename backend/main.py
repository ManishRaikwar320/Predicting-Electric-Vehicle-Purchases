from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.predict_func import Predict_EV_Buy

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Predict_EV = Predict_EV_Buy()

class EVData(BaseModel):
    Age: int
    Annual_Income_USD: float
    Daily_Commute_km: float
    Number_of_Cars_Owned: int
    Charging_Stations_Near_Home: int
    Charging_Stations_Near_Work: int
    Environmental_Concern_Level: float
    Gender: str
    City_Type: str
    Current_Car_Type: str
    Home_Charging_Possible: str
    Subsidy_Available: str
    Range_Anxiety_Level: str



@app.post("/predict")
def predict(data: EVData):

    result = Predict_EV.predict(data.model_dump())

    return result 