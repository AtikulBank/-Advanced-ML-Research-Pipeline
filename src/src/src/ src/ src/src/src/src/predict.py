import joblib
import numpy as np

model = joblib.load("models/model.pkl")

def predict(features: list):
    features = np.array(features).reshape(1, -1)
    return float(model.predict(features)[0])
