import pytest
from transstellar.framework import BaseUITest, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Button as V4Button
from transstellar_antd.v4 import Modal as V4Modal
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v5 import Button as V5Button
from transstellar_antd.v5 import Modal as V5Modal
from transstellar_antd.v5 import Page as V5Page

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "button_class": V4Button,
        "modal_class": V4Modal,
        "url": "https://4x.ant.design/components/modal",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "button_class": V5Button,
        "modal_class": V5Modal,
        "url": "https://ant.design/components/modal",
    },
)


@handle_ui_error()
class TestModal(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    modal = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, button_class, modal_class, url):
        self.prepare(page_class, button_class, modal_class, url)

    def prepare(self, page_class, button_class, modal_class, url):
        self.app.driver.get(url)
        self.app.driver.set_window_size(1024, 768)

        self.page = page_class(self.app)

        # V5 page will jump to #footerRenderParams after a while.
        # So we need to wait for it to avoid inconsistency.
        self.page.sleep(15)

        button = self.page.find_element_by_label(button_class, "Open Modal")
        button.scroll_to_view()
        button.click()
        self.page.sleep(3)

        self.modal = self.page.find_element_by_label(modal_class, "Basic Modal")

    def test_close(self):
        self.modal.close()
