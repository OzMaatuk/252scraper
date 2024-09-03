from src.pages.xpaths import *

class GenderFilter:
    """Represents the gender filter element."""
    def __init__(self, selenium_facade, container_locator):
        self.selenium_facade = selenium_facade
        self.container_locator = container_locator

    def select_gender(self, gender):
        """Selects the specified gender filter."""
        gender_checkbox_locator = f"{self.container_locator}//input[@type='checkbox' and @value='{gender}']"
        self.selenium_facade.click_element(gender_checkbox_locator)