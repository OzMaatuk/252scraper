from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import logging

class BasePage:
    """
    Base class for page objects, providing common methods and structure.
    """
    def __init__(self, driver: WebDriver, logger: logging.Logger, selenium_facade: SeleniumFacade):
        self.driver = driver
        self.logger = logger
        self.selenium_facade = selenium_facade

    def load(self, url: str):
        """
        Loads a page by navigating to the specified URL and waiting for it to load.

        Args:
            url (str): The URL of the page to load.
        """
        self.logger.info(f"Navigating to: {url}")
        self.driver.get(url)
        self.wait_for_page_load(url)

    def wait_for_page_load(self, url: str = ""):
        """
        Waits for a specific element to be present, indicating the page has loaded.

        Args:
            url (str, optional): The URL of the page to wait for. Defaults to "".

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("Please Implement this method")

    def find_element(self, locator: str, by: By = By.XPATH, timeout: int = 10):
        """
        Finds a single element on the page using the SeleniumFacade.

        Args:
            locator (str): The locator for the element.
            by (By, optional): The method used to locate the element (By.XPATH, By.ID, etc.). Defaults to By.XPATH.
            timeout (int, optional): The maximum time to wait for the element to be present. Defaults to 10 seconds.

        Returns:
            WebElement: The found element.
        """
        return self.selenium_facade.find_element(locator, by, timeout)

    def find_elements(self, locator: str, by: By = By.XPATH, timeout: int = 10):
        """
        Finds multiple elements on the page using the SeleniumFacade.

        Args:
            locator (str): The locator for the elements.
            by (By, optional): The method used to locate the elements (By.XPATH, By.ID, etc.). Defaults to By.XPATH.
            timeout (int, optional): The maximum time to wait for the elements to be present. Defaults to 10 seconds.

        Returns:
            list: A list of found elements.
        """
        return self.selenium_facade.find_elements(locator, by, timeout)

    def click_element(self, locator: str, by: By = By.XPATH, timeout: int = 10):
        """
        Finds an element and clicks it using the SeleniumFacade.

        Args:
            locator (str): The locator for the element.
            by (By, optional): The method used to locate the element (By.XPATH, By.ID, etc.). Defaults to By.XPATH.
            timeout (int, optional): The maximum time to wait for the element to be clickable. Defaults to 10 seconds.
        """
        self.selenium_facade.click_element(locator, by, timeout)

    def get_element_text(self, locator: str, by: By = By.XPATH, timeout: int = 10) -> str:
        """
        Gets the text content of an element using the SeleniumFacade.

        Args:
            locator (str): The locator for the element.
            by (By, optional): The method used to locate the element (By.XPATH, By.ID, etc.). Defaults to By.XPATH.
            timeout (int, optional): The maximum time to wait for the element to be present. Defaults to 10 seconds.

        Returns:
            str: The text content of the found element.
        """
        return self.selenium_facade.get_element_text(locator, by, timeout)

    def enter_text(self, locator: str, text: str, by: By = By.XPATH, timeout: int = 10):
        """
        Enters text into an input field using the SeleniumFacade.

        Args:
            locator (str): The locator for the input field.
            text (str): The text to enter into the input field.
            by (By, optional): The method used to locate the input field (By.XPATH, By.ID, etc.). Defaults to By.XPATH.
            timeout (int, optional): The maximum time to wait for the input field to be present. Defaults to 10 seconds.
        """
        self.selenium_facade.enter_text(locator, text, by, timeout)

    def execute_script(self, script: str, *args):
        """
        Executes JavaScript in the browser using the SeleniumFacade.

        Args:
            script (str): The JavaScript code to execute.
            *args: Any additional arguments to pass to the script.

        Returns:
            Any: The result of the executed script.
        """
        self.selenium_facade.execute_script(script, *args)