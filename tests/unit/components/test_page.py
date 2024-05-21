import pytest
from transstellar.framework import BaseUITest, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Button as V4Button
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v5 import Button as V5Button
from transstellar_antd.v5 import Page as V5Page

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "button_class": V4Button,
        "url": "https://4x.ant.design/components/message",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "button_class": V5Button,
        "url": "https://ant.design/components/message",
    },
)


@handle_ui_error()
class TestPage(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    button_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, button_class, url):
        self.prepare(page_class, button_class, url)

    def prepare(self, page_class, button_class, url):
        self.button_class = button_class
        self.app.driver.get(url)

        self.page = page_class(self.app)
        self.page.sleep(5)

    def test_get_ant_message(self):
        button = self.page.find_element_by_label(
            self.button_class, "Display normal message"
        )
        button.click()

        message_content = self.page.get_ant_message()

        assert message_content is not None
