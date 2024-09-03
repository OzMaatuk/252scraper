from src.pages.xpaths import *

class Card:
    """Represents an individual card on the page."""
    def __init__(self, selenium_facade, card_element):
        self.selenium_facade = selenium_facade
        self.card_element = card_element

    def get_name(self):
        """Gets the name from the card."""
        return self.selenium_facade.get_element_text(CARD_NAME, parent_element=self.card_element)

    def click_view_button(self):
        """Clicks the 'View' button on the card."""
        view_button = self.selenium_facade.find_element(CARD_BUTTON, parent_element=self.card_element)
        view_button.click() 