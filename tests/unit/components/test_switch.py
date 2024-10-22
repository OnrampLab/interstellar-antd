import pytest
from transstellar.framework import BaseUITest, Element, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v4 import Switch as V4Switch
from transstellar_antd.v5 import Page as V5Page
from transstellar_antd.v5 import Switch as V5Switch

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "switch_class": V4Switch,
        "url": "https://4x.ant.design/components/switch",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "switch_class": V5Switch,
        "url": "https://ant.design/components/switch",
    },
)


class CodeBlock(Element):
    XPATH_CURRENT = '//section[contains(@id, "switch-demo-basic")]'


class DisabledCodeBlock(Element):
    XPATH_CURRENT = '//section[contains(@id, "switch-demo-disabled")]'


@handle_ui_error()
class TestSwitch(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    switch_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, switch_class, url):
        self.prepare(page_class, switch_class, url)

    def prepare(self, page_class, switch_class, url):
        self.app.driver.get(url)

        self.switch_class = switch_class
        self.page = page_class(self.app)
        self.page.sleep(7)

    def test_switch(self):
        code_block = self.page.find_element(CodeBlock)
        switch = code_block.find_element(self.switch_class)

        switch.switch(False)

    def test_enabled(self):
        code_block = self.page.find_element(DisabledCodeBlock)
        self.switch = code_block.find_element(self.switch_class)
        self.switch.scroll_to_view()
        self.switch.sleep(3)

        assert not self.switch.is_enabled()
