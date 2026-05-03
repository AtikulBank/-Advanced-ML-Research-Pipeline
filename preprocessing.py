from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def preprocess(df, target, test_size, random_state):
    X = df.drop(columns=[target])
    y = df[target]

    imputer = SimpleImputer(strategy="median")
    X = imputer.fit_transform(X)

    return train_test_split(X, y, test_size=test_size, random_state=random_state)
