import pytest
from transstellar.framework import BaseUITest, Element, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v4 import RadioGroup as V4RadioGroup
from transstellar_antd.v5 import Page as V5Page
from transstellar_antd.v5 import RadioGroup as V5RadioGroup

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "radio_group_class": V4RadioGroup,
        "url": "https://4x.ant.design/components/radio",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "radio_group_class": V5RadioGroup,
        "url": "https://ant.design/components/radio",
    },
)


class CodeBlock(Element):
    XPATH_CURRENT = '//section[@id="components-radio-demo-radiobutton"]'


@handle_ui_error()
class TestRadioGroup(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    radio_group_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, radio_group_class, url):
        self.prepare(page_class, radio_group_class, url)

    def prepare(self, page_class, radio_group_class, url):
        self.app.driver.get(url)

        self.radio_group_class = radio_group_class
        self.page = page_class(self.app)
        self.page.sleep(5)

        code_block = self.page.find_element(CodeBlock)
        self.radio_groups = code_block.find_elements(self.radio_group_class)

    def test_select(self):
        self.radio_group = self.radio_groups[0]
        self.radio_group.scroll_to_view()
        self.radio_group.sleep(3)

        self.radio_group.select("Shanghai")
        self.radio_group.sleep(3)

        assert self.radio_group.get_current_item_text() == "Shanghai"

    def test_enabled(self):
        self.radio_group = self.radio_groups[2]
        self.radio_group.scroll_to_view()
        self.radio_group.sleep(3)

        assert not self.radio_group.is_enabled()
