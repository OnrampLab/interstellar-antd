from datetime import date

import pytest
from transstellar.framework import BaseUITest, Element, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import DatePicker as V4DatePicker
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v5 import DatePicker as V5DatePicker
from transstellar_antd.v5 import Page as V5Page

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "date_picker_class": V4DatePicker,
        "url": "https://4x.ant.design/components/date-picker",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "date_picker_class": V5DatePicker,
        "url": "https://ant.design/components/date-picker",
    },
)


class BasicPickerBlock(Element):
    XPATH_CURRENT = '//section[contains(@id, "components-date-picker-demo-basic")]'


class RangePickerBlock(Element):
    XPATH_CURRENT = (
        '//section[contains(@id, "components-date-picker-demo-range-picker")]'
    )


@handle_ui_error()
class TestDatePicker(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    date_picker_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, date_picker_class, url):
        self.prepare(page_class, date_picker_class, url)

    def prepare(self, page_class, date_picker_class, url):
        self.app.driver.get(url)

        self.date_picker_class = date_picker_class
        self.page = page_class(self.app)

    def test_pick_single_date(self):
        code_block = self.page.find_element(BasicPickerBlock)

        date_picker = code_block.find_element(self.date_picker_class)
        from_date = date(2024, 5, 17)

        date_picker.pick_date(from_date)

        assert date_picker.get_basic_date_value() == "2024-05-17"

    def test_pick_date_range_for_date_only(self):
        code_block = self.page.find_element(RangePickerBlock)
        date_picker = code_block.find_element(self.date_picker_class)

        from_date = date(2024, 5, 17)
        to_date = date(2024, 5, 24)

        date_picker.pick_date_range(from_date, to_date)

        assert date_picker.get_date_range_values() == ["2024-05-17", "2024-05-24"]

    def test_pick_date_range_with_time(self):
        code_block = self.page.find_element(RangePickerBlock)
        date_pickers = code_block.find_elements(self.date_picker_class)
        date_picker = date_pickers[1]

        from_date = date(2024, 5, 17)
        to_date = date(2024, 5, 24)

        date_picker.pick_date_range(from_date, to_date, True)

        assert date_picker.get_date_range_values() == [
            "2024-05-17 00:00:00",
            "2024-05-24 00:00:00",
        ]
