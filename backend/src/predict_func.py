import joblib
import random
import pandas as pd
from pydantic import BaseModel
from src.encoder import Encoder_Func


class InputData(BaseModel):

    id: int
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


class Predict_EV_Buy:

    def __init__(self):

        self.model = joblib.load("./models/model.joblib")
        self.scaler = joblib.load("./models/scaler.joblib")

    def predict(self, input_data: InputData):
        if type(input_data) != dict:
            input_data = dict(input_data)

        data = {"id": random.randint(1,1000), **input_data}
        data = Encoder_Func(pd.DataFrame([data]))
        data = self.scaler.transform(data)

        y_pred = self.model.predict(data)
        
        if int(y_pred[0]) == 1:
            return {"prediction": "Yes will_buy_EV"}
        else:
            return {"prediction": "No will_buy_EV"}