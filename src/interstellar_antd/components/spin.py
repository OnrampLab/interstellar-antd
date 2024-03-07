from urllib.parse import urlparse

from interstellar.framework import Element


class Spin(Element):
    XPATH_CURRENT = '//div[contains(@class, "ant-spin ")]'
