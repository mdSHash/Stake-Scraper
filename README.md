# Stake-Scraper
Scraping the High Rollers Tennis bets

## Overview
This project consists of two Python scripts to scrape data from the Stake website using GraphQL API and Flask to serve the scraped data via a RESTful API. The first script (`stake_scraper.py`) continuously fetches betting data, converts currency, and stores it in a CSV file. The second script (`app.py`) creates a Flask web server to serve the scraped data.

## Requirements
- Python 3.x
- Libraries: requests, bs4 (BeautifulSoup), Flask

## Installation
1. Clone the repository:
  git clone https://github.com/mdSHash/Stake-Scraper
  cd Stake-Scraper

2. Install dependencies:
  pip install -r requirements.txt

## Usage
1. Run the `stake_scraper.py` script to continuously fetch and store data:
  python stake_scraper.py

2. Run the `app.py` script to start the Flask server:
  python app.py

3. Access the API endpoint to get the scraped data:
  http://localhost:5000/api/data

## Notes
- Ensure that you have proper internet connectivity to scrape data from the Stake website.
- The CSV file (`Tennis_Bets.csv`) will be continuously updated with new data.
- Adjust the scraping interval and other parameters as needed.
