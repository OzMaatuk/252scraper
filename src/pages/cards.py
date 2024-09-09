import logging
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.patterns.cards_strategy import CardCollectionStrategy
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.xpaths import *
from src.pages.base import BasePage
from src.patterns.facade import SeleniumFacade
from src.pages.pageobjects.age_filter import AgeFilter
from src.pages.pageobjects.gender_filter import GenderFilter

class CardsPage(BasePage):
    def __init__(self, driver: WebDriver, 
                 logger: logging.Logger, 
                 selenium_facade: SeleniumFacade, 
                 card_collection_strategy: CardCollectionStrategy):
        """
        Initializes the CardsPage.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.
            logger (logging.Logger): The logger for output messages.
            selenium_facade (SeleniumFacade): The SeleniumFacade instance for interacting with the browser.
            card_collection_strategy (CardCollectionStrategy): The strategy for handling card collections.
        """
        super().__init__(driver, logger, selenium_facade)
        self.gender_filter = GenderFilter(selenium_facade, GENDER_CHECKBOX_XPATH)
        self.age_range_slider = AgeFilter(selenium_facade, AGE_SLIDER_XPATH)
        self.card_collection_strategy = card_collection_strategy

    def load_cards(self, url: str):
        """
        Loads the cards page and handles the initial popup.

        Args:
            url (str): The URL of the cards page.
        """
        try:
            self.load(url) 
            self.click_element(POPUP_BUTTON)
            self.logger.info("Close popup.")
        except Exception as e:
            self.logger.error(f"Error loading cards page: {e}")
            raise

    def wait_for_page_load(self, url: str = ""):
        """
        Waits for the cards page to load completely.

        Args:
            url (str, optional): The URL of the page to wait for. Defaults to "".
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.url_contains(url))
            self.logger.info("Waiting for cards container to load...")
            self.find_element(CARDS_CONTAINER_XPATH)
            self.logger.info("Cards container loaded.")
        except Exception as e:
            self.logger.error(f"Error waiting for page load: {e}")
            raise

    def apply_filters(self):
        """
        Applies the gender and age range filters.
        """
        try:
            self.logger.info("Setting filters...")
            self.gender_filter.select_gender("female")
            self.age_range_slider.set_age_range(23, 24) #TODO: make configurable
            self.logger.info("Filters applied.")
        except Exception as e:
            self.logger.error(f"Error setting filters: {e}")
            raise
        time.sleep(10)

    def process_cards(self, message: str):
        """
        Processes visible cards on the page using the selected strategy.
        """
        try:
            cards = self.card_collection_strategy.collect_cards(self.driver)
            self.card_collection_strategy.iterate_through_cards(self.driver, cards, self.card_collection_strategy.process_card, message)
        except Exception as e:
            self.logger.error(f"Error processing cards: {e}")
            raise