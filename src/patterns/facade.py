from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumFacade:
    """Provides a simplified interface for common Selenium WebDriver interactions."""

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, by=By.XPATH, timeout=10, parent_element=None):
        """Finds a single element on the page. 

        Args:
            locator (str): The locator for the element.
            by (By, optional): The method used to locate the element (By.XPATH, By.ID, etc.). Defaults to By.XPATH.
            timeout (int, optional): The maximum time to wait for the element to be present. Defaults to 10 seconds.
            parent_element (WebElement, optional): The parent element to search within. Defaults to None (searches the entire page).

        Returns:
            WebElement: The found element.
        """
        if parent_element:
            return WebDriverWait(parent_element, timeout).until(
                EC.presence_of_element_located((by, locator))
            )
        else:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, locator))
            )

    def find_elements(self, locator, by=By.XPATH, timeout=10):
        """Finds multiple elements on the page."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((by, locator))
        )

    def click_element(self, locator, by=By.XPATH, timeout=10):
        """Finds an element and clicks it."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()

    def get_element_text(self, locator, by=By.XPATH, timeout=10):
        """Gets the text content of an element."""
        element = self.find_element(locator, by, timeout)
        return element.text
    
    def get_element_text(self, locator, by=By.XPATH, timeout=10, parent_element=None):
        """Gets the text content of an element."""
        element = self.find_element(locator, by, timeout, parent_element)
        return element.text

    def enter_text(self, locator, text, by=By.XPATH, timeout=10):
        """Enters text into an input field."""
        element = self.find_element(locator, by, timeout)
        element.send_keys(text)

    def execute_script(self, script, *args):
        """Executes JavaScript in the browser."""
        self.driver.execute_script(script, *args)