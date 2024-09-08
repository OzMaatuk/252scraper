from .base import BasePage
from .xpaths import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.patterns.login_strategy import LoginStrategy

class LoginPage(BasePage):
    def __init__(self, driver, logger, selenium_facade, login_strategy: LoginStrategy):
        super().__init__(driver, logger, selenium_facade)
        self.login_strategy = login_strategy

    def login(self, redirect_url, email, password):
        """
        Logs in to the website, using login strategy
        """
        try:
            self.logger.info("Start Login")
            self.login_strategy.login(email, password) # Use the strategy
            WebDriverWait(self.driver, 10).until(EC.url_to_be(redirect_url))
            self.logger.info("Login successful!")

        except Exception as e:
            self.logger.error(f"Error during login: {e}")
            self.driver.quit()
            exit(1)

    def wait_for_page_load(self, url=""):
        """Waits for the login form to be present."""
        try:
            self.logger.info("Waiting for login form to load...")
            self.find_element(LOGIN_FORM_XPATH)
            self.logger.info("Login form loaded.")

        except Exception as e:
            self.logger.error(f"Error during login page load: {e}")
            self.driver.quit()
            exit(1)