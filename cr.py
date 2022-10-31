from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import pandas as pd
import time
import datetime


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://cryptoroyale.one/skins?m=marketplace')

time.sleep(180)

webtable_df = pd.read_html(driver.find_element(By.XPATH,"//table[@id='markettable']").get_attribute('outerHTML'))[0]

jetzt = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
dateiname = jetzt + str('.csv')

webtable_df.to_csv(dateiname)

driver.quit()
