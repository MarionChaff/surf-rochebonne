import pandas as pd

class OneHotEncoder:

    def __init__(self, nb_classes=4):
        self.nb_classes = nb_classes

    def transform(self, y):
        y_encoded = {}
        for i in range(self.nb_classes + 1):
            y_encoded[i] = (y == i).astype(int)
        print(f'✅ target encoded')
        return pd.DataFrame(y_encoded)
