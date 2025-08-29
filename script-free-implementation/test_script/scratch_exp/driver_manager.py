from selenium import webdriver
from selenium.common.exceptions import (NoAlertPresentException,
                                        UnexpectedAlertPresentException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service


class DriverManager:
    def __init__(self):
        service = Service(executable_path="chrome_deps/bin/chromedriver113")
        options = webdriver.ChromeOptions()
        options.binary_location = "chrome_deps/bin/chrome113"
        options.add_experimental_option("prefs", {"intl.accept_languages": "en_US"})
        options.add_experimental_option("detach", True)
        options.add_argument("--no-sandbox")
        self.__driver = webdriver.Chrome(service=service, options=options)
    
    def get_driver(self):
        return self.__driver
    
    def quit(self):
        self.__driver.quit()
