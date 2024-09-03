from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pageobjects.xpaths import *

class BasePage:
    """
    Base class for page objects, providing common methods and structure.
    """
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def load(self, url):
        """
        Loads a page by navigating to the specified URL and waiting for it to load.

        Args:
            url (str): The URL to navigate to.
        """
        self.logger.info(f"Navigating to: {url}")
        self.driver.get(url)
        self.wait_for_page_load(url)

    def wait_for_page_load(self, url=""):
        """
        Waits for a specific element to be present, indicating the page has loaded.
        """
        raise NotImplementedError("Please Implement this method")
    
        if 'login' in url:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, LOGIN_FORM_XPATH))
            )
        elif 'cards' in url:
            # Wait for login to complete and redirect to happen
            WebDriverWait(self.driver, 10).until(
                EC.url_contains(url)  # Wait for URL to contain cards page path
            )
            # Wait for a specific element that indicates the cards are loaded
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, CARDS_CONTAINER_XPATH))
            )
        else:
            self.logger.error(f"Unknown URL: {url}. Can't wait for page load.")
            # Add a default wait or raise an exception if necessary

        self.logger.info("Page loaded successfully.")

    def find_element(self, locator, by=By.XPATH, timeout=10):
        """
        Finds a single element on the page.

        Args:
            locator (str): The locator for the element.
            by (By, optional): The method used to locate the element (By.XPATH, By.ID, etc.). Defaults to By.XPATH.
            timeout (int, optional): The maximum time to wait for the element to be present. Defaults to 10 seconds.

        Returns:
            WebElement: The found element.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def find_elements(self, locator, by=By.XPATH, timeout=10):
        """
        Finds multiple elements on the page.

        Args:
            locator (str): The locator for the elements.
            by (By, optional): The method used to locate the elements (By.XPATH, By.ID, etc.). Defaults to By.XPATH.
            timeout (int, optional): The maximum time to wait for the elements to be present. Defaults to 10 seconds.

        Returns:
            list of WebElements: A list of the found elements.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((by, locator))
        )

    def click_element(self, locator, by=By.XPATH, timeout=10):
        """
        Finds an element and clicks it.

        Args:
            locator (str): The locator for the element.
            by (By, optional): The method used to locate the element. Defaults to By.XPATH.
            timeout (int, optional): The maximum time to wait for the element to be clickable. Defaults to 10 seconds.
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()