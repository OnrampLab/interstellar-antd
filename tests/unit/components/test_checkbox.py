import pytest
from transstellar.framework import BaseUITest, Element, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Checkbox as V4Checkbox
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v5 import Checkbox as V5Checkbox
from transstellar_antd.v5 import Page as V5Page

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "checkbox_class": V4Checkbox,
        "url": "https://4x.ant.design/components/checkbox",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "checkbox_class": V5Checkbox,
        "url": "https://ant.design/components/checkbox",
    },
)


class CodeBlock(Element):
    XPATH_CURRENT = '//section[contains(@id, "components-checkbox-demo-disabled")]'


@handle_ui_error()
class TestCheckbox(BaseUITest):
    scenarios = [scenario1, scenario2]
    checkbox = None
    checkbox_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, checkbox_class, url):
        self.prepare(page_class, checkbox_class, url)

    def prepare(self, page_class, checkbox_class, url):
        self.app.driver.get(url)

        self.page = page_class(self.app)
        self.page.sleep(5)

        self.checkbox_class = checkbox_class
        self.checkbox = self.page.find_global_element(checkbox_class)

    def test_constructor(self):
        assert self.checkbox is not None

    def test_check(self):
        self.checkbox.check(True)

    def test_enabled(self):
        code_block = self.page.find_element(CodeBlock)
        self.checkbox = code_block.find_element(self.checkbox_class)
        self.checkbox.scroll_to_view()
        self.checkbox.sleep(3)

        assert not self.checkbox.is_enabled()
