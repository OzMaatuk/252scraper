import logging
import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

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
def setup_logging() -> logging.Logger:
    """
    Sets up the logging configuration.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("App start.")
    return logger

# Set up WebDriver 
def setup_webdriver(chromedriver_path: str) -> webdriver.Chrome:
    """
    Sets up the Selenium WebDriver with the specified ChromeDriver path.

    Args:
        chromedriver_path (str): Path to the ChromeDriver executable.

    Returns:
        webdriver.Chrome: Configured WebDriver instance.
    """
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment for headless mode
    chrome_options.add_argument("--verbose")

    try:
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except WebDriverException as e:
        logger.error(f"Failed to initialize WebDriver: {e}")
        raise

if __name__ == "__main__":
    logger = setup_logging()

    # Set up WebDriver
    chromedriver_path = "D:\\chromedriver\\chromedriver-win64\\chromedriver.exe"
    try:
        driver = setup_webdriver(chromedriver_path)
        logger.info("WebDriver initialized.")
    except WebDriverException:
        logger.critical("Exiting due to WebDriver initialization failure.")
        exit(1)

    # Create the SeleniumFacade
    selenium_facade = SeleniumFacade(driver)

    # Create Strategy objects
    login_strategy = StandardLogin(selenium_facade)
    card_collection_strategy = StandardCardCollection(selenium_facade, logger)

    # Start automation
    automation = Automation(driver, 
                            logger, 
                            members_url, 
                            selenium_facade, 
                            login_url, 
                            cards_url, 
                            username, 
                            password, 
                            login_strategy, 
                            card_collection_strategy)
    try:
        automation.run()
    except Exception as e:
        logger.error(f"An error occurred during automation: {e}")
    finally:
        # Clean up
        logger.info("Closing WebDriver.")
        driver.quit()
        logger.info("Automation complete! 🪄✨")