
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t
from selenium.webdriver.common.action_chains import ActionChains

## Go to this website and download the correct chromedriver
## for your machine. After downloading, put the driver in this repo.

browser = webdriver.Chrome('./chromedriver')
link = 'https://www.linkedin.com'
browser.get(link)
t.sleep(5)
login_bar = browser.find_element_by_id('login-email')
login_bar.send_keys(<!INSERT YOUR EMAIL TO LOG IN HERE!>)
t.sleep(5)
password_bar = browser.find_element_by_id('login-password')
password_bar.send_keys(<!INSERT YOUR PASSWORD HERE!>)
t.sleep(5)
login_bar.submit()
browser.get("https://www.linkedin.com/psettings/member-data")
t.sleep(5)
export_data = browser.find_element_by_class_name("data-export-option-label").click()
t.sleep(5)
export_button = browser.find_element_by_id("download-button").click()
t.sleep(5)
verify_password = browser.find_element_by_id("verify-password")
verify_password.send_keys(<!INSERT YOUR PASSWORD HERE!>).submit()
