import pandas as pd
from sklearn.model_selection import train_test_split

class DatasetPreparator:

    def __init__(self,path):
        self.path = path
        self.dataset = None

    def import_dataset(self):
        self.dataset = pd.read_csv(self.path)
        self.dataset = self.dataset.sample(frac=1, random_state=42).reset_index(drop=True)
        print("✅ Dataset downloaded")
        return self.dataset

    def create_test_and_train_set(self, test_size=0.2, random_state=42):
        if self.dataset is None:
            raise ValueError("Dataset not created. Please call import_dataset() first.")
        else:
            try:
                y = self.dataset['note']
                X = self.dataset.drop(columns=['note'])
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
                print("✅ Train and test datasets created")
            except Exception as e:
                print('Error creating train and test sets. Please ensure the dataset is in the correct format.')
        return X_train, X_test, y_train, y_test

from ..params import DATASET_PATH

if __name__ == '__main__':
    dataset_preparator = DatasetPreparator(path=DATASET_PATH)
    dataset_preparator.import_dataset()
    X_train, X_test, y_train, y_test = dataset_preparator.create_test_and_train_set()
    print(X_train.head())
