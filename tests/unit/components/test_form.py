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


class V4RegisterBlock(Element):
    XPATH_CURRENT = '//section[contains(@id, "components-form-demo-register")]'


class V4DisabledBlock(Element):
    XPATH_CURRENT = '//section[@id="components-form-demo-disabled"]'


class V5RegisterBlock(Element):
    XPATH_CURRENT = '//section[contains(@id, "form-demo-register")]'


class V5DisabledBlock(Element):
    XPATH_CURRENT = '//section[@id="form-demo-disabled"]'


@handle_ui_error()
class TestForm(BaseUITest):
    scenarios = [scenario1, scenario2]
    page = None
    form_class = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, request, page_class, form_class, checkbox_class, url):
        self.prepare(page_class, form_class, checkbox_class, url)
        current_scenario_name = request.node.name
        self.scenario_id = current_scenario_name.split("[")[1].split("]")[0]

        if self.scenario_id == "v4":
            code_block = self.page.find_element(V4RegisterBlock)
        else:
            code_block = self.page.find_element(V5RegisterBlock)

        if self.scenario_id == "v4":
            self.disabled_code_block = self.page.find_element(V4DisabledBlock)
        else:
            self.disabled_code_block = self.page.find_element(V5DisabledBlock)

        self.form = code_block.find_element(self.form_class)
        self.form.scroll_to_view()
        self.sleep(5)

    def prepare(self, page_class, form_class, checkbox_class, url):
        self.app.driver.get(url)

        self.form_class = form_class
        self.checkbox_class = checkbox_class
        self.page = page_class(self.app)
        self.page.sleep(5)

    def test_input(self):
        self.form.input("E-mail", "test")

    def test_text_area_input(self):
        self.form.text_area_input("Intro", "test")
        self.screenshot("textarea.png")

    def test_select(self):
        self.form.select("Gender", "Male")

    def direct_check(self):
        self.form.direct_check("I have read the", True)

    def test_check(self):
        self.form = self.disabled_code_block.find_element(self.form_class)
        self.form.scroll_to_view()
        self.sleep(5)

        checkbox = self.disabled_code_block.find_element_by_label(
            self.checkbox_class, "Form disabled"
        )
        checkbox.scroll_to_view()
        checkbox.click()
        self.sleep(1)

        self.form.check("Checkbox", True)

    def test_switch(self):
        self.form = self.disabled_code_block.find_element(self.form_class)
        self.form.scroll_to_view()
        self.sleep(5)

        checkbox = self.disabled_code_block.find_element_by_label(
            self.checkbox_class, "Form disabled"
        )
        checkbox.scroll_to_view()
        checkbox.click()
        self.sleep(1)

        self.form.switch("Switch", True)

    def test_find_element_by_form_item_label(self):
        self.form = self.disabled_code_block.find_element(self.form_class)
        self.form.scroll_to_view()
        self.sleep(5)

        checkbox = self.form.find_element_by_form_item_label(
            self.checkbox_class, "Checkbox"
        )

        assert checkbox is not None

    def test_is_form_item_present(self):
        self.form = self.disabled_code_block.find_element(self.form_class)
        self.form.scroll_to_view()
        self.sleep(5)

        assert self.form.is_form_item_present("TreeSelect")
        assert not self.form.is_form_item_present("No Exist")
