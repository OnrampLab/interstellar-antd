from urllib.parse import urlparse

from interstellar.framework import Element


class Message(Element):
    XPATH_CURRENT = '//div[@class="ant-message"]'

    def get_content(self):
        return self.find_dom_element_by_xpath(f"./div/div").text
