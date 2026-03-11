#load scaler.pkl and model.pkl files
# create a function to predict
import pickle
import numpy as np

class Insurance_Prediction:
    def __init__(self):
        with open("C:\\Users\\Nikhila sri\\OneDrive\\Documents\\TECKWORKS\\day 15\\projects\\Insurance_prediction\\artifacts\\scaler.pkl","rb") as f:
            self.scaler=pickle.load(f)
        with open("C:\\Users\\Nikhila sri\\OneDrive\\Documents\\TECKWORKS\\day 15\\projects\\Insurance_prediction\\artifacts\\model.pkl","rb") as f:
            self.model=pickle.load(f)
    def prediction(self,Age,Annual_Income_LPA,Policy_Term_Years,Sum_Assured_Lakhs):
        input=np.array([[Age,Annual_Income_LPA,Policy_Term_Years,Sum_Assured_Lakhs]])
        scaled_input=self.scaler.transform(input)
        result=self.model.predict(scaled_input)
        return result[0]