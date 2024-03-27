import pytest
from transstellar.framework import BaseUITest, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Input as V4Input
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v5 import Input as V5Input
from transstellar_antd.v5 import Page as V5Page

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "input_class": V4Input,
        "url": "https://4x.ant.design/components/input",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "input_class": V5Input,
        "url": "https://ant.design/components/input",
    },
)


@handle_ui_error()
class TestInput(BaseUITest):
    scenarios = [scenario1, scenario2]
    input = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, input_class, url):
        self.prepare(page_class, input_class, url)

    def prepare(self, page_class, input_class, url):
        self.app.driver.get(url)

        page = page_class(self.app)
        self.input = page.find_global_element(input_class)

    def test_constructor(self):
        assert self.input is not None

    def test_input(self):
        self.input.input("ABC")
