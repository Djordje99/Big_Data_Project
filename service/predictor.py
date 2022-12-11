from xgboost import XGBClassifier
import pandas as pd


def predict():
    xgb = XGBClassifier()
    xgb.load_model('model/model')

    data_frame = pd.DataFrame([[1.0,1.0,1.0,40.0,1.0,0.0,0.0,0.0,0.0,1.0,0.0,1.0,0.0,5.0,18.0,15.0,1.0,0.0,9.0,4.0]])
    print(data_frame)
    prediction = xgb.predict(data_frame)

    print(prediction)