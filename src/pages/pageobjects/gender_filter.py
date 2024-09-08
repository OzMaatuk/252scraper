from src.pages.xpaths import *
from src.patterns.facade import SeleniumFacade
import logging

class GenderFilter:
    """Represents the gender filter element."""

    def __init__(self, selenium_facade: SeleniumFacade, container_locator: str):
        """
        Initializes the GenderFilter.

        Args:
            selenium_facade (SeleniumFacade): The SeleniumFacade instance for interacting with the browser.
            container_locator (str): The XPath locator for the container element of the gender filter.
        """
        self.selenium_facade = selenium_facade
        self.container_locator = container_locator

    def select_gender(self, gender: str):
        """
        Selects the specified gender filter.

        Args:
            gender (str): The gender to select (e.g., 'female', 'male').
        """
        try:
            gender_checkbox_locator = f"{self.container_locator}//input[@type='checkbox' and @value='{gender}']"
            self.selenium_facade.click_element(gender_checkbox_locator)
            logging.info(f"Selected gender: {gender}")
        except Exception as e:
            logging.error(f"Error selecting gender '{gender}': {e}")
            raise