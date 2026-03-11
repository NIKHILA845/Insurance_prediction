import pickle
import numpy as np

class Insurance_Prediction:

    def __init__(self):
        artifacts_path = os.path.join(os.path.dirname(__file__), '..', 'artifacts')
        with open(os.path.join(artifacts_path, 'scaler.pkl'),'rb') as f:
            self.scaler = pickle.load(f)
        with open(os.path.join(artifacts_path, 'model.pkl'),'rb') as f:
            self.model = pickle.load(f)

    def prediction(self, Age, Annual_Income_LPA, Policy_Term_Years, Sum_Assured_Lakhs):
        input_data = np.array([[Age, Annual_Income_LPA, Policy_Term_Years, Sum_Assured_Lakhs]])
        scaled_input = self.scaler.transform(input_data)
        result = self.model.predict(scaled_input)
        return result[0]