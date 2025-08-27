from abc import ABCMeta, abstractmethod, abstractproperty
from time import sleep
from typing import Optional

import Setting
from page.driver_manager import DriverManager

from script.locator import Locator, LocatorType
from script.operation_type import OperationType
from datetime import datetime
import random


class Step(metaclass=ABCMeta):
    def __init__(self, raw_string: str):
        self.__raw_string = raw_string

    @property
    def raw_string(self):
        return self.__raw_string

    @abstractproperty
    def operation_type(self) -> OperationType:
        return OperationType.PAGE_TRANSITION


class CodableOperation(Step, metaclass=ABCMeta):
    @abstractmethod
    def to_code(self) -> str:
        pass


class ExecutableOperation(CodableOperation, metaclass=ABCMeta):
    def __init__(self, raw_string: str):
        super().__init__(raw_string)

    @abstractmethod
    def execute(self, driver_manager: DriverManager) -> str:
        pass


class LocatableOperation(ExecutableOperation, metaclass=ABCMeta):
    def __init__(self, raw_string: str, target: str, once: bool):
        super().__init__(raw_string)
        self.__target = target
        self.__once = once

    @property
    def target(self) -> str:
        return self.__target

    @property
    def once(self) -> bool:
        return self.__once

    @abstractmethod
    def to_code(self, locator: Locator) -> str:
        pass

    @abstractmethod
    def execute(self, locator: Locator, driver_manager: DriverManager) -> str:
        pass

    def get_locator(self) -> Optional[Locator]:
        if self.target[0] == "#":
            return Locator(LocatorType.ID, self.target[1:])
        elif self.target[0:6] == "xpath:":
            return Locator(LocatorType.XPATH, self.target[6:])
        elif self.target[0:5] == "link:":
            return Locator(LocatorType.LINK_TEXT, self.target[5:])
        else:
            return None


