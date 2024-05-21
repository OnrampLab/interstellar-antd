import pytest
from transstellar.framework import BaseUITest, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v4 import Spin as V4Spin
from transstellar_antd.v5 import Page as V5Page
from transstellar_antd.v5 import Spin as V5Spin

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "spin_class": V4Spin,
        "url": "https://4x.ant.design/components/spin",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "spin_class": V5Spin,
        "url": "https://ant.design/components/spin",
    },
)


@handle_ui_error()
class TestSpin(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    spin_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, spin_class, url):
        self.prepare(page_class, spin_class, url)

    def prepare(self, page_class, spin_class, url):
        self.app.driver.get(url)

        self.spin_class = spin_class
        self.page = page_class(self.app)
        self.page.sleep(3)

    def test(self):
        spin = self.page.find_element(self.spin_class)

        assert spin is not None
