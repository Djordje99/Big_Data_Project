from preprocessor.data_loader import DataLoader

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from scipy.stats import chisquare, chi2_contingency
from scipy.stats import probplot
from scipy import stats
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


## machine learning libary
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import roc_auc_score, classification_report, confusion_matrix, precision_recall_fscore_support,roc_curve
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

from PyQt5.QtWidgets import QApplication
import sys
from gui.diabetes_controller import DiabetesController
from service.train_model import train
from service.predictor import predict


if __name__ == '__main__':
    predict()
    # app = QApplication(sys.argv)
    # main_window = DiabetesController()

    # main_window.show()
    # sys.exit(app.exec_())

