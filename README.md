# Automated Web ETL Pipeline

## Overview
This repository contains a miniature ETL (Extract, Transform, Load) pipeline built in Python. It is designed to automate the collection of unstructured web data and transform it into a clean, structured format (CSV) ready for immediate Exploratory Data Analysis (EDA) or dashboarding.

## Pipeline Architecture
1. **Extract:** Uses a headless Firefox browser controlled by Selenium to bypass basic anti-bot mechanisms and capture fully rendered HTML.
2. **Transform:** Leverages `BeautifulSoup` to parse the DOM and extract specific data nodes. It then uses `pandas` to clean the text (removing rogue characters and whitespace) and format it into rows and columns.
3. **Load:** Exports the structured DataFrame into an analysis-ready `.csv` file, the gold standard for analytics tools like Tableau, PowerBI, or Excel.

## Technologies Used
* **Python 3**
* **Pandas** (Data cleaning, DataFrame structuring, CSV export)
* **Selenium & GeckoDriver** (Headless browser automation)
* **BeautifulSoup4** (HTML parsing)

## How to Run It
1. Ensure your virtual environment is active and dependencies (`pandas`, `selenium`, `beautifulsoup4`) are installed.
2. Run the pipeline:
   ```bash
   python data_scraper.py
   ```
3. The script will output a clean `analytics_ready.csv` file in the root directory.
