import pytest
from transstellar.framework import BaseUITest, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Breadcrumb as V4Breadcrumb
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v5 import Breadcrumb as V5Breadcrumb
from transstellar_antd.v5 import Page as V5Page

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "breadcrumb_class": V4Breadcrumb,
        "url": "https://4x.ant.design/components/breadcrumb",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "breadcrumb_class": V5Breadcrumb,
        "url": "https://ant.design/components/breadcrumb",
    },
)


@handle_ui_error()
class TestBreadcrumb(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    breadcrumb_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, breadcrumb_class, url):
        self.prepare(page_class, breadcrumb_class, url)

    def prepare(self, page_class, breadcrumb_class, url):
        self.app.driver.get(url)

        self.breadcrumb_class = breadcrumb_class
        self.page = page_class(self.app)
        self.page.sleep(3)

    def test(self):
        breadcrumb = self.page.find_element(self.breadcrumb_class)

        assert breadcrumb is not None
