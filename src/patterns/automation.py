from src.pages.login import LoginPage
from src.pages.cards import CardsPage
from src.patterns.login_strategy import LoginStrategy
from src.patterns.cards_strategy import CardCollectionStrategy

class State:
    """
    Defines the possible states of the automation.
    Each state represents a stage in the automation process.
    """
    LOGIN = 'login'
    LOAD_CARDS = 'load_cards'
    APPLY_FILTERS = 'apply_filters'
    PROCESS_CARDS = 'process_cards'
    # ... add more states as needed

class Automation:
    """
    Using State-Machine pattern to manage the state and flow of the automation.
    """
    def __init__(self, driver, logger, members_url, facade, login_url, cards_url, username, password, login_strategy: LoginStrategy, card_collection_strategy: CardCollectionStrategy):
        """
        Initializes the state machine.

        Args:
            driver (webdriver): The Selenium WebDriver instance.
            logger (logging.Logger): The logger for output messages.
            login_url (str): The URL of the login page.
            cards_url (str): The URL of the cards page.
            username (str): The username for login.
            password (str): The password for login.
            login_strategy (LoginStrategy): The strategy for logging into the website.
            card_collection_strategy (CardCollectionStrateg): The strategy for handling card collections.
        """
        self.driver = driver
        self.logger = logger
        self.current_state = State.LOGIN  # Start in the login state

        # Credentials & URLs
        self.login_url = login_url
        self.cards_url = cards_url
        self.members_url = members_url
        self.facade = facade
        self.username = username
        self.password = password

        # Strategies
        self.login_strategy = login_strategy
        self.card_collection_strategy = card_collection_strategy
        
        # Page Objects
        self.login_page = LoginPage(self.driver, self.logger, self.facade, self.login_strategy)
        self.cards_page = CardsPage(self.driver, self.logger, self.facade, self.card_collection_strategy)

    def run(self):
        """
        The main loop of the state machine.
        Continues to execute actions based on the current state.
        """
        while True: # The loop can be controlled by a condition for ending the automation
            if self.current_state == State.LOGIN:
                self.handle_login_state()
            elif self.current_state == State.LOAD_CARDS:
                self.handle_load_cards_state()
            elif self.current_state == State.APPLY_FILTERS:
                self.handle_apply_filters_state()
            elif self.current_state == State.PROCESS_CARDS:
                self.handle_process_cards_state()
            # ... handle more states
            else:
                self.logger.error(f"Invalid state: {self.current_state}")
                break # Exit the loop if in invalid state 

    def handle_login_state(self):
        """Handles the logic for the LOGIN state."""
        self.login_page.load(self.login_url)
        self.login_page.login(self.members_url, self.username, self.password)
        self.transition_to(State.LOAD_CARDS)  # Transition to the next state after login

    def handle_load_cards_state(self):
        """Handles the logic for the LOAD_CARDS state."""
        self.cards_page.load_cards(self.cards_url)
        self.transition_to(State.APPLY_FILTERS)  # Transition to the next state

    def handle_apply_filters_state(self):
        """Handles the logic for the APPLY_FILTERS state."""
        self.cards_page.apply_filters()
        self.transition_to(State.PROCESS_CARDS) # Transition to the next state

    def handle_process_cards_state(self):
        """Handles the logic for the PROCESS_CARDS state."""
        self.cards_page.process_cards()
        # ... (add logic for transitioning to other states or ending automation if needed)

    def transition_to(self, new_state):
        """
        Transitions the state machine to a new state.

        Args:
            new_state (str): The desired new state.
        """
        self.logger.info(f"Transitioning from state '{self.current_state}' to '{new_state}'")
        self.current_state = new_state