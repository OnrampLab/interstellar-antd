from urllib.parse import urlparse

from interstellar.framework import Element

from .checkbox import Checkbox
from .form_item import FormItem
from .input import Input
from .select import Select
from .switch import Switch
from .text_area import TextArea


class Form(Element):
    XPATH_CURRENT = "//form"

    def input(self, label: str, value: str):
        input_element: Input = self.__find_element_by_label(label, Input)
        input_element.input(value)

    def text_area_input(self, label: str, value: str):
        text_area_element: TextArea = self.__find_element_by_label(label, TextArea)
        text_area_element.input(value)

    def select(self, label: str, value: str):
        select_element: Select = self.__find_element_by_label(label, Select)
        select_element.select(value)

    def switch(self, label: str, value: str):
        switch_element: Switch = self.__find_element_by_label(label, Switch)
        switch_element.switch(value)

    def check(self, label: str, value: str):
        checkbox_element: Checkbox = self.__find_element_by_label(label, Checkbox)
        checkbox_element.check(value)

    def __find_element_by_label(self, label: str, element_class):
        form_item: FormItem = self.find_element_by_label(FormItem, label)
        element: element_class = form_item.find_form_control(element_class)

        return element
