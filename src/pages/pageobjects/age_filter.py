from selenium.webdriver.common.keys import Keys
from src.pages.xpaths import *

class AgeFilter:
    """Represents the age range slider element."""
    def __init__(self, selenium_facade, slider_locator):
        self.selenium_facade = selenium_facade
        self.slider_locator = slider_locator

    def set_age_range(self, min_age, max_age):
        """Sets the age range on the slider."""
        min_input = self.selenium_facade.find_element(
            f"{self.slider_locator}//input[@class='jet-range__slider__input jet-range__slider__input--min']", timeout=20)
        max_input = self.selenium_facade.find_element(
            f"{self.slider_locator}//input[@class='jet-range__slider__input jet-range__slider__input--max']", timeout=20)

        self.selenium_facade.execute_script("arguments[0].value = {}; arguments[0].dispatchEvent(new Event('input'));".format(min_age), min_input)
        self.selenium_facade.execute_script("arguments[0].value = {}; arguments[0].dispatchEvent(new Event('input'));".format(max_age), max_input)

        slider_element = self.selenium_facade.find_element(self.slider_locator)
        slider_element.send_keys(Keys.ENTER)