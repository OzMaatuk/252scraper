import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base import BasePage
from src.pages.xpaths import *
from src.patterns.login_strategy import LoginStrategy
from src.patterns.facade import SeleniumFacade

class LoginPage(BasePage):
    def __init__(self, driver: WebDriver, logger: logging.Logger, selenium_facade: SeleniumFacade, login_strategy: LoginStrategy):
        """
        Initializes the LoginPage.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.
            logger (logging.Logger): The logger for output messages.
            selenium_facade (SeleniumFacade): The SeleniumFacade instance for interacting with the browser.
            login_strategy (LoginStrategy): The strategy for logging into the website.
        """
        super().__init__(driver, logger, selenium_facade)
        self.login_strategy = login_strategy

    def login(self, redirect_url: str, email: str, password: str):
        """
        Logs in to the website using the login strategy.

        Args:
            redirect_url (str): The URL to redirect to after a successful login.
            email (str): The email address for login.
            password (str): The password for login.
        """
        try:
            self.logger.info("Start Login")
            self.login_strategy.login(self.driver, email, password)  # Use the strategy
            WebDriverWait(self.driver, 10).until(EC.url_to_be(redirect_url))
            self.logger.info("Login successful!")

        except Exception as e:
            self.logger.error(f"Error during login: {e}")
            self.driver.quit()
            exit(1)

    def wait_for_page_load(self, url: str = ""):
        """
        Waits for the login form to be present.

        Args:
            url (str, optional): The URL of the page to wait for. Defaults to "".
        """
        try:
            self.logger.info("Waiting for login form to load...")
            self.find_element(LOGIN_FORM_XPATH)
            self.logger.info("Login form loaded.")

        except Exception as e:
            self.logger.error(f"Error during login page load: {e}")
            self.driver.quit()
            exit(1)