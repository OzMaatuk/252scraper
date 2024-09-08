from abc import ABC, abstractmethod

class LoginStrategy(ABC):
    """Base class for login strategies."""

    @abstractmethod
    def login(self, driver, username, password):
        """Logs into the website using the specified credentials.

        Args:
            driver (webdriver): The Selenium WebDriver instance.
            username (str): The username or email.
            password (str): The password.
        """
        pass


# from .login_strategy import LoginStrategy
from src.pages.xpaths import *

class StandardLogin(LoginStrategy):
    """Logs in using the standard username/password form."""

    def __init__(self, selenium_facade):
        self.selenium_facade = selenium_facade

    def login(self, username, password):
        """Logs in using the standard username/password form."""
        try:
            self.enter_email(username)
            self.enter_password(password)
            self.click_submit_button()

        except Exception as e:
            raise Exception(f"Error during standard login: {e}")

    def enter_email(self, email):
        """Enters the email address into the email field."""
        self.selenium_facade.enter_text(LOGIN_EMAIL_TEXTBOX, email)

    def enter_password(self, password):
        """Enters the password into the password field."""
        self.selenium_facade.enter_text(LOGIN_PASSWORD_TEXTBOX, password)

    def click_submit_button(self):
        """Clicks the submit button on the login form."""
        self.selenium_facade.click_element(LOGIN_SUBMIT_BUTTON)