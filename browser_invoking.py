from selenium import webdriver
#calling in the chrome driver to execute or hit chrome browser and executable path is the path of chrome plugin for automating this process
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='/Users/siddharthsrivastava/chromedriver')
driver.get('https://rahulshettyacademy.com/angularpractice/')#Hitting the Url
print('The title of the url is',driver.title)
print("Current Url is",driver.current_url)
#driver.find_elements_by_name('name').send_keys("siddharht")
driver.find_element(By.NAME,'name').send_keys("siddharth")
driver.find_element(By.CSS_SELECTOR,'[name="email"]').send_keys("sidd.245@gmail.com")
driver.find_element(By.XPATH,'//input[contains(@placeholder,"Password")]').send_keys('12345')
driver.find_element(By.CSS_SELECTOR,'[type="checkbox"]').click()
driver.find_element(By.XPATH,'//div[@class="form-group"]/div[2]').click()
driver.find_element(By.XPATH,'//div[@class="container"]/form/input[@value="Submit"]').click()
print("Text printed in the screen is",driver.find_element(By.CSS_SELECTOR,'div.alert-success').text)







