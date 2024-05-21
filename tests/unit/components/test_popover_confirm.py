import pytest
from transstellar.framework import BaseUITest, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd import Anchor
from transstellar_antd.v4 import Button as V4Button
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v4 import PopoverConfirm as V4PopoverConfirm
from transstellar_antd.v5 import Button as V5Button
from transstellar_antd.v5 import Page as V5Page
from transstellar_antd.v5 import PopoverConfirm as V5PopoverConfirm

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "button_class": V4Button,
        "popconfirm_class": V4PopoverConfirm,
        "url": "https://4x.ant.design/components/popconfirm",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "button_class": V5Button,
        "popconfirm_class": V5PopoverConfirm,
        "url": "https://ant.design/components/popconfirm",
    },
)


@handle_ui_error()
class TestPopoverConfirm(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    button_class = None
    popconfirm_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, button_class, popconfirm_class, url):
        self.prepare(page_class, button_class, popconfirm_class, url)

    def prepare(self, page_class, button_class, popconfirm_class, url):
        self.app.driver.get(url)

        self.button_class = button_class
        self.popconfirm_class = popconfirm_class
        self.page = page_class(self.app)
        self.page.sleep(5)

    def test_click(self):
        if self.popconfirm_class == V4PopoverConfirm:
            button = self.page.find_element_by_label(Anchor, "Delete")
        else:
            button = self.page.find_element_by_label(self.button_class, "Delete")

        button.click()

        self.page.sleep(3)

        popover_confirm = self.page.find_global_element(self.popconfirm_class)

        popover_confirm.click("No")
