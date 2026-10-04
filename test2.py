
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("file:///C:/Users/admin/Documents/final car model - Copy (3)/index.html")
time.sleep(4)
intro_active = driver.execute_script("return typeof introState !== \"undefined\" ? introState.active : null;")
print("INTRO ACTIVE:", intro_active)
intro_start = driver.execute_script("return typeof introState !== \"undefined\" ? introState.startTime : null;")
print("INTRO START:", intro_start)
driver.quit()

