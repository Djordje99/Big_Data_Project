from xgboost import XGBClassifier
import pandas as pd

ATTRIBUTES = ['BMI', 'MentHlth', 'PhysHlth', 'Income', 'Education', 'Age', 'GenHlth']

def predict(data_frame_row):
    xgb = XGBClassifier()
    xgb.load_model('model/model')

    data_frame = prepare_data(data_frame_row)

    data_frame = pd.DataFrame([[1.0,1.0,1.0,40.0,1.0,0.0,0.0,0.0,0.0,1.0,0.0,1.0,0.0,5.0,18.0,15.0,1.0,0.0,9.0,4.0]])
    print(data_frame)
    prediction = xgb.predict(data_frame)

    print(prediction)


def __prepare_data(data_frame_row):
    pass