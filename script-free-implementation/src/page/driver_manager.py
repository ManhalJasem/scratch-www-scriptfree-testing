import Setting
import shutil
import tempfile
from script.locator import Locator, LocatorType
from selenium import webdriver
from selenium.common.exceptions import (NoAlertPresentException,
                                        UnexpectedAlertPresentException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service


class DriverManager:
    def __init__(self, app_specific_options=None):
        service = Service(executable_path=Setting.CHROMEDRIVER_LOCATION)
        options = webdriver.ChromeOptions()
        options.binary_location = Setting.BINARY_LOCATION
        options.add_experimental_option("prefs", {"intl.accept_languages": "en_US"})
        options.add_argument("--no-sandbox")
        if app_specific_options:
            temp_profile = tempfile.mkdtemp()
            shutil.copytree("chrome-profiles/mm-chrome-profile", temp_profile, dirs_exist_ok=True, symlinks=True)
            options.add_argument(f"--user-data-dir={temp_profile}")
            options.add_argument(app_specific_options[1])
        if Setting.HEADLESS:
            options.add_argument("--headless")
        self.__driver = webdriver.Chrome(service=service, options=options)

    def quit(self):
        self.__driver.quit()

    def open(self, url):
        try:
            self.__driver.get(url)
        except UnexpectedAlertPresentException:
            try:
                alert = self.__driver.switch_to.alert
                alert.accept()
                print("Alert accepted")
                self.__driver.get(url)
            except NoAlertPresentException:
                pass

    def enter(self, locator: Locator, value: str):
        element = self.__locate(locator)
        element.clear()
        element.send_keys(value)

    def select(self, locator: Locator, value: str):
        element = self.__locate(locator)
        Select(element).select_by_visible_text(value)

    def click(self, locator: Locator):
        element = self.__locate(locator)
        element.click()
    
    def assert_element(self, locator: Locator):
        element = self.__locate(locator)
        assert element.is_displayed()

    def execute_script(self, script: str):
        self.__driver.execute_script(script)
    
    def get_screenshot_as_png(self):
        self.__driver.get_screenshot_as_png()

    def get_page_source(self) -> str:
        try:
            return self.__driver.page_source
        except UnexpectedAlertPresentException:
            try:
                alert = self.__driver.switch_to.alert
                alert.accept()
                print("Alert accepted")
                return self.__driver.page_source
            except NoAlertPresentException:
                return ""

    def __locate(self, locator: Locator):
        if locator.locator_type == LocatorType.NAME:
            return self.__driver.find_element(By.NAME, locator.value)
        elif locator.locator_type == LocatorType.ID:
            return self.__driver.find_element(By.ID, locator.value)
        elif locator.locator_type == LocatorType.LINK_TEXT:
            return self.__driver.find_element(By.LINK_TEXT, locator.value)
        elif locator.locator_type == LocatorType.XPATH:
            return self.__driver.find_element(By.XPATH, locator.value)
