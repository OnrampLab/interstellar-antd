import pytest
from transstellar.framework import BaseUITest, Element, handle_ui_error

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


class V4BasicTableCodeBlock(Element):
    XPATH_CURRENT = '//section[contains(@id, "components-table-demo-basic")]'


class V5BasicTableCodeBlock(Element):
    XPATH_CURRENT = '//section[contains(@id, "table-demo-basic")]'


@handle_ui_error()
class TestTable(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    table = None
    table_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, request, page_class, table_class, url):
        self.scenario_id = request.node.name.split("[")[1].split("]")[0]
        self.prepare(page_class, table_class, url)

    def prepare(self, page_class, table_class, url):
        self.app.driver.get(url)

        self.table_class = table_class
        self.page = page_class(self.app)
        self.page.sleep(3)

        if self.scenario_id == "v4":
            code_block = self.page.find_element(V4BasicTableCodeBlock)
        else:
            code_block = self.page.find_element(V5BasicTableCodeBlock)

        self.table = code_block.find_element(self.table_class)
        self.table.scroll_to_view()
        self.page.sleep(3)

    def test_find_row(self):
        row = self.table.find_row("Age", 42)

        assert row is not None

    def test_get_row(self):
        row = self.table.get_row(0)

        assert row is not None
