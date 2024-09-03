from .base import BasePage
from .xpaths import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginForm:
    """Represents the login form element."""
    def __init__(self, selenium_facade, form_locator):
        self.selenium_facade = selenium_facade
        self.form_locator = form_locator

    def enter_email(self, email):
        """Enters the email address into the email field."""
        email_input = self.selenium_facade.find_element(f"{self.form_locator}{LOGIN_EMAIL_TEXTBOX}")
        email_input.send_keys(email)

    def enter_password(self, password):
        """Enters the password into the password field."""
        password_input = self.selenium_facade.find_element(f"{self.form_locator}{LOGIN_PASSWORD_TEXTBOX}")
        password_input.send_keys(password)

    def click_submit(self):
        """Clicks the submit button on the login form."""
        self.selenium_facade.click_element(f"{self.form_locator}{LOGIN_SUBMIT_BUTTON}")

class LoginPage(BasePage):
    def __init__(self, driver, logger, selenium_facade):
        super().__init__(driver, logger, selenium_facade)
        self.login_form = LoginForm(selenium_facade, "")  # No container locator needed here

    def login(self, redirect_url, email, password):
        """
        Logs in to the website.
        """
        try:
            self.login_form.enter_email(email)
            self.login_form.enter_password(password)
            self.login_form.click_submit()

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