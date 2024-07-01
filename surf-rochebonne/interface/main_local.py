from ..ml_logic.data import DatasetPreparator
from ..ml_logic.preprocessor import Preprocessor
from ..ml_logic.encode import OneHotEncoder
from ..scrape.scraper import Scraper
from ..ml_logic.model import Model
from ..params import *

#surf-rochebonne.interface.main_local

if __name__ == '__main__':

    # Downloads and splits data
    dataset_preparator = DatasetPreparator(path=DATASET_PATH)
    dataset_preparator.import_dataset()
    X_train, X_test, y_train, y_test = dataset_preparator.create_test_and_train_set()

    # Preprocess (scale) X data
    preprocessor = Preprocessor()
    preprocessor.fit(X_train)
    X_train_scaled = preprocessor.transform(X_train)
    X_test_scaled = preprocessor.transform(X_test)

    # Encode y data
    encoder = OneHotEncoder(nb_classes=4)
    y_train_encoded = encoder.transform(y_train)
    print(y_train_encoded.shape)
    y_test_encoded = encoder.transform(y_test)
    print(y_test_encoded.shape)

    # Fit model
    model = Model()
    model.fit(X_train_scaled,y_train_encoded)

    # Scrape Windguru surf forecast (new X)
    #scraper = Scraper(WG_URL)
    #forecast_df = scraper.scrape(NUM_PREV)

    # Select features and preprocess surf forecast (new X)
    #X_forecast_scaled = preprocessor.transform(forecast_df)

    # predict surf condition
    #forecast_df['note'] = model.predict(X_forecast_scaled)
