from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    features = [
        float(request.form['open']),
        float(request.form['high']),
        float(request.form['low']),
        float(request.form['close']),
        float(request.form['volume']),
        float(request.form['marketcap']),
        float(request.form['daily_return']),
        float(request.form['ma7']),
        float(request.form['ma14']),
        float(request.form['liquidity_ratio']),
        float(request.form['atr'])
    ]

    features = np.array([features])
    features = scaler.transform(features)

    prediction = model.predict(features)

    return render_template(
        'index.html',
        prediction_text=f'Predicted Volatility: {prediction[0]:.4f}'
    )


if __name__ == '__main__':
    app.run(debug=True)