import pytest
from transstellar.framework import BaseUITest, Element, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Form as V4Form
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v5 import Form as V5Form
from transstellar_antd.v5 import Page as V5Page

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "form_class": V4Form,
        "url": "https://4x.ant.design/components/form",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "form_class": V5Form,
        "url": "https://ant.design/components/form",
    },
)


class CodeBlock(Element):
    XPATH_CURRENT = '//section[contains(@id, "form-demo-disabled")]'


@handle_ui_error()
class TestForm(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    form_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, form_class, url):
        self.prepare(page_class, form_class, url)

    def prepare(self, page_class, form_class, url):
        self.app.driver.get(url)

        self.form_class = form_class
        self.page = page_class(self.app)
        self.page.sleep(5)

    def test_form(self):
        form = self.page.find_element(self.form_class)

        form.form(False)

    def test_enabled(self):
        code_block = self.page.find_element(CodeBlock)
        self.form = code_block.find_element(self.form_class)
        self.form.scroll_to_view()
        self.form.sleep(3)

        assert not self.form.is_enabled()
