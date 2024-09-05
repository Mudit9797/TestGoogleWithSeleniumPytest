import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Fixture to initialize and close the browser
@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Required for some headless environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--disable-gpu")  # Optional: for better compatibility
    chrome_options.add_argument("start-maximized")  # Optional: start maximized

    service = Service('/home/vvdn30016/PycharmProjects/chromedriver for selenium/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.implicitly_wait(5)  # Wait up to 5 seconds for elements
    yield driver  # This is the setup part, the browser instance is returned here
    driver.quit()  # This is the teardown part, after the test is done, the browser is closed

# Test function for Google search
def test_google_search(browser):
    browser.get("https://google.com")

    # Assert that Google homepage is loaded
    assert "Google" in browser.title

    # Perform Google search
    search_box = browser.find_element(By.XPATH, "//*[@name='q']")
    search_box.send_keys("Python")
    time.sleep(2)  # Optional: wait for suggestions
    browser.find_element(By.XPATH, "(//input[@name='btnK'])[1]").click()

    # Assert that search results page loaded
    assert "Python" in browser.title

    counter = 1
    for i in range(1, 11):
        if i in range(5, 10):
            continue  # Skip results 5 to 9
        else:
            # Get the search result title
            result_text = browser.find_element(By.XPATH, f"(//h3[@class='LC20lb MBeuO DKV0Md'])[{i}]").text
            print(f'{counter}. {result_text}')
            assert result_text != ""  # Assert that result text is not empty
            counter += 1
            browser.execute_script("window.scrollBy(0, 100);")
            time.sleep(2)