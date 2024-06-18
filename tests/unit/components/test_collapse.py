import pytest
from transstellar.framework import BaseUITest, Element, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Collapse as V4Collapse
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v5 import Collapse as V5Collapse
from transstellar_antd.v5 import Page as V5Page

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "collapse_class": V4Collapse,
        "url": "https://4x.ant.design/components/collapse",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "collapse_class": V5Collapse,
        "url": "https://ant.design/components/collapse",
    },
)


class CodeBlock(Element):
    XPATH_CURRENT = '//section[@id="components-collapse-demo-basic"]'


@handle_ui_error()
class TestCollapse(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    collapse_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, collapse_class, url):
        self.prepare(page_class, collapse_class, url)

    def prepare(self, page_class, collapse_class, url):
        self.app.driver.get(url)

        self.collapse_class = collapse_class
        self.page = page_class(self.app)
        self.page.sleep(3)

    def test_collapse(self):
        code_block = self.page.find_element(CodeBlock)
        collapse = code_block.find_element(self.collapse_class)
        items = collapse.get_items()
        item = items[0]

        assert len(items) == 3

        assert "This is panel header 1" in item.get_header_text()
        assert "A dog is a type of domesticated animal" in item.get_content_text()
        assert item.is_expanded()

        item.scroll_to_view()
        item.sleep(3)

        item.click()

        assert not item.is_expanded()

    def test_find_item(self):
        code_block = self.page.find_element(CodeBlock)
        collapse = code_block.find_element(self.collapse_class)
        item = collapse.find_item("This is panel header 1")

        assert "This is panel header 1" in item.get_header_text()
        assert "A dog is a type of domesticated animal" in item.get_content_text()
        assert item.is_expanded()
