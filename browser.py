from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Browser:
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

