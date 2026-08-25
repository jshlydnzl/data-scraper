import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# ==========================================
# ⚙️ CONFIGURATION ZONE (EDIT THIS SECTION!)
# ==========================================
# 1. The website you want to scrape
TARGET_URL = "http://quotes.toscrape.com/"

# 2. The main "Box" that holds each item (e.g., a product card, a job post)
CONTAINER_TAG = 'div'
CONTAINER_CLASS = 'quote'

# 3. The specific pieces of data you want from inside each box
# Format -> "Your Column Name": ("html_tag", "class_name")
DATA_POINTS = {
    "Quote Text": ("span", "text"),
    "Author Name": ("small", "author"),
}
# ==========================================


def scrape_structured_data(url):
    print(f"🚀 Launching Analytics Scraper for: {url}...")
    
    firefox_options = Options()
    firefox_options.add_argument("--headless") # Run invisibly in the background
    
    try:
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
        
        driver.get(url)
        time.sleep(2) # Give the website time to load
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # --- THE DATA ENGINEERING PART ---
        structured_data = []
        
        # Find all the main boxes on the page
        boxes = soup.find_all(CONTAINER_TAG, class_=CONTAINER_CLASS)
        
        for box in boxes:
            row = {}
            # Loop through the data points you configured above
            for column_name, (tag, css_class) in DATA_POINTS.items():
                element = box.find(tag, class_=css_class)
                # If the element exists, grab its text and remove weird quotation marks.
                clean_text = element.text.strip().replace('“', '').replace('”', '') if element else "N/A"
                row[column_name] = clean_text
                
            structured_data.append(row)
            
        driver.quit()
        return structured_data

    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    raw_data = scrape_structured_data(TARGET_URL)
    
    if raw_data:
        print(f"✅ Successfully extracted {len(raw_data)} structured rows!")
        
        # --- THE DATA ANALYTICS PART ---
        print("📊 Converting data to a Pandas DataFrame...")
        df = pd.DataFrame(raw_data)
        
        # Save to CSV (The gold standard for analytics and dashboards)
        csv_filename = "analytics_ready.csv"
        df.to_csv(csv_filename, index=False)
        print(f"💾 Saved perfectly structured data to {csv_filename}!")
        
        # Print a preview of the table
        print("\n--- DATA PREVIEW ---")
        print(df.head())
