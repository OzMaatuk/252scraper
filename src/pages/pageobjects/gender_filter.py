import logging
from src.pages.xpaths import *
from src.patterns.facade import SeleniumFacade

class GenderFilter:
    """Represents the gender filter element."""

    def __init__(self, selenium_facade: SeleniumFacade, container_locator: str):
        """
        Initializes the GenderFilter.

        Args:
            selenium_facade (SeleniumFacade): The SeleniumFacade instance for interacting with the browser.
            container_locator (str): The XPath locator for the container element of the gender filter.
        """
        self.selenium_facade = selenium_facade
        self.container_locator = container_locator

    def select_gender(self, gender: str):
        """
        Selects the specified gender filter.

        Args:
            gender (str): The gender to select (e.g., 'female', 'male').
        """
        try:
            gender_checkbox_xpath = f"{self.container_locator}//input[@type='checkbox' and @value='{gender}']"

            # Use JavaScript to click the checkbox and trigger the change event
            self.selenium_facade.execute_script(
                f"""
                const checkbox = document.evaluate('{gender_checkbox_xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                checkbox.checked = true;
                checkbox.dispatchEvent(new Event('change')); 
                """ 
            )

            logging.info(f"Selected gender: {gender}")
        except Exception as e:
            logging.error(f"Error selecting gender '{gender}': {e}")
            raise


            # # 2. Click the Gender checkbox using JavaScript
            # gender_checkbox = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, GENDER_CHECKBOX_XPATH))
            # )
            # self.driver.execute_script("arguments[0].click(); arguments[0].dispatchEvent(new Event('change'));", gender_checkbox)
            # self.logger.info("Clicked gender checkbox using JavaScript and triggered change event.")
