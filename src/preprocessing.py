import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
import joblib


def load_data(path):
    df = pd.read_csv(path, index_col=0)
    new_list = [column.title() for column in df.columns]
    df.columns = new_list
    return df


def preprocess_data(df):
    df['Date'] = pd.to_datetime(df['Date'])

    # Sort values
    df = df.sort_values(by='Date')

    # Handle missing values
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

    imputer = SimpleImputer(strategy='mean')
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

    return df


def scale_features(X:str):
    # scaler = StandardScaler()
    scaler = RobustScaler()
    X = X.replace([np.inf,-np.inf], np.nan)
    X.dropna()
    X_scaled = scaler.fit_transform(X)

    joblib.dump(scaler, '../scaler.pkl')
    return X_scaled


