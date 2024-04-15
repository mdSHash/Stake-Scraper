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
