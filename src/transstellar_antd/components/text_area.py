from urllib.parse import urlparse

from .input import Input


class TextArea(Input):
    XPATH_CURRENT = '//textarea[contains(@class, "ant-input")]'
