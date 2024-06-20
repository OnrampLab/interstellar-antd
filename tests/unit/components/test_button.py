import pytest
from transstellar.framework import BaseUITest, Element, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Button as V4Button
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v5 import Button as V5Button
from transstellar_antd.v5 import Page as V5Page

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "button_class": V4Button,
        "url": "https://4x.ant.design/components/button",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "button_class": V5Button,
        "url": "https://ant.design/components/button",
    },
)


class CodeBlock(Element):
    XPATH_CURRENT = '//section[contains(@id, "components-button-demo-disabled")]'


@handle_ui_error()
class TestButton(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    button = None
    button_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, button_class, url):
        self.button_class = button_class
        self.prepare(page_class, url)

    def prepare(self, page_class, url):
        self.app.driver.get(url)
        self.page = page_class(self.app)
        self.page.sleep(3)
        self.button = self.page.find_global_element(self.button_class)

    def test_constructor(self):
        assert self.button is not None

    def test_click(self):
        self.button.click()

    def test_enabled(self):
        code_block = self.page.find_element(CodeBlock)
        self.button = code_block.find_element_by_label(self.button_class, "disabled")
        self.button.scroll_to_view()
        self.button.sleep(3)

        assert not self.button.is_enabled()
