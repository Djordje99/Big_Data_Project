import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings("ignore")

from preprocessor.data_loader import DataLoader


def pca_display(dimensions, first_filed, second_filed):
    loader = DataLoader()
    data_frame = loader.load_data()

    encoder = LabelEncoder()

    for col in data_frame.columns:
        data_frame[col] = encoder.fit_transform(data_frame[col])

    X_features = data_frame.iloc[:,1:22]

    scaler = StandardScaler()
    X_features = scaler.fit_transform(X_features)

    pca2 = PCA(n_components=dimensions)
    pca2.fit(X_features)
    x_3d = pca2.transform(X_features)

    plt.figure(figsize=(8,6))
    plt.scatter(x_3d[0:1000, first_filed], x_3d[0:1000, second_filed], c=data_frame.iloc[0:1000, :]['Diabetes_012'])
    plt.show()
