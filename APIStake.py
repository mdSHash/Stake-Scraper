from flask import Flask, jsonify
import csv

app = Flask(__name__)

# Define route to fetch data
@app.route('/api/data')
def get_data():
    data = []
    # Read data from CSV file
    with open('Tennis_Bets.csv', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)  # Convert reader to list of dictionaries
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
