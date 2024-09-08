import logging
from selenium.webdriver.common.keys import Keys
from src.pages.xpaths import *
from src.patterns.facade import SeleniumFacade

class AgeFilter:
    """Represents the age range slider element."""

    def __init__(self, selenium_facade: SeleniumFacade, slider_locator: str):
        """
        Initializes the AgeFilter.

        Args:
            selenium_facade (SeleniumFacade): The SeleniumFacade instance for interacting with the browser.
            slider_locator (str): The XPath locator for the slider element.
        """
        self.selenium_facade = selenium_facade
        self.slider_locator = slider_locator

    def set_age_range(self, min_age: int, max_age: int):
        """
        Sets the age range on the slider.

        Args:
            min_age (int): The minimum age to set on the slider.
            max_age (int): The maximum age to set on the slider.
        """
        try:
            min_input = self.selenium_facade.find_element(
                f"{self.slider_locator}//input[@class='jet-range__slider__input jet-range__slider__input--min']", timeout=20)
            max_input = self.selenium_facade.find_element(
                f"{self.slider_locator}//input[@class='jet-range__slider__input jet-range__slider__input--max']", timeout=20)

            self.selenium_facade.execute_script("arguments[0].value = {}; arguments[0].dispatchEvent(new Event('input'));".format(min_age), min_input)
            self.selenium_facade.execute_script("arguments[0].value = {}; arguments[0].dispatchEvent(new Event('input'));".format(max_age), max_input)

            slider_element = self.selenium_facade.find_element(self.slider_locator)
            slider_element.send_keys(Keys.ENTER)
            logging.info(f"Set age range: {min_age}-{max_age}")
        except Exception as e:
            logging.error(f"Error setting age range: {e}")
            raise