import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.windguru.cz/112'
exec_path = '/Users/marionchaffaut/chromedriver/chromedriver-mac-x64/chromedriver' # Put as ENV
num_prev = 100 # Number of observations to be collected from Windguru

class Scraper:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(executable_path=exec_path)

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

        self.driver.get(self.url)
        forecast = {}

        names_fig = ['tabid_0_0_dates','tabid_0_0_WINDSPD','tabid_0_0_GUST','tabid_0_0_HTSGW', 'tabid_0_0_PERPW']
        names_dir = ['tabid_0_0_SMER','tabid_0_0_DIRPW']

        for name in names_fig:
            temp_list = []
            for i in range(1, num_prev + 1):
                try:
                    value = self.driver.find_element(By.XPATH, f'//*[@id="{name}"]/td[{i}]')
                    temp_list.append(value.text)
                except Exception as e:
                    temp_list.append('na')
            forecast[name] = temp_list

        for name in names_dir:
            temp_list = []
            for i in range(1, num_prev + 1):
                try:
                    value = self.driver.find_element(By.XPATH, f'//*[@id="{name}"]/td[{i}]/span')
                    temp_list.append(value.get_attribute('title'))
                except Exception as e:
                    temp_list.append('na')
            forecast[name] = temp_list

        forecast_df=pd.DataFrame(forecast)

        return forecast_df

if __name__ == '__main__':
    scraper = Scraper(url)
    forecast_df = scraper.scrape(num_prev)
