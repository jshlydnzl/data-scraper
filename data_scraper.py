import time
import random
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# ==========================================
# ⚙️ CONFIGURATION ZONE (BOOKSTORE RANDOMIZER)
# ==========================================
# Pick a random page from 1 to 50 every morning!
random_page = random.randint(1, 50)
TARGET_URL = f"http://books.toscrape.com/catalogue/page-{random_page}.html"

# 2. The main "Box" that holds each book
CONTAINER_TAG = 'article'
CONTAINER_CLASS = 'product_pod'

# 3. The specific pieces of data you want
DATA_POINTS = {
    "Book_Title": ("h3", ""),
    "Price_GBP": ("p", "price_color"),
    "Availability": ("p", "instock availability")
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
            for column_name, (tag, css_class) in DATA_POINTS.items():
                if css_class == "":
                    element = box.find(tag)
                else:
                    element = box.find(tag, class_=css_class)
                
                # We leave some 'dirty' characters (like Â£ or In stock) so you can clean it in Excel!
                clean_text = element.text.strip() if element else "N/A"
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
        
        # Save to CSV
        csv_filename = "unclean_data.csv"
        df.to_csv(csv_filename, index=False)
        print(f"💾 Saved data to {csv_filename} for morning Data Cleaning practice!")
        
        print("\n--- DATA PREVIEW ---")
        print(df.head())
