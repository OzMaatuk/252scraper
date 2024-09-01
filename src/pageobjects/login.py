from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pageobjects.xpaths import *

class LoginPage:

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def load(self, url):
        # Navigate to the website (login page)
        self.logger.info(f"Navigating to: {url}")
        self.driver.get(url)

    def login(self, url, email, password):
        # --- Log In ---
        try:
            self.logger.info("Waiting for login form to load...")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, LOGIN_FORM_XPATH))
            )
            self.logger.info("Login form loaded.")

            # Enter email
            email_input = self.driver.find_element(By.XPATH, LOGIN_EMAIL_TEXTBOX)
            email_input.send_keys(email)

            # Enter password 
            password_input = self.driver.find_element(By.XPATH, LOGIN_PASSWORD_TEXTBOX)
            password_input.send_keys(password)

            # Click login button
            login_button = self.driver.find_element(By.XPATH, LOGIN_SUBMIT_BUTTON)
            login_button.click()

            # Wait for login to complete (you might need to adjust this wait)
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be(url)  # Wait for the cards page URL
            )

            self.logger.info("Login successful!")

        except Exception as e:
            self.logger.error(f"Error during login: {e}")
            self.driver.quit()
            exit(1)