class Open(ExecutableOperation):
    def __init__(self, raw_string: str, value: str):
        Step.__init__(self, raw_string)
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value

    @property
    def operation_type(self) -> OperationType:
        return OperationType.OPEN

    def to_code(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = "{}_{}_{}.png".format(
            self.operation_type.name.replace(" ", "_").lower(),
            timestamp,
            random.randint(1000, 9999)
        )
        return (
            "driver.get('{}')".format(self.value)
            + "\n    "
            + "driver.implicitly_wait(10)"
            + "\n    "
            + "driver.save_screenshot('{}/{}')".format(Setting.SCREENSHOT_FOLDER, screenshot_name)
        )

    def execute(self, driver_manager: DriverManager) -> None:
        driver_manager.open(self.value)
        sleep(Setting.TRANSITION_SLEEP_TIME)
        driver_manager.get_screenshot_as_png()


class Enter(LocatableOperation):
    def __init__(self, raw_string: str, target: str, value: str, once: bool):
        LocatableOperation.__init__(self, raw_string, target, once)
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value

    @property
    def operation_type(self) -> OperationType:
        return OperationType.ENTER

    def to_code(self, locator: Locator):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = "{}_{}_{}.png".format(
            self.operation_type.name.replace(" ", "_").lower(),
            timestamp,
            random.randint(1000, 9999)
        )
        return (
            "driver.find_element(By.{},'{}').screenshot('{}/{}')".format(
                locator.locator_type.value, locator.value, Setting.SCREENSHOT_FOLDER, screenshot_name
            )
            + "\n    "
            + "driver.find_element(By.{},'{}').clear()".format(
                locator.locator_type.value, locator.value
            )
            + "\n    "
            + "driver.find_element(By.{},'{}').send_keys('{}')".format(
                locator.locator_type.value, locator.value, self.value
            )
        )

    def execute(self, locator: Locator, driver_manager: DriverManager) -> None:
        sleep(Setting.SLEEP_TIME)
        if Setting.SHOW_OPERATION:
            print("enter {} in {}".format(self.value, locator.value))
        driver_manager.enter(locator, self.value)
        driver_manager.get_screenshot_as_png()


class Select(LocatableOperation):
    def __init__(self, raw_string: str, target: str, value: str, once: bool):
        LocatableOperation.__init__(self, raw_string, target, once)
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value

    @property
    def operation_type(self) -> OperationType:
        return OperationType.SELECT

    def to_code(self, locator: Locator):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = "{}_{}_{}.png".format(
            self.operation_type.name.replace(" ", "_").lower(),
            timestamp,
            random.randint(1000, 9999)
        )
        return (
            "driver.find_element(By.{},'{}').screenshot('{}/{}')".format(
                locator.locator_type.value, locator.value, Setting.SCREENSHOT_FOLDER, screenshot_name
            )
            + "\n    "
            + "Select(driver.find_element(By.{},'{}')).select_by_visible_text('{}')".format(
                locator.locator_type.value, locator.value, self.value
            )
        )

    def execute(self, locator: Locator, driver_manager: DriverManager) -> None:
        sleep(Setting.SLEEP_TIME)
        if Setting.SHOW_OPERATION:
            print("select {} from {}".format(self.value, locator.value))
        driver_manager.select(locator, self.value)
        driver_manager.get_screenshot_as_png()


class Click(LocatableOperation):
    def __init__(self, raw_string: str, target: str, once: bool):
        LocatableOperation.__init__(self, raw_string, target, once)

    @property
    def operation_type(self) -> OperationType:
        return OperationType.CLICK

    def to_code(self, locator: Locator):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = "{}_{}_{}.png".format(
            self.operation_type.name.replace(" ", "_").lower(),
            timestamp,
            random.randint(1000, 9999)
        )
        return ( 
            "driver.find_element(By.{},'{}').screenshot('{}/{}')".format(
                locator.locator_type.value, locator.value, Setting.SCREENSHOT_FOLDER, screenshot_name
            )
            + "\n    "
            + "driver.find_element(By.{},'{}').click()".format(
                locator.locator_type.value, locator.value
            )
        )

    def execute(self, locator: Locator, driver_manager: DriverManager) -> None:
        sleep(Setting.SLEEP_TIME)
        if Setting.SHOW_OPERATION:
            print("click {}".format(locator.value))
        driver_manager.click(locator)
        driver_manager.get_screenshot_as_png()

class ClickDiv(LocatableOperation):
    def __init__(self, raw_string: str, target: str, once: bool):
        LocatableOperation.__init__(self, raw_string, target, once)

    @property
    def operation_type(self) -> OperationType:
        return OperationType.CLICK_DIV

    def to_code(self, locator: Locator):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = "{}_{}_{}.png".format(
            self.operation_type.name.replace(" ", "_").lower(),
            timestamp,
            random.randint(1000, 9999)
        )
        return ( 
            "driver.find_element(By.{},'{}').screenshot('{}/{}')".format(
                locator.locator_type.value, locator.value, Setting.SCREENSHOT_FOLDER, screenshot_name
            )
            + "\n    "
            + "driver.find_element(By.{},'{}').click()".format(
                locator.locator_type.value, locator.value
            )
        )

    def execute(self, locator: Locator, driver_manager: DriverManager) -> None:
        sleep(Setting.SLEEP_TIME)
        if Setting.SHOW_OPERATION:
            print("click div {}".format(locator.value))
        driver_manager.click(locator)
        driver_manager.get_screenshot_as_png()

class AssertElement(LocatableOperation):
    def __init__(self, raw_string: str, target: str, once: bool):
        LocatableOperation.__init__(self, raw_string, target, once)

    @property
    def operation_type(self) -> OperationType:
        return OperationType.ASSERT_ELEMENT

    def to_code(self, locator: Locator):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = "{}_{}_{}.png".format(
            self.operation_type.name.replace(" ", "_").lower(),
            timestamp,
            random.randint(1000, 9999)
        )
        return ( 
            "assert driver.find_element(By.{},'{}').is_displayed()".format(
                locator.locator_type.value, locator.value
            )
            + "\n    " 
            + "driver.find_element(By.{},'{}').screenshot('{}/{}')".format(
                locator.locator_type.value, locator.value, Setting.SCREENSHOT_FOLDER, screenshot_name
            )
        )

    def execute(self, locator: Locator, driver_manager: DriverManager) -> None:
        sleep(Setting.SLEEP_TIME)
        if Setting.SHOW_OPERATION:
            print("assert element {}".format(locator.value))
        driver_manager.assert_element(locator)
        driver_manager.get_screenshot_as_png()

class ExecuteScript(LocatableOperation):
    def __init__(self, raw_string: str, target: str, once: bool):
        LocatableOperation.__init__(self, raw_string, "log in", once)
        self.__script = target

    @property
    def operation_type(self) -> OperationType:
        return OperationType.EXECUTE_SCRIPT

    def to_code(self, locator: Locator):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = "{}_{}_{}.png".format(
            self.operation_type.name.replace(" ", "_").lower(),
            timestamp,
            random.randint(1000, 9999)
        )
        return ( 
            "sleep(2)"
            + "\n    "
            + "driver.execute_script(\"\"\"{}\"\"\")".format(self.__script)
            + "\n    " 
            + "driver.save_screenshot('{}/{}')".format(Setting.SCREENSHOT_FOLDER, screenshot_name)
        )

    def execute(self, locator: Locator, driver_manager: DriverManager) -> None:
        sleep(Setting.SLEEP_TIME)
        if Setting.SHOW_OPERATION:
            print("execute script {}".format(self.__script))
        driver_manager.execute_script(self.__script)
        driver_manager.get_screenshot_as_png()


class AssertTitle(CodableOperation):
    def __init__(self, raw_string: str, value: str):
        Step.__init__(self, raw_string)
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value

    @property
    def operation_type(self) -> OperationType:
        return OperationType.ASSERT_TITLE

    def to_code(self) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = "{}_{}_{}.png".format(
            self.operation_type.name.replace(" ", "_").lower(),
            timestamp,
            random.randint(1000, 9999)
        )
        return ( 
            "assert '{}' == driver.title, 'expected title: \"{}\", but actual: \"{{}}\"'.format(driver.title)".format(
                self.value, self.value
            )
            + "\n    " 
            + "driver.save_screenshot('{}/{}')".format(Setting.SCREENSHOT_FOLDER, screenshot_name)
        )


class AssertString(CodableOperation):
    def __init__(self, raw_string: str, value: str):
        Step.__init__(self, raw_string)
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value

    @property
    def operation_type(self) -> OperationType:
        return OperationType.ASSERT_STRING

    def to_code(self) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = "{}_{}_{}.png".format(
            self.operation_type.name.replace(" ", "_").lower(),
            timestamp,
            random.randint(1000, 9999)
        )
        return ( 
            "assert '{}' in driver.page_source, 'string \"{}\" is not exist'".format(
                self.value, self.value
            )
            + "\n    " 
            + "driver.save_screenshot('{}/{}')".format(Setting.SCREENSHOT_FOLDER, screenshot_name)
        )


class PageTransition(Step):
    def __init__(self, raw_string):
        Step.__init__(self, raw_string)

    @property
    def operation_type(self) -> OperationType:
        return OperationType.PAGE_TRANSITION
