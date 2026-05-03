import numpy as np

def transform_features(X):
    return np.log1p(X)
