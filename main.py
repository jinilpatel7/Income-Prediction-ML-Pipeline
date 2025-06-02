from fastapi import FastAPI
from pydantic import BaseModel
import os, sys
from src.exception import CustomException
from src.pipeline.prediction_pipeline import PredictionPipeline, CustomeClass


app = FastAPI()

class InputData(BaseModel):
    age: int
    workclass: int
    education_num: int
    marital_status: int
    occupation: int
    relationship: int
    race: int
    sex: int
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: int

@app.post("/predict")
async def predict_route(data: InputData):
    try:
        custom_data = CustomeClass(
            age=data.age,
            workclass=data.workclass,
            education_num=data.education_num,
            marital_status=data.marital_status,
            occupation=data.occupation,
            relationship=data.relationship,
            race=data.race,
            sex=data.sex,
            capital_gain=data.capital_gain,
            capital_loss=data.capital_loss,
            hours_per_week=data.hours_per_week,
            native_country=data.native_country,
        )
        final_df = custom_data.get_data_DataFrame()
        predict_pipeline = PredictionPipeline()
        prediction = predict_pipeline.predict(final_df)
        label = ">50K" if prediction[0] == 1 else "<=50K"

        return {"prediction": label}
    
    except Exception as e:
        raise CustomException(e, sys)
        
