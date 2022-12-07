from PyQt5.QtCore import *
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
from sklearn.inspection import DecisionBoundaryDisplay

from preprocessor.data_loader import DataLoader


def nnc_display(first_field, second_field):
    loader = DataLoader()
    data_frame = loader.load_data()
    n_neighbors = 10

    data_frame_temp = data_frame.iloc[0:1000, : ]
    X = data_frame_temp[[first_field, second_field]]  #data_frame['GenHlth'] #iris.data[:, :2]
    y = data_frame_temp['Diabetes_012'] #iris.target

    cmap_light = ListedColormap(["orange", "cyan", "cornflowerblue"])
    cmap_bold = ["darkorange", "c", "darkblue"]

    clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
    clf.fit(X, y)

    _, ax = plt.subplots()
    DecisionBoundaryDisplay.from_estimator(
        clf,
        X,
        cmap=cmap_light,
        ax=ax,
        response_method="predict",
        plot_method="pcolormesh",
        xlabel=first_field,
        ylabel=second_field,
        shading="auto",
    )

    sns.scatterplot(
        x=X[first_field],
        y=X[second_field],
        hue=y,
        palette=cmap_bold,
        alpha=1.0,
        edgecolor="black",
    )
    plt.title(
        "3-Class classification (k = %i, weights = '%s')" % (n_neighbors, 'distance')
    )

    plt.show()