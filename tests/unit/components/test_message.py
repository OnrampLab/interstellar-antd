import pytest
from transstellar.framework import BaseUITest, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Button as V4Button
from transstellar_antd.v4 import Message as V4Message
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v5 import Button as V5Button
from transstellar_antd.v5 import Message as V5Message
from transstellar_antd.v5 import Page as V5Page

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "message_class": V4Message,
        "button_class": V4Button,
        "url": "https://4x.ant.design/components/message",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "message_class": V5Message,
        "button_class": V5Button,
        "url": "https://ant.design/components/message",
    },
)


@handle_ui_error()
class TestMessage(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    message = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, message_class, button_class, url):
        self.prepare(page_class, message_class, button_class, url)

    def prepare(self, page_class, message_class, button_class, url):
        self.app.driver.get(url)

        self.page = page_class(self.app)
        self.page.sleep(6)

        button = self.page.find_element_by_label(button_class, "Display normal message")
        button.click()

        self.message = self.page.find_global_element(message_class)

    def test_get_content(self):

        content = self.message.get_content()

        assert content is not None
