import pytest
from transstellar.framework import BaseUITest, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v4 import Tab as V4Tab
from transstellar_antd.v5 import Page as V5Page
from transstellar_antd.v5 import Tab as V5Tab

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "tab_class": V4Tab,
        "url": "https://4x.ant.design/components/tabs",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "tab_class": V5Tab,
        "url": "https://ant.design/components/tabs",
    },
)


@handle_ui_error()
class TestTab(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    tab_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, tab_class, url):
        self.prepare(page_class, tab_class, url)

    def prepare(self, page_class, tab_class, url):
        self.app.driver.get(url)

        self.tab_class = tab_class
        self.page = page_class(self.app)
        self.page.sleep(3)

    def test(self):
        tab = self.page.find_element(self.tab_class)

        assert tab is not None
