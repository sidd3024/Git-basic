
#Autosuggestive dropdown"
import time
from selenium import webdriver
#calling in the chrome driver to execute or hit chrome browser and executable path is the path of chrome plugin for automating this process
from selenium.webdriver.common.by import By

driver1=webdriver.Chrome(executable_path='/Users/siddharthsrivastava/chromedriver')
driver1.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver1.find_element(By.CSS_SELECTOR,'[id="autosuggest"]').send_keys('de')
time.sleep(2)
countries=driver1.find_elements(By.CSS_SELECTOR,'ul[id="ui-id-1"] li')
for country in countries:
    if country.text=="Denmark":
        country.click()
        break
assert(driver1.find_element(By.CSS_SELECTOR,'[id="autosuggest"]').get_attribute('value')=="Denmark")

