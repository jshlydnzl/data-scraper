# Automated Web ETL Pipeline

## Overview
This repository contains a highly adaptable, generalized ETL (Extract, Transform, Load) pipeline built in Python. It is designed to automate the collection of unstructured web data from almost any website and transform it into a clean, structured format (CSV) ready for Exploratory Data Analysis (EDA) or dashboarding.

## How the Generalized Engine Works
Instead of hardcoding the scraper for one specific website, this script features a **Configuration Zone** at the top of the file. By simply inspecting a website's HTML in your browser (Right Click -> Inspect), you can change the configuration variables to extract whatever data you want without rewriting the core Python logic!

### Example: Scraping a Bookstore instead of Quotes
If you want to scrape books instead of quotes, you just open `data_scraper.py` and change the variables at the top:

```python
TARGET_URL = "http://books.toscrape.com/"

CONTAINER_TAG = 'article'
CONTAINER_CLASS = 'product_pod'

DATA_POINTS = {
    "Book Title": ("h3", ""),
    "Price": ("p", "price_color")
}
```
The script will automatically adapt to the new website, find all the books, and generate a new CSV with "Book Title" and "Price" columns!

## Pipeline Architecture
1. **Extract:** Uses a headless Firefox browser controlled by Selenium to bypass basic anti-bot mechanisms and capture fully rendered HTML.
2. **Transform:** Leverages `BeautifulSoup` to parse the DOM dynamically based on your configuration. It then uses `pandas` to format the extracted nodes into structured rows and columns.
3. **Load:** Exports the structured DataFrame into an analysis-ready `.csv` file.

## Technologies Used
* **Python 3**
* **Pandas** (Data cleaning, DataFrame structuring, CSV export)
* **Selenium & GeckoDriver** (Headless browser automation)
* **BeautifulSoup4** (HTML parsing)

## Step-by-Step: How to Run It

**1. Install Dependencies** 
Ensure your Python virtual environment is active, then install the required Data Engineering tools:
```bash
pip install pandas selenium webdriver-manager beautifulsoup4
```

**2. Customize the Configuration (Optional)** 
Open `data_scraper.py` in VS Code. Edit the `TARGET_URL`, `CONTAINER`, and `DATA_POINTS` variables at the top of the script to match the HTML skeleton of your target website.

**3. Run the Pipeline** 
Execute the script from your terminal:
```bash
python data_scraper.py
```

**4. View your CSV** 
Once complete, a brand new file named `analytics_ready.csv` will automatically generate. This is your perfectly structured dataset, ready to be imported into Excel, Tableau, or PowerBI!
