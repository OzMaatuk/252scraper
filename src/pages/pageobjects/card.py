from src.pages.xpaths import *
from src.patterns.facade import SeleniumFacade
from selenium.webdriver.remote.webelement import WebElement
import logging

class Card:
    """Represents an individual card on the page."""

    def __init__(self, selenium_facade: SeleniumFacade, card_element: WebElement):
        """
        Initializes the Card.

        Args:
            selenium_facade (SeleniumFacade): The SeleniumFacade instance for interacting with the browser.
            card_element (WebElement): The WebElement representing the card.
        """
        self.selenium_facade = selenium_facade
        self.card_element = card_element

    def get_name(self) -> str:
        """
        Gets the name from the card.

        Returns:
            str: The name of the card.
        """
        try:
            name = self.selenium_facade.get_element_text(CARD_NAME, parent_element=self.card_element)
            logging.info(f"Card name retrieved: {name}")
            return name
        except Exception as e:
            logging.error(f"Error retrieving card name: {e}")
            raise

    def click_view_button(self):
        """
        Clicks the 'View' button on the card.
        """
        try:
            view_button = self.selenium_facade.find_element(CARD_BUTTON, parent_element=self.card_element)
            view_button.click()
            logging.info("Clicked 'View' button on card.")
        except Exception as e:
            logging.error(f"Error clicking 'View' button: {e}")
            raise