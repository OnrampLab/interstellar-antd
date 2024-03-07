from urllib.parse import urlparse

from interstellar.framework import Element


class Button(Element):
    XPATH_CURRENT = '//button[contains(@class, "ant-btn")]'

    def get_button_xpath(self, label):
        return f'//button[contains(@class, "ant-btn") and span/text()="{label}"]'

    def click(self):
        self.dom_element.click()
