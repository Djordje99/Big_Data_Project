import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE

from preprocessor.data_loader import DataLoader


def __normalize_variable():
    loader = DataLoader()
    data_frame = loader.load_data()

    num_attribs = ['BMI', 'MentHlth', 'PhysHlth', 'Income', 'Education', 'Age', 'GenHlth']

    cat_attribs = list(data_frame.columns[~data_frame.columns.isin(['BMI', 'MentHlth', 'AnyHealthcare', 'Income', 'Education', 'Age', 'GenHlth',
                                                    'PhysHlth', 'Diabetes_012'])])

    data_frame[cat_attribs] = data_frame[cat_attribs].astype('category')
    data_frame.Diabetes_012 = data_frame.Diabetes_012.astype('int')

    for num in num_attribs:
        data_frame[num] = (data_frame[num] - data_frame[num].min()) / (data_frame[num].max() - data_frame[num].min())

    label_map = {0:0, 1:1, 2:1}

    data_frame['Diabetes_012'] = data_frame['Diabetes_012'].map(label_map)

    return data_frame, num_attribs, cat_attribs



def train():
    data_frame, num_attribs, cat_attribs = __normalize_variable()

    y = data_frame.Diabetes_012

    attribs = data_frame[num_attribs + cat_attribs]

    X = pd.get_dummies(attribs, drop_first=True)

    print(X)

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, stratify=y, random_state=33)

    print(X_train)

    eval_set = [(X_val, y_val)]

    oversample = SMOTE(random_state=33)
    X_train, y_train = oversample.fit_resample(X_train, y_train)

    params = {
        'objective': 'binary:logistic',
        'n_estimators': 400,
        'max_depth': 4,
        'learning_rate': 0.2,
        'reg_alpha': 0.5,
        'subsample': 0.5,
        'colsample_bytree': 0.8,
        'random_state': 33,
        'use_label_encoder':False
            }

    xgb = (
        XGBClassifier(**params)
        .fit(X_train, y_train,
            eval_set=eval_set,
            eval_metric='error',
            verbose=True,
            early_stopping_rounds=10)
    )

    print(X_val)
    print('Model name: XGBoost Classifier')
    print('Accuracy: ', '{}%'.format(round((accuracy_score(y_val, xgb.predict(X_val)) * 100), 2)))

    xgb.save_model('model/model')

    print(classification_report(y_val, xgb.predict(X_val), target_names=['no_diabetes', 'prediabetes_or_diabetes']))

    table = pd.DataFrame(list(zip(X.columns,xgb.feature_importances_)),
                                        columns=['Feature', 'Importance (%)'])

    table['Importance (%)'] = (table['Importance (%)']
                            .apply(lambda row: round((row * 100),2)))
