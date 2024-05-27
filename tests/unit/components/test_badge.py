import pytest
from transstellar.framework import BaseUITest, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Badge as V4Badge
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v5 import Badge as V5Badge
from transstellar_antd.v5 import Page as V5Page

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "badge_class": V4Badge,
        "url": "https://4x.ant.design/components/badge",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "badge_class": V5Badge,
        "url": "https://ant.design/components/badge",
    },
)


@handle_ui_error()
class TestBadge(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    badge = None
    badge_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, badge_class, url):
        self.badge_class = badge_class
        self.prepare(page_class, url)

    def prepare(self, page_class, url):
        self.app.driver.get(url)
        self.page = page_class(self.app)
        self.page.sleep(3)

        self.badge = self.page.find_global_element(self.badge_class)

    def test_constructor(self):
        assert self.badge is not None

    def test_click(self):
        self.badge.click()
