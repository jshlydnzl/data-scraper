import argparse
import requests
from bs4 import BeautifulSoup
import time
import json

def scrape_url(url):
    print(f"Scraping: {url}...")
    # Using a standard browser user-agent so websites don't instantly block us as a bot
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # ⚠️ POLITE SCRAPING: Wait 2 seconds before requesting to avoid overloading servers
        time.sleep(2)
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Check for HTTP errors (like 404 or 403)
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.title.string.strip() if soup.title else 'No Title Found'
        
        # Remove script and style elements because we only care about visible text
        for script in soup(["script", "style"]):
            script.extract()
            
        # Get all text and clean it up
        text = soup.get_text(separator='\n')
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text_clean = '\n'.join(chunk for chunk in chunks if chunk)
        
        result = {
            "url": url,
            "title": title,
            # We save the first 2000 characters as a snippet, but you can change this to save the whole thing!
            "content": text_clean[:2000] + "\n...[Content Truncated]..."
        }
        
        return result

    except requests.exceptions.RequestException as e:
        print(f"❌ Error scraping {url}: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A polite and general web scraper.")
    parser.add_argument("url", help="The URL to scrape (e.g., https://example.com)")
    parser.add_argument("--output", "-o", help="Output JSON file name", default="scraped_data.json")
    
    args = parser.parse_args()
    
    data = scrape_url(args.url)
    if data:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"✅ Success! Data saved to {args.output}")
