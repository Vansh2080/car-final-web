
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('file:///C:/Users/admin/Documents/final car model - Copy (3)/index.html')
time.sleep(2)
try:
    error_el = driver.find_element('xpath', '//div[contains(text(), \'INTRO ERROR\')]')
    print('DOM ERROR:', error_el.text)
except Exception as e:
    print('NO ERROR IN DOM')
driver.quit()

