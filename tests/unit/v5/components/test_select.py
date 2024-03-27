import pytest
from transstellar.framework import BaseUITest, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v4 import Select as V4Select
from transstellar_antd.v5 import Page as V5Page
from transstellar_antd.v5 import Select as V5Select

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "select_class": V4Select,
        "url": "https://4x.ant.design/components/select",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "select_class": V5Select,
        "url": "https://ant.design/components/select",
    },
)


@handle_ui_error()
class TestSelect(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    select_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, select_class, url):
        self.prepare(page_class, select_class, url)

    def prepare(self, page_class, select_class, url):
        self.app.driver.get(url)

        self.select_class = select_class
        self.page = page_class(self.app)
        self.page.sleep(3)

    def test_select(self):
        select = self.page.find_element(self.select_class)

        select.select("Jack")
