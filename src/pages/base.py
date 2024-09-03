from selenium.webdriver.common.by import By
from src.pages.xpaths import *

class BasePage:
    """
    Base class for page objects, providing common methods and structure.
    """
    def __init__(self, driver, logger, selenium_facade):
        self.driver = driver
        self.logger = logger
        self.selenium_facade = selenium_facade

    def load(self, url):
        """
        Loads a page by navigating to the specified URL and waiting for it to load.
        """
        self.logger.info(f"Navigating to: {url}")
        self.driver.get(url)
        self.wait_for_page_load(url)

    def wait_for_page_load(self, url=""):
        """
        Waits for a specific element to be present, indicating the page has loaded.
        """
        raise NotImplementedError("Please Implement this method")
    def find_element(self, locator, by=By.XPATH, timeout=10):
        """
        Finds a single element on the page using the SeleniumFacade.
        """
        return self.selenium_facade.find_element(locator, by, timeout)

    def find_elements(self, locator, by=By.XPATH, timeout=10):
        """
        Finds multiple elements on the page using the SeleniumFacade.
        """
        return self.selenium_facade.find_elements(locator, by, timeout)

    def click_element(self, locator, by=By.XPATH, timeout=10):
        """
        Finds an element and clicks it using the SeleniumFacade.
        """
        self.selenium_facade.click_element(locator, by, timeout)

    def get_element_text(self, locator, by=By.XPATH, timeout=10):
        """Gets the text content of an element using the SeleniumFacade."""
        return self.selenium_facade.get_element_text(locator, by, timeout)

    def enter_text(self, locator, text, by=By.XPATH, timeout=10):
        """Enters text into an input field using the SeleniumFacade."""
        self.selenium_facade.enter_text(locator, text, by, timeout)

    def execute_script(self, script, *args):
        """Executes JavaScript in the browser using the SeleniumFacade."""
        self.selenium_facade.execute_script(script, *args)