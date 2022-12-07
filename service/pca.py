import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")

from preprocessor.data_loader import DataLoader


def pca_display():
    loader = DataLoader()
    data_frame = loader.load_data()

    # Machine learning systems work with integers, we need to encode these
    # string characters into ints

    encoder = LabelEncoder()

    # Now apply the transformation to all the columns:
    for col in data_frame.columns:
        data_frame[col] = encoder.fit_transform(data_frame[col])

    X_features = data_frame.iloc[:,1:22]
    y_label = data_frame.iloc[:, 0]

    # Scale the features
    scaler = StandardScaler()
    X_features = scaler.fit_transform(X_features)

    pca = PCA()
    pca.fit_transform(X_features)
    pca_variance = pca.explained_variance_

    plt.figure(figsize=(8, 6))
    plt.bar(range(21), pca_variance, alpha=0.5, align='center', label='individual variance')
    plt.legend()
    plt.ylabel('Variance ratio')
    plt.xlabel('Principal components')
    plt.show()

    pca2 = PCA(n_components=17)
    pca2.fit(X_features)
    x_3d = pca2.transform(X_features)

    plt.figure(figsize=(8,6))
    plt.scatter(x_3d[0:1000, 0], x_3d[0:1000, 5], c=data_frame.iloc[0:1000, :]['BMI'])
    plt.show()

    pca3 = PCA(n_components=2)
    pca3.fit(X_features)
    x_3d = pca3.transform(X_features)

    plt.figure(figsize=(8,6))
    plt.scatter(x_3d[0:1000, 0], x_3d[0:1000, 1], c=data_frame.iloc[0:1000, :]['BMI'])
    plt.show()