from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

class SeleniumFacade:
    """Provides a simplified interface for common Selenium WebDriver interactions."""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator: str, by: By = By.XPATH, timeout: int = 10, parent_element=None):
        """
        Finds a single element on the page. 

        Args:
            locator (str): The locator for the element.
            by (By, optional): The method used to locate the element (By.XPATH, By.ID, etc.). Defaults to By.XPATH.
            timeout (int, optional): The maximum time to wait for the element to be present. Defaults to 10 seconds.
            parent_element (WebElement, optional): The parent element to search within. Defaults to None (searches the entire page).

        Returns:
            WebElement: The found element.

        Raises:
            TimeoutException: If the element is not found within the timeout period.
        """
        try:
            if parent_element:
                return WebDriverWait(parent_element, timeout).until(
                    EC.presence_of_element_located((by, locator))
                )
            else:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((by, locator))
                )
        except TimeoutException as e:
            raise TimeoutException(f"Element not found: {locator} by {by}") from e

    def find_elements(self, locator: str, by: By = By.XPATH, timeout: int = 10):
        """
        Finds multiple elements on the page.

        Args:
            locator (str): The locator for the elements.
            by (By, optional): The method used to locate the elements (By.XPATH, By.ID, etc.). Defaults to By.XPATH.
            timeout (int, optional): The maximum time to wait for the elements to be present. Defaults to 10 seconds.

        Returns:
            list: A list of found elements.

        Raises:
            TimeoutException: If the elements are not found within the timeout period.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((by, locator))
            )
        except TimeoutException as e:
            raise TimeoutException(f"Elements not found: {locator} by {by}") from e

    def click_element(self, locator: str, by: By = By.XPATH, timeout: int = 10):
        """
        Finds an element and clicks it.

        Args:
            locator (str): The locator for the element.
            by (By, optional): The method used to locate the element (By.XPATH, By.ID, etc.). Defaults to By.XPATH.
            timeout (int, optional): The maximum time to wait for the element to be clickable. Defaults to 10 seconds.

        Raises:
            TimeoutException: If the element is not clickable within the timeout period.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, locator))
            )
            element.click()
        except TimeoutException as e:
            raise TimeoutException(f"Element not clickable: {locator} by {by}") from e

    def get_element_text(self, locator: str, by: By = By.XPATH, timeout: int = 10, parent_element=None) -> str:
        """
        Gets the text content of an element.

        Args:
            locator (str): The locator for the element.
            by (By, optional): The method used to locate the element (By.XPATH, By.ID, etc.). Defaults to By.XPATH.
            timeout (int, optional): The maximum time to wait for the element to be present. Defaults to 10 seconds.
            parent_element (WebElement, optional): The parent element to search within. Defaults to None (searches the entire page).

        Returns:
            str: The text content of the found element.

        Raises:
            TimeoutException: If the element is not found within the timeout period.
        """
        try:
            element = self.find_element(locator, by, timeout, parent_element)
            return element.text
        except TimeoutException as e:
            raise TimeoutException(f"Element text not retrievable: {locator} by {by}") from e

    def enter_text(self, locator: str, text: str, by: By = By.XPATH, timeout: int = 10):
        """
        Enters text into an input field.

        Args:
            locator (str): The locator for the input field.
            text (str): The text to enter into the input field.
            by (By, optional): The method used to locate the input field (By.XPATH, By.ID, etc.). Defaults to By.XPATH.
            timeout (int, optional): The maximum time to wait for the input field to be present. Defaults to 10 seconds.

        Raises:
            TimeoutException: If the input field is not found within the timeout period.
        """
        try:
            element = self.find_element(locator, by, timeout)
            element.send_keys(text)
        except TimeoutException as e:
            raise TimeoutException(f"Unable to enter text: {locator} by {by}") from e

    def execute_script(self, script: str, *args):
        """
        Executes JavaScript in the browser.

        Args:
            script (str): The JavaScript code to execute.
            *args: Any additional arguments to pass to the script.

        Returns:
            Any: The result of the executed script.
        """
        try:
            return self.driver.execute_script(script, *args)
        except WebDriverException as e:
            raise WebDriverException(f"Script execution failed: {script}") from e