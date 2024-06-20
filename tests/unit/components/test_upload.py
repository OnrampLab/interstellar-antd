import pytest
from transstellar.framework import BaseUITest, Element, handle_ui_error

from tests.pytest_generate_tests_helper import pytest_generate_tests_helper
from transstellar_antd.v4 import Page as V4Page
from transstellar_antd.v4 import Upload as V4Upload
from transstellar_antd.v5 import Page as V5Page
from transstellar_antd.v5 import Upload as V5Upload

pytest_generate_tests = pytest_generate_tests_helper

scenario1 = (
    "v4",
    {
        "page_class": V4Page,
        "upload_class": V4Upload,
        "url": "https://4x.ant.design/components/upload",
    },
)
scenario2 = (
    "v5",
    {
        "page_class": V5Page,
        "upload_class": V5Upload,
        "url": "https://ant.design/components/upload",
    },
)


class AvatarBlock(Element):
    XPATH_CURRENT = '//section[contains(@id, "components-upload-demo-avatar")]'


@handle_ui_error()
class TestUpload(BaseUITest):
    scenarios = [scenario1, scenario2]
    upload_class = None
    upload = None

    @pytest.fixture(autouse=True)
    def setup_method_test(self, page_class, upload_class, url):
        self.prepare(page_class, upload_class, url)

    def prepare(self, page_class, upload_class, url):
        self.app.driver.get(url)

        self.page = page_class(self.app)
        self.upload_class = upload_class
        self.upload = self.page.find_global_element(upload_class)

    def test_constructor(self):
        assert self.upload is not None

    def test_enabled(self):
        code_block = self.page.find_element(AvatarBlock)
        self.upload = code_block.find_element(self.upload_class)
        self.upload.scroll_to_view()
        self.upload.sleep(3)

        assert self.upload.is_enabled()
