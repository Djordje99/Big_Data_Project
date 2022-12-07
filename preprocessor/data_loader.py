import pandas as pd

COLUMN_NAMES = ['Diabetes_012','HighBP','HighChol','CholCheck','BMI','Smoker','Stroke','HeartDiseaseorAttack','PhysActivity','Fruits','Veggies','HvyAlcoholConsump',
                    'AnyHealthcare','NoDocbcCost','GenHlth','MentHlth','PhysHlth','DiffWalk','Sex','Age','Education','Income']

DTYPE = {'Diabetes_012': float,'HighBP': float,'HighChol': float,'CholCheck': float,'BMI': float,'Smoker': float,'Stroke': float,'HeartDiseaseorAttack': float,'PhysActivity': float,'Fruits': float,'Veggies': float,'HvyAlcoholConsump': float,
                    'AnyHealthcare': float,'NoDocbcCost': float,'GenHlth': float,'MentHlth': float,'PhysHlth': float,'DiffWalk': float,'Sex': float,'Age': float,'Education': float,'Income': float}

DATA_PATH = 'D:\\Master\\Big Data\\Projekat\\Big_Data_Project\\training_data\\diabetes.csv'

class DataLoader():
    def __init__(self) -> None:
        pass


    def load_data(self) -> pd.DataFrame:
        data_frame = pd.read_csv(DATA_PATH, names=COLUMN_NAMES, header=None, dtype=DTYPE)
        data_frame = data_frame.drop(index=0)
        data_frame.reset_index()

        return data_frame