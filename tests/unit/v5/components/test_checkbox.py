import pytest
from transstellar.framework import BaseUITest, handle_ui_error

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


@handle_ui_error()
class TestCheckbox(BaseUITest):
    scenarios = [scenario1, scenario2]
    checkbox = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, checkbox_class, url):
        self.prepare(page_class, checkbox_class, url)

    def prepare(self, page_class, checkbox_class, url):
        self.app.driver.get(url)

        page = page_class(self.app)
        page.sleep(3)

        self.checkbox = page.find_global_element(checkbox_class)

    def test_constructor(self):
        assert self.checkbox is not None

    def test_check(self):
        self.checkbox.check(True)
