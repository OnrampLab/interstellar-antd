import pytest
from transstellar.framework import BaseUITest, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v4 import Table as V4Table
from transstellar_antd.v5 import Page as V5Page
from transstellar_antd.v5 import Table as V5Table

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "table_class": V4Table,
        "url": "https://4x.ant.design/components/table",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "table_class": V5Table,
        "url": "https://ant.design/components/table",
    },
)


@handle_ui_error()
class TestTable(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    table = None
    table_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, table_class, url):
        self.prepare(page_class, table_class, url)

    def prepare(self, page_class, table_class, url):
        self.app.driver.get(url)

        self.table_class = table_class
        self.page = page_class(self.app)
        self.page.sleep(3)

        self.table = self.page.find_element(self.table_class)
        self.table.scroll_to_view()

    def test_find_row(self):
        row = self.table.find_row("Age", 42)

        assert row is not None

    def test_get_row(self):
        row = self.table.get_row(0)

        assert row is not None
