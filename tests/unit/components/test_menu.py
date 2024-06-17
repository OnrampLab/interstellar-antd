import pytest
from transstellar.framework import BaseUITest, Element, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Menu as V4Menu
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v5 import Menu as V5Menu
from transstellar_antd.v5 import Page as V5Page

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "menu_class": V4Menu,
        "url": "https://4x.ant.design/components/menu",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "menu_class": V5Menu,
        "url": "https://ant.design/components/menu",
    },
)


class CodeSearchBlock(Element):
    XPATH_CURRENT = (
        '//section[@id="menu-demo-inline" or @id="components-menu-demo-inline"]'
    )


@handle_ui_error()
class TestMenu(BaseUITest):
    scenarios = [scenario1]
    page = None
    menu_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, menu_class, url):
        self.prepare(page_class, menu_class, url)

    def prepare(self, page_class, menu_class, url):
        self.app.driver.get(url)

        self.menu_class = menu_class
        self.page = page_class(self.app)
        self.page.sleep(3)

    def test_menu(self):
        code_block = self.page.find_element(CodeSearchBlock)
        menu = code_block.find_element(self.menu_class)
        menu.scroll_to_view()
        self.page.sleep(3)

        menu.select("Option 2")

        assert menu.get_current_item_title() == "Option 2"
