import pandas as pd
import numpy as np


def create_features(df):

    # Daily Return
    df['Daily_Return'] = ((df['Close'] - df['Open']) / df['Open']) * 100

    # Rolling Volatility
    df['Volatility'] = df['Daily_Return'].rolling(window=7).std()

    # Moving Average
    df['MA_7'] = df['Close'].rolling(window=7).mean()
    df['MA_14'] = df['Close'].rolling(window=14).mean()

    # Liquidity Ratio
    df['Liquidity_Ratio'] = df['Volume'] / df['Marketcap']

    # Bollinger Bands
    rolling_std = df['Close'].rolling(window=20).std()
    df['Upper_Band'] = df['MA_14'] + (rolling_std * 2)
    df['Lower_Band'] = df['MA_14'] - (rolling_std * 2)

    # ATR Approximation
    df['ATR'] = df['High'] - df['Low']

    df = df.dropna()

    return df