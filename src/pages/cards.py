import time
from .base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.xpaths import *
from src.pages.pageobjects.card import Card
from src.pages.pageobjects.gender_filter import GenderFilter
from src.pages.pageobjects.age_filter import AgeFilter

class CardsPage(BasePage):
    def __init__(self, driver, logger, selenium_facade):
        super().__init__(driver, logger, selenium_facade)
        self.gender_filter = GenderFilter(selenium_facade, "//div[@class='jet-checkboxes-list']")
        self.age_range_slider = AgeFilter(selenium_facade, AGE_SLIDER_XPATH)

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
        """Scrolls through the cards, clicks on each 'View' button, and handles new tabs."""
        self.logger.info("Scrolling to load all cards...")
        cards = []
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)
            new_cards = self.find_elements(CARDS_XPATH)
            if len(new_cards) == len(cards):
                break
            cards = new_cards
        self.logger.info("All cards loaded.")

        cards = self.find_elements(CARDS_XPATH)
        self.logger.info(f"Found {len(cards)} cards.")
        time.sleep(30)

        for index, card_element in enumerate(cards):
            card = Card(self.selenium_facade, card_element)
            try:
                card_name = card.get_name()
                self.logger.info(f"Processing card {index + 1}: {card_name}")

                card.click_view_button()
                self.logger.info(f"Clicked 'View' button on card: {card_name}")

                self.driver.switch_to.window(self.driver.window_handles[-1])

                # --- Your actions in the new tab ---
                # ... (your code to extract data or interact with elements on the new page) ...

                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])

            except Exception as e:
                self.logger.error(f"Error processing card: {e}")