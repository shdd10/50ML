import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

if __name__ == "__main__":

    website = 'https://www.unenuitnomade.com/fragrance/rose-america/'
    path = '/Users/yueyu1/Downloads/chromedriver_mac64'
    service = Service(path)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options, service=service)
    driver.get(website)
    dropdown = Select(driver.find_element(By.ID, 'pa_volume'))
    dropdown.select_by_value('50-ml')
    time.sleep(6)
    addtocart = driver.find_element(By.ID, 'addtocart')
    classValue = addtocart.get_attribute("class")
    if "disabled" in classValue:
        print("cannot buy")
    time.sleep(2)

