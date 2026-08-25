# Automated Web ETL Pipeline

## Overview
This repository contains a miniature ETL (Extract, Transform, Load) pipeline built in Python. It is designed to automate the collection of unstructured web data and transform it into a clean, structured format (CSV) ready for immediate Exploratory Data Analysis (EDA) or dashboarding.

## Note on the Placeholder Website
By default, this script is configured to scrape a safe, legal sandbox website (`quotes.toscrape.com`). This serves as a **placeholder** to demonstrate the ETL architecture without violating the Terms of Service of live production websites. 

You can easily adapt the `BeautifulSoup` selectors in the script to target your own websites for custom data extraction!

## Pipeline Architecture
1. **Extract:** Uses a headless Firefox browser controlled by Selenium to bypass basic anti-bot mechanisms and capture fully rendered HTML.
2. **Transform:** Leverages `BeautifulSoup` to parse the DOM and extract specific data nodes. It then uses `pandas` to clean the text (removing rogue characters and whitespace) and format it into rows and columns.
3. **Load:** Exports the structured DataFrame into an analysis-ready `.csv` file, the gold standard for analytics tools.

## Technologies Used
* **Python 3**
* **Pandas** (Data cleaning, DataFrame structuring, CSV export)
* **Selenium & GeckoDriver** (Headless browser automation)
* **BeautifulSoup4** (HTML parsing)

## Step-by-Step: How to Run It
Follow these steps to run the pipeline and generate your own dataset:

**1. Install Dependencies** 
Ensure your Python virtual environment is active, then install the required Data Engineering tools:
```bash
pip install pandas selenium webdriver-manager beautifulsoup4
```

**2. Run the Pipeline** 
Execute the script from your terminal:
```bash
python data_scraper.py
```

**3. The Extraction Process** 
The script will silently open a headless browser, navigate to the placeholder site, extract the raw HTML, and use Pandas to clean the data in the background.

**4. View your CSV** 
Once complete, a brand new file named `analytics_ready.csv` will automatically generate in your folder. This is your perfectly structured dataset, ready to be imported into Excel, Tableau, or PowerBI!
