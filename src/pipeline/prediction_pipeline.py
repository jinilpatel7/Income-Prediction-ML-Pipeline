import os, sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from src.utils import load_object

class PredictionPipeline:
    
    def __init__(self):
        pass

    def predict(self, features): 
        logging.info("Prediction Pipeline started running")
        logging.info("Data Transformation Started")
        preprocessor_path = os.path.join("artifacts/data_transformation", "preprocessor.pkl")
        logging.info("Loading The Trained Model")
        model_path = os.path.join("artifacts/model_trainer", "model.pkl")

        processor = load_object(preprocessor_path)
        model = load_object(model_path)


        scaled = processor.transform(features)
        pred = model.predict(scaled)

        logging.info(f"best model found, Model Name is {pred}")
        return pred
        

class CustomeClass:
    def __init__(self, 
                  age:int,
                  workclass:int, 
                  education_num:int, 
                  marital_status:int, 
                  occupation:int,
                  relationship:int,  
                  race:int,
                  sex:int,  
                  capital_gain:int, 
                  capital_loss:int,
                  hours_per_week:int, 
                  native_country:int):
        self.age = age
        self.workclass = workclass
        self.education_num = education_num
        self.marital_status = marital_status
        self.occupation = occupation
        self.relationship = relationship
        self.race = race
        self.sex = sex
        self.capital_gain = capital_gain
        self.capital_loss = capital_loss
        self.hours_per_week = hours_per_week
        self.native_country = native_country


    def get_data_DataFrame(self):
        try:
            custom_input = {
                "age": [self.age],
                "workclass": [self.workclass],
                "education_num":[self.education_num],
                "marital_status":[self.marital_status],
                "occupation":[self.occupation],
                "relationship":[self.relationship],
                "race":[self.race],
                "sex":[self.sex],
                "capital_gain":[self.capital_gain],
                "capital_loss":[self.capital_loss],
                "hours_per_week":[self.hours_per_week],
                "native_country":[self.native_country]

            }

            data= pd.DataFrame(custom_input)

            return data
        except Exception as e:
            raise CustomException(e, sys)