# 252WebAutomation

## Description

This project uses Selenium WebDriver to automate the process of scraping data from the cards page on the 252 Project website (https://members.252project.co.il/cards/). It includes functionality to log in, apply filters (gender and age range), scroll down to load all cards, and click the "View" button on each card to access details pages (where you can add your custom data extraction logic).

## Installation

1. **Install Python:** Make sure you have Python 3.x installed on your system.
2. **Install Dependencies:**  Create a virtual environment (recommended) and install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. **ChromeDriver:** Download the ChromeDriver executable that matches your Chrome browser version from the official website: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).
4. **Set ChromeDriver Path:**
    - **Add to PATH (Recommended):** Extract the ChromeDriver executable to a directory and add that directory to your system's PATH environment variable. 
    - **Set in Code (Alternative):** Update the `chromedriver_path` variable in `app.py` to the full path of the ChromeDriver executable.

## Usage

1. **Environment Variables:**
   - Create a `.env` file in the project root directory and add the following variables, replacing placeholders with your actual values:

     ```
     MEMBERS_URL=https://members.252project.co.il/
     LOGIN_URL=https://members.252project.co.il/login/
     CARDS_URL=https://members.252project.co.il/cards/
     USERNAME=your_username
     PASSWORD=your_password
     ```

2. **Run the Script:**
   - From the project root directory, run the following command:

     ```bash
     python app.py
     ```

## Customization

- **`xpaths.py`:** Update the XPaths in this file if the website structure changes.
- **`cards.py`:**
    - **`apply_filters()`:** Modify the filter criteria (gender, age range) as needed.
    - **`process_cards()`:** Add your custom code for extracting data or interacting with elements on the individual card details pages within the `# --- Your actions in the new tab ---` section.

## Improvments

- **Headless Mode:**  Uncomment `chrome_options.add_argument("--headless")` in `app.py` to run the script in headless mode (without opening a visible browser window).
- **Robust Locators:** For long-term stability, try to use the most robust locators (IDs, unique class names) possible when identifying elements on the website.
- **Explicit Waits:** The code uses explicit waits (`WebDriverWait`) to ensure that elements are present and clickable before interacting with them. Adjust wait times if necessary to accommodate the website's loading speed.
- **Error Handling:** The script includes basic error handling to catch exceptions and log errors. Consider adding more specific error handling based on your needs.