import pytest
from transstellar.framework import BaseUITest, Element, handle_ui_error

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


class V4PrefixAndSuffixCodeBlock(Element):
    XPATH_CURRENT = '//section[contains(@id, "components-input-demo-presuffix")]'


class V5PrefixAndSuffixCodeBlock(Element):
    XPATH_CURRENT = '//section[contains(@id, "input-demo-presuffix")]'


@handle_ui_error()
class TestInput(BaseUITest):
    scenarios = [scenario1, scenario2]
    input_class = None
    input = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, request, page_class, input_class, url):
        self.scenario_id = request.node.name.split("[")[1].split("]")[0]
        self.prepare(page_class, input_class, url)

    def prepare(self, page_class, input_class, url):
        self.app.driver.get(url)

        self.page = page_class(self.app)
        self.input_class = input_class
        self.input = self.page.find_global_element(input_class)

    def test_constructor(self):
        assert self.input is not None

    def test_input(self):
        self.input.input("ABC")
        self.input.input("DEF")

    def test_append(self):
        self.input.append("ABC")
        self.input.append("DEF")

        new_text = self.input.get_value()

        assert new_text == "ABCDEF"

    def test_enabled(self):
        if self.scenario_id == "v4":
            code_block = self.page.find_element(V4PrefixAndSuffixCodeBlock)
        else:
            code_block = self.page.find_element(V5PrefixAndSuffixCodeBlock)
        inputs = code_block.find_elements(self.input_class)
        self.input = inputs[2]
        self.input.scroll_to_view()
        self.input.sleep(3)

        assert not self.input.is_enabled()
