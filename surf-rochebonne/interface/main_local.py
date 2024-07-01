# modules
from ..ml_logic.data import DatasetPreparator
from ..ml_logic.preprocessor import Preprocessor
from ..scrape.scraper import Scraper

# params
from ..params import *

if __name__ == '__main__':

    # downloads and splits data
    dataset_preparator = DatasetPreparator(path=DATASET_PATH)
    dataset_preparator.import_dataset()
    X_train, X_test, y_train, y_test = dataset_preparator.create_test_and_train_set()

    # preprocess (scale) data
    preprocessor = Preprocessor()
    preprocessor.fit(X_train)
    X_train_scaled = preprocessor.transform(X_train)
    X_test_scaled = preprocessor.transform(X_test)

    # train model


    # scrape windguru surf forecast
    scraper = Scraper(WG_URL)
    forecast_df = scraper.scrape(NUM_PREV)

    # predict surf condition
