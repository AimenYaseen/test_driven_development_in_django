import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

time.sleep(5)  # Let the user actually see something!

assert browser.page_source.find("install")

time.sleep(5)  # Let the user actually see something!

browser.quit()
