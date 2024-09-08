import time
from .base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.xpaths import *
from src.pages.pageobjects.gender_filter import GenderFilter
from src.pages.pageobjects.age_filter import AgeFilter
from src.patterns.cards_strategy import CardCollectionStrategy 

class CardsPage(BasePage):
    def __init__(self, driver, logger, selenium_facade, card_collection_strategy: CardCollectionStrategy):
        super().__init__(driver, logger, selenium_facade)
        self.gender_filter = GenderFilter(selenium_facade, GENDER_CHECKBOX_XPATH)
        self.age_range_slider = AgeFilter(selenium_facade, AGE_SLIDER_XPATH)
        self.card_collection_strategy = card_collection_strategy

    def load_cards(self, url):
        """Loads the cards page and handles the initial popup."""
        self.load(url) 
        self.click_element(POPUP_BUTTON)
        self.logger.info("Close popup.")

    def wait_for_page_load(self, url=""):
        """Waits for the cards page to load completely."""
        WebDriverWait(self.driver, 10).until(EC.url_contains(url))

        self.logger.info("Waiting for cards container to load...")
        self.find_element(CARDS_CONTAINER_XPATH)
        self.logger.info("Cards container loaded.")

    def apply_filters(self):
        """Applies the gender and age range filters."""
        try:
            self.logger.info("Setting filters...")
            self.gender_filter.select_gender("female")
            self.age_range_slider.set_age_range(25, 33)
            self.logger.info("Filters applied.")
        except Exception as e:
            self.logger.error(f"Error setting filters: {e}")
        time.sleep(10) 


    def process_cards(self):
        """Processes visible cards on the page using the selected strategy."""
        try:
            cards = self.card_collection_strategy.collect_cards(self.driver)
            self.card_collection_strategy.iterate_through_cards(self.driver, cards)  # Use the strategy to iterate

        except Exception as e:
            self.logger.error(f"Error processing cards: {e}")