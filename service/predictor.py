from xgboost import XGBClassifier
import pandas as pd

ATTRIBUTES = ['BMI', 'MentHlth', 'PhysHlth', 'Income', 'Education', 'Age', 'GenHlth']

def predict(data_frame_row):
    xgb = XGBClassifier()
    xgb.load_model('model/model')

    data_frame = __prepare_data(data_frame_row)

    print(data_frame)
    prediction = xgb.predict(data_frame)

    return prediction


def __prepare_data(data_frame_row):
    data_frame = pd.DataFrame([data_frame_row])

    data_frame['BMI'] = (data_frame['BMI'] - 12) / (98 - 12)   #(value - min) / (max - min)
    data_frame['MentHlth'] = (data_frame['MentHlth'] - 1) / (30 - 1)
    data_frame['PhysHlth'] = (data_frame['PhysHlth'] - 1) / (30 - 1)
    data_frame['Income'] = (data_frame['Income'] - 1) / (8 - 1)
    data_frame['Education'] = (data_frame['Education'] - 1) / (6 - 1)
    data_frame['Age'] = (data_frame['Age'] - 1) / (13 - 1)
    data_frame['GenHlth'] = (data_frame['GenHlth'] - 1) / (5 - 1)

    return data_frame
