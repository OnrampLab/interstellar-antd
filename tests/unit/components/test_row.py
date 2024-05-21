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
class TestRow(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    row = None
    table_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, table_class, url):
        self.prepare(page_class, table_class, url)

    def prepare(self, page_class, table_class, url):
        self.app.driver.get(url)

        self.table_class = table_class
        self.page = page_class(self.app)
        self.page.sleep(3)

        table = self.page.find_element(self.table_class)
        table.scroll_to_view()

        self.row = table.get_row(0)

    def test_column_titles(self):
        assert self.row.column_titles is not None

    def test_get_cell_text(self):
        name = self.row.get_cell_text("Name")

        assert name == "John Brown"

    def test_get_cell_values(self):
        cells = self.row.get_cells()

        assert cells == {
            "Name": "John Brown",
            "Age": "32",
            "Address": "New York No. 1 Lake Park",
            "Tags": "NICEDEVELOPER",
            "Action": "Invite John Brown\nDelete",
        }

    def test_find_dom_element_in_cell_by_xpath(self):
        anchor = self.row.find_dom_element_in_cell_by_xpath("Name", "//a")

        assert anchor is not None
