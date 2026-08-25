import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

def scrape_structured_data(url):
    print(f"🚀 Launching Analytics Scraper for: {url}...")
    
    firefox_options = Options()
    # We run this one "headless" (invisible) so it runs super fast in the background
    firefox_options.add_argument("--headless") 
    
    try:
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
        
        driver.get(url)
        time.sleep(2) 
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # --- THE DATA ENGINEERING PART ---
        # Instead of grabbing ALL text, we hunt for specific HTML boxes
        structured_data = []
        
        # Find all HTML <div> boxes that have the class name "quote"
        quote_boxes = soup.find_all('div', class_='quote')
        
        for box in quote_boxes:
            # Extract specific pieces of data from inside each box
            text = box.find('span', class_='text').text.strip()
            author = box.find('small', class_='author').text.strip()
            
            # Put it into a structured dictionary (this represents one Excel Row)
            structured_data.append({
                "Author": author,
                "Quote": text
            })
            
        driver.quit()
        return structured_data

    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    url = "http://quotes.toscrape.com/"
    raw_data = scrape_structured_data(url)
    
    if raw_data:
        print(f"✅ Successfully extracted {len(raw_data)} structured rows!")
        
        # --- THE DATA ANALYTICS PART ---
        print("📊 Converting data to a Pandas DataFrame...")
        df = pd.DataFrame(raw_data)
        
        # Data Cleaning step: Let's remove the weird “ quotation marks from the text
        df['Quote'] = df['Quote'].str.replace('“', '').str.replace('”', '')
        
        # Save to CSV (The gold standard for analytics and dashboards)
        csv_filename = "analytics_ready.csv"
        df.to_csv(csv_filename, index=False)
        print(f"💾 Saved perfectly structured data to {csv_filename}!")
        
        # Print a preview of the table
        print("\n--- DATA PREVIEW ---")
        print(df.head())
