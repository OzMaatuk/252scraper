from abc import ABC, abstractmethod

class CardCollectionStrategy(ABC):
    """Base class for card collection strategies."""

    def __init__(self, selenium_facade, logger):
        self.selenium_facade = selenium_facade
        self.logger = logger

    @abstractmethod
    def collect_cards(self, driver):
        """Collects cards from the page.

        Args:
            driver (webdriver): The Selenium WebDriver instance.

        Returns:
            list: A list of card WebElements.
        """
        pass 

# from .card_collection_strategy import CardCollectionStrategy
import time
import logging
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.xpaths import *
from src.pages.pageobjects.card import Card
from src.patterns.facade import SeleniumFacade
from src.patterns.cards_strategy import CardCollectionStrategy

class StandardCardCollection(CardCollectionStrategy):
    """Collects cards by scrolling and finding them using a specific XPath."""

    def __init__(self, selenium_facade: SeleniumFacade, logger: logging.Logger):
        """
        Initializes the StandardCardCollection strategy.

        Args:
            selenium_facade (SeleniumFacade): The SeleniumFacade instance for interacting with the browser.
            logger (logging.Logger): The logger for output messages.
        """
        self.selenium_facade = selenium_facade
        self.logger = logger

    def collect_cards(self, driver: WebDriver):
        """Collects all visible cards on the page after scrolling."""
        try:
            self.scroll_to_load_all_cards(driver)
            cards = self.selenium_facade.find_elements(CARDS_XPATH)
            self.logger.info(f"Found {len(cards)} cards.")
            time.sleep(30)
            return cards

        except Exception as e:
            raise Exception(f"Error collecting cards: {e}")

    def scroll_to_load_all_cards(self, driver: WebDriver):
        """Scrolls down the page until all cards are loaded."""
        self.logger.info("Scrolling to load all cards...")
        cards = []
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)  # Adjust wait time if needed
            new_cards = self.selenium_facade.find_elements(CARDS_XPATH)
            if len(new_cards) == len(cards):
                break
            cards = new_cards
        self.logger.info("All cards loaded.")

    def iterate_through_cards(self, driver: WebDriver, cards: list):
        """Iterates through the collected cards and applies the process_card method."""
        for index, card_element in enumerate(cards):
            card = Card(self.selenium_facade, card_element)
            try:
                card_name = card.get_name()
                self.logger.info(f"Processing card {index + 1}: {card_name}")

                # Apply the process_card method 
                self.process_card(driver, card) 

            except Exception as e:
                self.logger.error(f"Error processing card: {e}") 

    def process_card(self, driver: WebDriver, card: Card):
        """Clicks the "View" button and performs actions in the new tab."""
        card.click_view_button()
        self.logger.info(f"Clicked 'View' button on card: {card.get_name()}")

        driver.switch_to.window(driver.window_handles[-1])

        # --- Your actions in the new tab ---
        # ... (your code to extract data or interact with elements on the new page) ...

        driver.close()
        driver.switch_to.window(driver.window_handles[0])