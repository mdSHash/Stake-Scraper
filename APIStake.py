from fastapi import FastAPI
from typing import List
import csv

app = FastAPI()

# Define route to fetch data
@app.get('/api/data')
async def get_data():
    data = []
    # Read data from CSV file
    with open('Tennis_Bets.csv', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)  # Convert reader to list of dictionaries
    return data
