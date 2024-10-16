import pytest
from transstellar.framework import BaseUITest, Element, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v5 import ColorPicker as V5ColorPicker
from transstellar_antd.v5 import Page as V5Page

pytest_generate_tests = pytest_generate_tests_helper

scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "color_picker_class": V5ColorPicker,
        "url": "https://ant.design/components/color-picker",
    },
)


class BasicUsageBlock(Element):
    XPATH_CURRENT = '//section[@id="color-picker-demo-base"]'


class DisabledBlock(Element):
    XPATH_CURRENT = '//section[@id="color-picker-demo-disabled"]'


@handle_ui_error()
class TestColorPicker(BaseUITest):
    scenarios = [scenario2]
    page = None
    color_picker_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, color_picker_class, url):
        self.prepare(page_class, color_picker_class, url)

    def prepare(self, page_class, color_picker_class, url):
        self.app.driver.get(url)

        self.color_picker_class = color_picker_class
        self.page = page_class(self.app)
        self.page.sleep(6)

    def test_pick_color_by_hex(self):
        code_block = self.page.find_element(BasicUsageBlock)

        color_picker = code_block.find_element(self.color_picker_class)

        color_picker.pick_color_by_hex("FFFFFF")

        assert color_picker.get_current_color() == "FFFFFF"

    def test_enabled(self):
        code_block = self.page.find_element(DisabledBlock)
        self.color_picker = code_block.find_element(self.color_picker_class)
        self.color_picker.scroll_to_view()
        self.color_picker.sleep(3)

        assert not self.color_picker.is_enabled()
