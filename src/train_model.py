import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
from preprocessing import load_data, preprocess_data, scale_features
from feature_engineering import create_features


# Load Dataset
path = '../dataset/dataset.csv'
df = load_data(path)

# Preprocessing
df = preprocess_data(df)

# Feature Engineering
df = create_features(df)

# Features and Target
features = [
    'Open',
    'High',
    'Low',
    'Close',
    'Volume',
    'Marketcap',
    'Daily_Return',
    'MA_7',
    'MA_14',
    'Liquidity_Ratio',
    'ATR'
]

X = df[features]
y = df['Volatility']

# Scaling
X_scaled = scale_features(X)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Metrics
rmse = mean_squared_error(y_test, predictions) ** 0.5
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print('RMSE:', rmse)
print('MAE:', mae)
print('R2 Score:', r2)

# Save Model
joblib.dump(model, '../model.pkl')

print('Model Saved Successfully!')
