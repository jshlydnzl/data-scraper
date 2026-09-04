# 🕸️ Dynamic Web Data Scraper

[![Vibe Coded](https://img.shields.io/badge/Vibe%20Coded-AI%20Assisted-purple)](https://github.com/jshlydnzl)

An automated Python web scraper designed to extract raw data from websites and turn it into a structured CSV file for Excel data cleaning practice.

*(Note: While some might label this an "ETL Pipeline", it is fundamentally a highly efficient, automated web scraping script built to generate datasets for my daily Data Analytics practice!)*

This project was intentionally **Vibe Coded** (AI-assisted engineered) to demonstrate modern automation workflows and rapid script development.

---

## 🛠️ How it Works: The "Config Zone"
Instead of hardcoding the scraper for one specific website, this script is built with a dynamic **Configuration Zone** at the top of the file. By simply inspecting a website's HTML (Right Click -> Inspect), you can change a few variables to scrape entirely different websites without rewriting the core Python logic!

### Example: Scraping a Bookstore
If you want to scrape books instead of quotes, just change these variables at the top of `data_scraper.py`:

```python
TARGET_URL = "http://books.toscrape.com/"

# The HTML container that holds one single item (like one book)
CONTAINER_TAG = 'article'
CONTAINER_CLASS = 'product_pod'

# The specific data points you want to pull from inside that container
DATA_POINTS = {
    "Book Title": ("h3", ""),
    "Price": ("p", "price_color")
}
```

The script will automatically adapt to the new website, loop through the HTML, and generate a fresh CSV with "Book Title" and "Price" columns!

---

## 🏗️ Architecture & Technologies
*   **Python 3 & Pandas:** Formats the extracted data into structured rows/columns and exports it as an analysis-ready `.csv`.
*   **Selenium & GeckoDriver:** Uses a headless Firefox browser to bypass basic anti-bot mechanisms and load JavaScript-rendered HTML.
*   **BeautifulSoup4:** Parses the DOM dynamically based on your custom configuration.
*   **Linux Cron Jobs:** Acts as a local automation engine. A cron job (`@reboot`) silently executes the scraper in the background every time the laptop boots up, ensuring fresh data is always waiting for daily analysis.

---

## 🚀 Quick Start

**1. Install Dependencies** 
Make sure your virtual environment is active, then install the required tools:
```bash
pip install pandas selenium webdriver-manager beautifulsoup4
```

**2. Run the Scraper** 
Execute the script from your terminal:
```bash
python data_scraper.py
```

**3. Analyze Your Data** 
A file named `unclean_data.csv` will be automatically generated. You can then load this into Excel to practice Data Cleaning (TRIM, XLOOKUP, Pivot Tables), or run it through the `ullr` CLI to audit the data quality!
