from base import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pageobjects.xpaths import *
from selenium.webdriver.common.keys import Keys

class CardsPage(BasePage):
    def __init__(self, driver, logger, selenium_facade):
        super().__init__(driver, logger, selenium_facade)

    def load_cards(self, url):
        """Loads the cards page and handles the initial popup."""
        
        # Navigate to the cards
        self.load(url)  # Use the load method from BasePage
        
        # Click the clock popup button
        self.click_element(POPUP_BUTTON)
        self.logger.info("Close popup.")

    def wait_for_page_load(self, url=""):
        # Wait for login to complete and redirect to happen
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(url)  # Wait for URL to contain cards page path
        )

        # Wait for a specific element that indicates the cards are loaded
        self.logger.info("Waiting for cards container to load...")
        self.find_element(CARDS_CONTAINER_XPATH)
        self.logger.info("Cards container loaded.")


    def apply_filters(self):
        # --- Filters Section ---
        try:
            self.logger.info("Setting filters...")

            # 2. Click the Gender checkbox using JavaScript
            gender_checkbox = self.find_element(GENDER_CHECKBOX_XPATH)
            self.driver.execute_script("arguments[0].click(); arguments[0].dispatchEvent(new Event('change'));", gender_checkbox)
            self.logger.info("Clicked gender checkbox using JavaScript and triggered change event.")

            # 3. Get the slider element
            slider_element = self.find_element(AGE_SLIDER_XPATH)

            # 4. Get the min and max input elements within the slider
            # min_input = slider_element.find_element(By.CSS_SELECTOR, "input.jet-range__slider__input--min")
            # max_input = slider_element.find_element(By.CSS_SELECTOR, "input.jet-range__slider__input--max")

            # Get the min and max input elements within the slider (using the facade)
            min_input = self.find_element(f"{AGE_SLIDER_XPATH}//input[@class='jet-range__slider__input jet-range__slider__input--min']", timeout=20) 
            max_input = self.find_element(f"{AGE_SLIDER_XPATH}//input[@class='jet-range__slider__input jet-range__slider__input--max']", timeout=20)

            # 5. Set the slider values using JavaScript
            self.execute_script("arguments[0].value = 25; arguments[0].dispatchEvent(new Event('input'));", min_input)
            self.execute_script("arguments[0].value = 33; arguments[0].dispatchEvent(new Event('input'));", max_input)

            # Send Enter Key to the slider 
            slider_element = self.find_element(AGE_SLIDER_XPATH)
            slider_element.send_keys(Keys.ENTER)

            self.logger.info("Set age filter range.")

        except Exception as e:
            self.logger.error(f"Error setting filters: {e}")

        time.sleep(10)  # Wait for filters to apply

    def process_cards(self):
        # --- Cards Page (after filters are applied) ---

        # --- Scroll Down until No More Cards ---
        self.logger.info("Scrolling to load all cards...")
        # Initialize cards list before the loop 
        cards = [] 
        while True:
            # Scroll to the bottom of the page
            self.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)  # Wait for cards to load

            # Try to find more cards
            new_cards = self.find_elements(CARDS_XPATH) 

            # Wait for a specific element that indicates the cards are loaded
            self.logger.info("Waiting for cards container to load...")
            self.find_element(CARDS_CONTAINER_XPATH)
            self.logger.info("Cards container loaded.")

            # If no new cards are found, break the loop
            if len(new_cards) == len(cards):
                break

            # Update the cards list
            cards = new_cards

        self.logger.info("All cards loaded.")

        # Find all cards using a more reliable XPath
        cards = self.find_elements(CARDS_XPATH)
        self.logger.info(f"Found {len(cards)} cards.")
        time.sleep(30)

        # --- Process Cards ---
        # Iterate through cards
        for index, card in enumerate(cards):
            card_name = ""
            try:
                # Locate the card name element 
                card_name = self.get_element_text(CARD_NAME, timeout=20)
                self.logger.info(f"Processing card {index+1}: {card_name}")

                # --- Click on the "View" Button ---
                self.click_element(CARD_BUTTON)
                self.logger.info(f"Clicked 'View' button on card: {card_name}")

                # --- Switch to New Tab, Perform Actions, and Close ---
                self.driver.switch_to.window(self.driver.window_handles[-1])  # Switch to the new tab

                # --- Your actions in the new tab ---
                # ... (your code to extract data or interact with elements on the new page) ...

                self.driver.close()  # Close the new tab
                self.driver.switch_to.window(self.driver.window_handles[0])  # Switch back to the main cards tab

            except Exception as e:
                self.logger.error(f"Error processing card '{card_name}': {e}")