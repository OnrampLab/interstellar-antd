import pytest
from transstellar.framework import BaseUITest, Element, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd import Anchor
from transstellar_antd.v4 import Button as V4Button
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v4 import Popover as V4Popover
from transstellar_antd.v5 import Button as V5Button
from transstellar_antd.v5 import Page as V5Page
from transstellar_antd.v5 import Popover as V5Popover

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "button_class": V4Button,
        "popover_class": V4Popover,
        "url": "https://4x.ant.design/components/popover",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "button_class": V5Button,
        "popover_class": V5Popover,
        "url": "https://ant.design/components/popover",
    },
)


@handle_ui_error()
class TestPopover(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    button_class = None
    popover_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, button_class, popover_class, url):
        self.prepare(page_class, button_class, popover_class, url)

    def prepare(self, page_class, button_class, popover_class, url):
        self.app.driver.get(url)

        self.button_class = button_class
        self.popover_class = popover_class
        self.page = page_class(self.app)
        self.page.sleep(5)

    def test_click_popover(self):
        button = self.page.find_element_by_label(self.button_class, "Click me")
        button.click()

        self.page.sleep(3)

        popover = self.page.find_element(self.popover_class)

        assert popover.is_opened()
