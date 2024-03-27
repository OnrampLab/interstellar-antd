from transstellar.framework import Element


class Input(Element):
    XPATH_CURRENT = '//input[contains(@class, "ant-input")]'

    def input(self, value: str):
        self.logger.info(f"input to value: {value}")

        self.get_current_dom_element().send_keys(value)
