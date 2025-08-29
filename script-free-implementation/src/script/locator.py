from enum import Enum


class LocatorType(Enum):
    ID = "ID"
    NAME = "NAME"
    LINK_TEXT = "PARTIAL_LINK_TEXT"
    XPATH = "XPATH"


class Locator:
    def __init__(self, locator_type: LocatorType, value):
        self.__locator_type = locator_type
        self.__value = value

    @property
    def locator_type(self):
        return self.__locator_type

    @property
    def value(self):
        return self.__value
