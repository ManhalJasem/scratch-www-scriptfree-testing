from enum import Enum


class OperationType(Enum):
    ENTER = "enter"
    SELECT = "select"
    CLICK = "click"
    CLICK_DIV = "click div"
    OPEN = "open"
    PAGE_TRANSITION = "page_transition"
    ASSERT_ELEMENT = "assert element"
    ASSERT_STRING = "assert string"
    ASSERT_TITLE = "assert title"
    EXECUTE_SCRIPT = "execute script"
