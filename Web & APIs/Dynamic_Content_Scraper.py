import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time 

class DynamicScraper:
    """Scraper for JavaScript-heavy websites"""
    
    def __init__(self, headless=False):
        self.driver = self.setup_driver(headless)
        
    def setup_driver(self, headless):
        """Setup Chrome driver with options"""
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)
    
    def scrape_infinite_scroll(self, url, max_scrolls=5):
        """Scrape content from infinite scroll pages"""
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 10)
        
        all_items = []
        
        for scroll in range(max_scrolls):
            # Wait for content to load
            try:
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))
            except:
                break
            
            # Get current items
            items = self.driver.find_elements(By.CLASS_NAME, "quote")
            
            for item in items:
                try:
                    text = item.find_element(By.CLASS_NAME, "text").text
                    author = item.find_element(By.CLASS_NAME, "author").text
                    
                    item_data = {
                        'text': text,
                        'author': author,
                        'scroll_level': scroll + 1
                    }
                    
                    if item_data not in all_items:
                        all_items.append(item_data)
                        
                except Exception as e:
                    continue
            
            # Scroll to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for new content
            
            print(f"Scroll {scroll + 1}: Found {len(all_items)} total items")
        
        return all_items
    
    def scrape_spa_content(self, url, navigation_steps):
        """Scrape Single Page Application content"""
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 10)
        
        results = {}
        
        for step_name, step_config in navigation_steps.items():
            try:
                # Click navigation element
                nav_element = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, step_config['selector']))
                )
                nav_element.click()
                
                # Wait for content to load
                content_elements = wait.until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, step_config['content_selector']))
                )
                
                # Extract content
                step_data = []
                for element in content_elements:
                    step_data.append(element.text)
                
                results[step_name] = step_data
                
            except Exception as e:
                print(f"Error in step {step_name}: {e}")
                results[step_name] = []
        
        return results
    
    def close(self):
        """Close the browser"""
        self.driver.quit()

# Usage example
def demo_dynamic_scraping():
    """Demo dynamic content scraping"""
    scraper = DynamicScraper(headless=False)
    
    try:
        # Scrape infinite scroll content
        print("Scraping infinite scroll content...")
        quotes = scraper.scrape_infinite_scroll("https://quotes.toscrape.com/js/", max_scrolls=3)
        
        print(f"Scraped {len(quotes)} quotes")
        for quote in quotes[:3]:
            print(f"  '{quote['text'][:50]}...' - {quote['author']}")
        
    finally:
        scraper.close()

# Run demo
demo_dynamic_scraping()


# simple code
'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import json

def setup_driver():
    """Setup Chrome driver with options"""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in background
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Basic usage
driver = setup_driver()

try:
    driver.get("https://quotes.toscrape.com/js/")  # JavaScript-heavy version
    wait = WebDriverWait(driver, 10)
    quotes = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))

    # Store data
    data = []

    for quote in quotes[:3]:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text
        data.append({"text": text, "author": author})

    # Save all quotes to a JSON file
    with open("quotes.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Data saved to quotes.json successfully!")

finally:
    driver.quit()'''


