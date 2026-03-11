# load training and testing data
#scale the training data
#save  scaled data into processed folder
from data_preprocessing import load_and_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle
x_train,x_test,y_train,y_test=load_and_split()
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)

pd.DataFrame(x_train_scaled).to_csv(r"C:\Users\Nikhila sri\OneDrive\Documents\TECKWORKS\day 15\projects\Insurance_prediction\data\processed\x_train.csv",index=False)
pd.DataFrame(x_test_scaled).to_csv(r"C:\Users\Nikhila sri\OneDrive\Documents\TECKWORKS\day 15\projects\Insurance_prediction\data\processed\x_test.csv",index=False)
pd.DataFrame(y_train).to_csv(r"C:\Users\Nikhila sri\OneDrive\Documents\TECKWORKS\day 15\projects\Insurance_prediction\data\processed\y_train.csv",index=False)
pd.DataFrame(y_test).to_csv(r"C:\Users\Nikhila sri\OneDrive\Documents\TECKWORKS\day 15\projects\Insurance_prediction\data\processed\y_test.csv",index=False)

with open("../artifacts/scaler.pkl","wb") as f:
    pickle.dump(scaler,f)