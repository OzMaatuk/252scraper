from base import BasePage
from .xpaths import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    def login(self, redirect_url, email, password):
        """
        Logs in to the website.

        Args:
            redirect_url (str): The URL to expect after successful login.
            email (str): The user's email address.
            password (str): The user's password.
        """
        try:
            # Enter email
            email_input = self.find_element(LOGIN_EMAIL_TEXTBOX)
            email_input.send_keys(email)

            # Enter password
            password_input = self.find_element(LOGIN_PASSWORD_TEXTBOX)
            password_input.send_keys(password)

            # Click login button
            self.click_element(LOGIN_SUBMIT_BUTTON)

            # Wait for login to complete 
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be(redirect_url) 
            )

            self.logger.info("Login successful!")

        except Exception as e:
            self.logger.error(f"Error during login: {e}")
            self.driver.quit()
            exit(1)

    def wait_for_page_load(self, url=""):
        """
        Waits for a specific element to be present, indicating the page has loaded.

        Args:
            url (str): The URL of the page (used to determine the element to wait for).
        """
        try:
            self.logger.info("Waiting for login form to load...")
            self.find_element(LOGIN_FORM_XPATH)
            self.logger.info("Login form loaded.")

        except Exception as e:
            self.logger.error(f"Error during login page load: {e}")
            self.driver.quit()
            exit(1)