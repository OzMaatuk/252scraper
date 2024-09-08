from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver

class LoginStrategy(ABC):
    """Base class for login strategies."""

    @abstractmethod
    def login(self, driver: WebDriver, username: str, password: str):
        """
        Logs into the website using the specified credentials.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.
            username (str): The username or email.
            password (str): The password.
        """
        pass


from src.pages.xpaths import *
from src.patterns.facade import SeleniumFacade

class StandardLogin(LoginStrategy):
    """Logs in using the standard username/password form."""

    def __init__(self, selenium_facade: SeleniumFacade):
        """
        Initializes the StandardLogin strategy.

        Args:
            selenium_facade (SeleniumFacade): The SeleniumFacade instance for interacting with the browser.
        """
        self.selenium_facade = selenium_facade

    def login(self, driver: WebDriver, username: str, password: str):
        """
        Logs in using the standard username/password form.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.
            username (str): The username or email.
            password (str): The password.
        """
        try:
            self.enter_email(username)
            self.enter_password(password)
            self.click_submit_button()
        except Exception as e:
            raise Exception(f"Error during standard login: {e}")

    def enter_email(self, email: str):
        """
        Enters the email address into the email field.

        Args:
            email (str): The email address to enter.
        """
        self.selenium_facade.enter_text(LOGIN_EMAIL_TEXTBOX, email)

    def enter_password(self, password: str):
        """
        Enters the password into the password field.

        Args:
            password (str): The password to enter.
        """
        self.selenium_facade.enter_text(LOGIN_PASSWORD_TEXTBOX, password)

    def click_submit_button(self):
        """Clicks the submit button on the login form."""
        self.selenium_facade.click_element(LOGIN_SUBMIT_BUTTON)