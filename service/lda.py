from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from preprocessor.data_loader import DataLoader


COLUMN_NAMES = ['HighBP','HighChol','CholCheck','BMI','Smoker','Stroke','HeartDiseaseorAttack','PhysActivity','Fruits','Veggies','HvyAlcoholConsump',
                    'AnyHealthcare','NoDocbcCost','GenHlth','MentHlth','PhysHlth','DiffWalk','Sex','Age','Education','Income']
DIMENSIONS = list([i for i in range(1, 22)])

DICT_COLUMN = dict(zip(COLUMN_NAMES, DIMENSIONS))

def lda_display():
    loader = DataLoader()
    data_frame = loader.load_data()

    X = data_frame.iloc[0:1000,1:22]
    y = data_frame.iloc[0:1000, 0]

    model = LinearDiscriminantAnalysis()
    data_plot = model.fit(X, y).transform(X)

    plt.figure()

    plt.scatter(data_plot[y == 0, 0], data_plot[y == 0, 1], alpha=.8, label='No Diabetes')
    plt.scatter(data_plot[y == 1, 0], data_plot[y == 1, 1], alpha=.8, label='Pre Diabetes')
    plt.scatter(data_plot[y == 2, 0], data_plot[y == 2, 1], alpha=.8, label='Diabetes')


    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.show()
