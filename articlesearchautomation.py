from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL to be accessed
url = "https://www.mendeley.com/search/"

# Set up Selenium WebDriver
options = webdriver.EdgeOptions()
options.use_chromium = True
driver = webdriver.Edge(options=options)

# Maximize browser Window
driver.maximize_window()


try:
    # Navigate to the URL
    driver.get(url)

    # Wait for the page and potential popups to load
    time.sleep(5)

    # Click on 'Accept all cookies' button
    try:
        accept_cookies_button = driver.find_element(
            By.ID, 'onetrust-accept-btn-handler')
        accept_cookies_button.click()
    except Exception as e:
        print(f"Could not find or click on 'Accept all cookies' button: {e}")

    time.sleep(10)  # An explicit wait

    # Navigate to sign-in & login
    sign_in_button = driver.find_element(
        By.XPATH, "//a[contains(@href, '/sign-in')]")
    sign_in_button.click()

    # An explicit wait
    time.sleep(5)

    # Login
    email_input = driver.find_element(By.ID, "bdd-email")
    # Mendeley account email address
    email_input.send_keys("email.example@email.com")
    continue_button = driver.find_element(By.ID, "bdd-elsPrimaryBtn")
    continue_button.click()

    # An explicit wait
    time.sleep(5)

    password_input = driver.find_element(By.ID, "bdd-password")
    # Mendeley account password
    password_input.send_keys("password")
    sign_in_button = driver.find_element(By.ID, "bdd-elsPrimaryBtn")
    sign_in_button.click()

   # An explicit wait
    time.sleep(10)

    # Input search term
    try:
        search_input = driver.find_element(By.ID, 'search-mendeley')
        search_input.send_keys(
            "swarm intelligence optimization in manufacturing")
    except Exception as e:
        print(f"Could not find the search box: {e}")

    # Click on the search button
    try:
        search_button = driver.find_element(
            By.XPATH, '//button[contains(@class, "qe-search-button") and @type="submit"]')
        search_button.click()
    except Exception as e:
        print(f"Could not find or click on the search button: {e}")

    # Keep the browser open for additional 10 seconds to observe actions
    time.sleep(10)

    # List of years to be selected
    years_to_select = ['2023', '2022', '2021', '2020', '2019']

    # Check the desired year checkboxes
    try:
        for year in years_to_select:
            # Find the label that contains the year
            year_checkbox_label = driver.find_element(
                By.XPATH, f"//label[contains(text(), '{year}')]")

            # Clicking the label toggles the checkbox
            year_checkbox_label.click()

            # Wait for a moment before selecting the next checkbox
            time.sleep(1)

    except Exception as e:
        print(f"Could not find or click a year checkbox: {e}")

    # Check the "Journal" document type checkbox
    try:
        # Find the label that contains the text 'Journal'
        journal_checkbox_label = driver.find_element(
            By.XPATH, "//label[contains(text(), 'Journal')]")

        # Clicking the label toggles the checkbox
        journal_checkbox_label.click()

    except Exception as e:
        print(f"Could not find or click the 'Journal' checkbox: {e}")

    # Keep the browser open for additional 10 seconds to observe actions
    time.sleep(10)

    # Interacting with search results
    count = 0
    while count < 30:
        # Check for 'Add to library' buttons and interact
        buttons = driver.find_elements(
            By.XPATH, "//button[contains(@class, 'qe-add-to-library')]")
        for button in buttons:
            if "Add to library" in button.text and count < 30:  # Replace with appropriate text
                button.click()
                count += 1
                time.sleep(1)  # Wait for the item to be added

        # Go to next page
        next_page_button = driver.find_element(
            By.XPATH, "//button[contains(@class, 'qe-next-page')]")
        next_page_button.click()

        # Allow page to load & replace with an explicit wait if possible
        time.sleep(5)

finally:
    # Close the driver when finished
    driver.close()
