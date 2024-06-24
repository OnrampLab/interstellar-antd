import pytest
from transstellar.framework import BaseUITest, Element, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Checkbox as V4Checkbox
from transstellar_antd.v4 import Form as V4Form
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v5 import Checkbox as V5Checkbox
from transstellar_antd.v5 import Form as V5Form
from transstellar_antd.v5 import Page as V5Page

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "form_class": V4Form,
        "checkbox_class": V4Checkbox,
        "url": "https://4x.ant.design/components/form",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "form_class": V5Form,
        "checkbox_class": V5Checkbox,
        "url": "https://ant.design/components/form",
    },
)


class RegisterBlock(Element):
    XPATH_CURRENT = '//section[contains(@id, "components-form-demo-register")]'


class DisabledBlock(Element):
    XPATH_CURRENT = '//section[@id="components-form-demo-disabled"]'


@handle_ui_error()
class TestForm(BaseUITest):
    scenarios = [scenario2]
    page = None
    form_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, form_class, checkbox_class, url):
        self.prepare(page_class, form_class, checkbox_class, url)
        code_block = self.page.find_element(RegisterBlock)
        self.form = code_block.find_element(self.form_class)
        self.form.scroll_to_view()
        self.sleep(5)

    def prepare(self, page_class, form_class, checkbox_class, url):
        self.app.driver.get(url)

        self.form_class = form_class
        self.checkbox_class = checkbox_class
        self.page = page_class(self.app)
        self.page.sleep(5)

    def test_input1(self):
        self.form.input("E-mail", "test")

    def test_text_area_input(self):
        self.form.text_area_input("Intro", "test")
        self.screenshot("textarea.png")

    def test_select(self):
        self.form.select("Gender", "Male")

    def direct_check(self):
        self.form.direct_check("I have read the", True)

    def test_check(self):
        code_block = self.page.find_element(DisabledBlock)
        self.form = code_block.find_element(self.form_class)
        self.form.scroll_to_view()
        self.sleep(5)

        checkbox = code_block.find_element_by_label(
            self.checkbox_class, "Form disabled"
        )
        checkbox.scroll_to_view()
        checkbox.click()
        self.sleep(1)

        self.form.check("Checkbox", True)

    def test_switch(self):
        code_block = self.page.find_element(DisabledBlock)
        self.form = code_block.find_element(self.form_class)
        self.form.scroll_to_view()
        self.sleep(5)

        checkbox = code_block.find_element_by_label(
            self.checkbox_class, "Form disabled"
        )
        checkbox.scroll_to_view()
        checkbox.click()
        self.sleep(1)

        self.form.switch("Switch", True)

    def test_find_element_by_form_item_label(self):
        code_block = self.page.find_element(DisabledBlock)
        self.form = code_block.find_element(self.form_class)
        self.form.scroll_to_view()
        self.sleep(5)

        checkbox = self.form.find_element_by_form_item_label(
            self.checkbox_class, "Checkbox"
        )

        assert checkbox is not None
