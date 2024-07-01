import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class Preprocessor:
    def __init__(self):
        self.preprocessor = ColumnTransformer(transformers=[
            ('minmax_scaler', MinMaxScaler(), ['wind_speed', 'wind_dir', 'swell_dir']),
            ('standard_scaler', StandardScaler(), ['swell_height', 'swell_period'])
        ], remainder='passthrough')

    def fit(self, X):
        self.preprocessor.fit(X)
        return self

    def transform(self, X):
        X_scaled = pd.DataFrame(self.preprocessor.transform(X))
        X_scaled.columns = X.columns
        print("✅ Dataset scaled")
        return X_scaled
