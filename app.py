import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv
from src.patterns.automation import Automation
from src.patterns.facade import SeleniumFacade
from src.patterns.login_strategy import StandardLogin 
from src.patterns.cards_strategy import StandardCardCollection


# Load environment variables from .env
load_dotenv()

# Get variables from environment
login_url = os.getenv('LOGIN_URL')
cards_url = os.getenv('CARDS_URL')
members_url = os.getenv('MEMBERS_URL')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# Set up logging
def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("App start.")
    return logger

# Set up WebDriver 
def setup_webdriver(chromedriver_path):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment for headless mode
    chrome_options.add_argument("--verbose")

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Main execution
if __name__ == "__main__":
    logger = setup_logging()

    # Set up WebDriver
    chromedriver_path = "D:\chromedriver\chromedriver-win64\chromedriver.exe"
    driver = setup_webdriver(chromedriver_path)
    logger.info("WebDriver initialized.")

    # Create the SeleniumFacade
    selenium_facade = SeleniumFacade(driver)

    # Create Strategy objects
    login_strategy = StandardLogin(selenium_facade)
    card_collection_strategy = StandardCardCollection(selenium_facade, logger)

    # Start automation
    automation = Automation(driver, logger, members_url, selenium_facade, login_url, cards_url, username, password, login_strategy, card_collection_strategy)
    automation.run()

    # Clean up
    logger.info("Closing WebDriver.")
    driver.quit()
    logger.info("Automation complete! 🪄✨")