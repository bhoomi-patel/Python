# Selenium = Controls real web browsers programmatically
# JavaScript handling - scrapes content loaded dynamically
# User interactions - click buttons, fill forms, scroll pages

# Memory Trick: Selenium = Selects Elements through Navigation In User Mode!

'''pip install selenium
# Also need to install ChromeDriver or use webdriver-manager
pip install webdriver-manager'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def setup_driver():
    """Setup Chrome driver with options"""
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Run in background , Runs Chrome without opening a visible window (useful for background scraping)
    options.add_argument('--no-sandbox') # Avoids permission issues
    options.add_argument('--disable-dev-shm-usage') # Fixes memory sharing issues on Linux/Windows
    
    # Properly setup ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Initialize driver
driver = setup_driver()

try:
    # Navigate to target page
    driver.get("https://quotes.toscrape.com/js/")  # JS-heavy site

    # Wait until quotes are loaded
    wait = WebDriverWait(driver, 10)
    quotes = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))

    # Extract text and author
    for quote in quotes[:3]:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text
        print(f"'{text}' - {author}")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()  # Always close the browser


''' advanced selenium features'''
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
def selenium_scraping():
    driver=setup_driver()

    try:
        driver.get("https://example.com")

        # 1-fill form
        search_box=driver.find_element(By.NAME,"search")
        search_box.send_keys("Python programming")
        search_box.send_keys(Keys.RETURN)

        # 2- click button
        button = driver.find_element(By.ID,"submit-btn")
        button.click()
    
        # 3 - scroll page
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)

        # 4 - wait for dynamic content
        wait = WebDriverWait(driver,10)
        dynamic_content = wait.until (EC.presence_of_all_elements_located((By.CLASS_NAME,"dynamic-content")))

        # 5 - handle multiple windows/tabs
        original_window = driver.current_window_handle
        driver.execute_script("window.open('https://example2.com','_blank');")
        driver.switch_to.window(driver.window_handles[-1]) # switch to new tab

        # do something in new tab
        driver.close() # close current tab
        driver.switch_to.window(original_window) # switch back

        # take screenshot
        driver.save_screenshot("page_ss.png")

    finally:
        driver.quit() # 