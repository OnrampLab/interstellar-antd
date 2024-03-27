from transstellar.framework import Element


class Button(Element):
    XPATH_CURRENT = '//button[contains(@class, "ant-btn")]'

    def click(self):
        self.dom_element.click()
