# Scraper

A simple, general-purpose Python web scraper. You can use this to grab visible text from public webpages (like job postings, articles, etc.) and save it into a clean JSON format. 

## How to use

1. Open your terminal in this directory.
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the scraper and point it at a URL:
   ```bash
   python scrape.py https://example.com/some-page
   ```
4. The extracted text will be saved in `scraped_data.json`.

---

## ⚠️ THE CATCH (READ THIS BEFORE YOU GO WILD) ⚠️

While scraping public data is generally legal, **websites absolutely hate it.** 

If you use this script to aggressively scrape large corporate sites like Indeed, LinkedIn, or Jobstreet in a loop, here is what will happen:
1. **You will get IP Banned:** Big sites use protections like Cloudflare. If you send too many requests too fast, they will block your IP address, meaning you can't even visit their site normally.
2. **You will get CAPTCHAs:** You might start seeing "Verify you are human" checks constantly.
3. **Terms of Service:** You are likely violating the site's Terms of Service. 

### Best Practices for not getting banned:
- **Be Polite:** This script includes a built-in 2-second delay (`time.sleep(2)`). **Do not remove this** if you are running the script in a loop.
- **Don't spam:** Do not run this on thousands of pages a minute. It will crash small servers and get you banned on large ones.
- **Use APIs:** If a website offers an official API (Application Programming Interface), always use that instead of scraping!

**Disclaimer:** The creator of this script is not responsible for your IP getting banned, your computer getting angry, or you violating any website's Terms of Service. Use responsibly!
