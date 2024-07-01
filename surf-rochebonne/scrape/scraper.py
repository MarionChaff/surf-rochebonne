# libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

# params
from ..params import *

 # Number of observations to be collected from Windguru

class Scraper:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def scrape(self, num_prev):

        """
        Scrapes forecast data for a specified number of observations (1 observation = 2-hour period)
        Args:
        * num_prev: Number of forecast periods to scrape.
        Returns:
        * A pandas DataFrame containing the scraped forecast data:
            - Date & hour of estimate
            - Wind and gust speed and direction
            - Swell height, period and direction
        """

        # Wait for the browsed page before scraping
        try:
            myElem = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="tabid_0_0_dates"]/td[1]')))
        except TimeoutException:
            None

        forecast = {}

        parse_number = lambda x: int(''.join([l for l in str(x) if l.isdigit()]))

        # Extract datetime
        temp_list = []
        for i in range(1, num_prev + 1):
            try:
                value = self.driver.find_element(By.XPATH, f'//*[@id="tabid_0_0_dates"]/td[{i}]')
                temp_list.append(value.text)
            except Exception as e:
                temp_list.append(pd.NA)
        forecast['date'] = temp_list

        # Extract numeric figures
        for name in ['tabid_0_0_WINDSPD','tabid_0_0_GUST','tabid_0_0_HTSGW', 'tabid_0_0_PERPW'] :
            temp_list = []
            for i in range(1, num_prev + 1):
                try:
                    value = self.driver.find_element(By.XPATH, f'//*[@id="{name}"]/td[{i}]')
                    numeric_value = float(value.text.strip())  # Convert text to float
                    temp_list.append(numeric_value)
                except Exception as e:
                    temp_list.append(pd.NA)
            forecast[name] = temp_list

        # Extract angles
        for name in ['tabid_0_0_SMER','tabid_0_0_DIRPW']:
            temp_list = []
            for i in range(1, num_prev + 1):
                try:
                    value = self.driver.find_element(By.XPATH, f'//*[@id="{name}"]/td[{i}]/span')
                    numeric_value = parse_number(value.get_attribute('title'))
                    temp_list.append(numeric_value)
                except Exception as e:
                    temp_list.append(pd.NA)
            forecast[name] = temp_list

        forecast_df=pd.DataFrame(forecast)

        # Formatting
        forecast_df.dropna(inplace=True)
        forecast_df.columns = ['date','wind_speed','gust_speed','swell_height','swell_period','wind_dir','swell_dir']
        forecast_df['wind_speed'] = forecast_df[['wind_speed', 'gust_speed']].mean(axis=1)
        forecast_df = forecast_df.drop(columns=['gust_speed'])
        forecast_df[['wind_speed','swell_period']] = forecast_df[['wind_speed','swell_period']].astype(int)

        return forecast_df

if __name__ == '__main__':
    scraper = Scraper(WG_URL)
    forecast_df = scraper.scrape(NUM_PREV)
    print(forecast_df)
