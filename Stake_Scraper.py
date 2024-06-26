import requests
import json
import csv
from bs4 import BeautifulSoup
import time

def scrape_final_converted_value(amount, from_currency):
    """
        Scrape final converted value from xe.com and convert it to USD.

        Parameters:
            amount (float): Amount of currency to convert.
            from_currency (str): Currency code to convert from.

        Returns:
            str: Final converted value in USD.
    """
    if from_currency.upper() in ["USDT", "USDC"]:
        return amount
    url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={from_currency}&To=USD"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            final_value_paragraph = soup.find('p', class_='sc-1c293993-1 fxoXHw')
            if final_value_paragraph:
                final_value_text = final_value_paragraph.text.strip()
                # Extracting the final converted value
                final_value = final_value_text.split()[0].replace(',', '')
                return final_value
            else:
                print("Final value paragraph not found in the HTML.")
                return None
        else:
            print(f"Failed to get exchange rate for {from_currency} to USD of Amount {amount}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while scraping final converted value: {e}")
        return None

url = "https://stake.com/_api/graphql"

# Define the updated cookies and headers

cookies = {
    'cf_chl_3': '7c7d266e66720bf',
    '__cf_bm': 'vrp9e5sIoBFt64hsgrwq1u0UScyRPx6miinglm9b13c-1713488413-1.0.1.1-PWbVJjdeJbUtJLcLqZqvEQ2g5IstD_iSGfbCAInEffnqFKKQ09JbUV.eI_oXxefB3PStHWzPsEj9gXfIRB.DPw',
    'currency_currency': 'btc',
    'currency_hideZeroBalances': 'false',
    'currency_currencyView': 'crypto',
    'session_info': 'undefined',
    'fiat_number_format': 'en',
    'leftSidebarView_v2': 'expanded',
    'sidebarView': 'hidden',
    'casinoSearch': '["Monopoly","Crazy Time","Sweet Bonanza","Money Train","Reactoonz"]',
    'sportsSearch': '["Liverpool FC","Kansas City Chiefs","Los Angeles Lakers","FC Barcelona","FC Bayern Munich"]',
    'sportMarketGroupMap': '{}',
    'oddsFormat': 'decimal',
    'cf_clearance': 'T9HUNNEmWJd2cDvqk5tbwGtJksVq0mvlPwy_l6lnWWo-1713488415-1.0.1.1-GzojYnzOX5U9F6Ga4pe6jztxJjYZacty2IKgOLLE.BfSCqJbYKEgPKKH5Ht55lnxBumcQwnA2ZbNXr89CbaJ6g',
    'locale': 'en',
    'mp_e29e8d653fb046aa5a7d7b151ecf6f99_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18ef3de3ab68d4-06348d5e2c94d5-26001a51-1aeaa0-18ef3de3ab68d4%22%2C%22%24device_id%22%3A%20%2218ef3de3ab68d4-06348d5e2c94d5-26001a51-1aeaa0-18ef3de3ab68d4%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fstake.com%2Fsports%2Fhome%3F__cf_chl_tk%3DmeYKA8xYiwZ4pxA2WGrIGAU6RKjKwYF35MpBskjM56s-1713488410-0.0.1.1-1578%22%2C%22%24initial_referring_domain%22%3A%20%22stake.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fstake.com%2Fsports%2Fhome%3F__cf_chl_tk%3DmeYKA8xYiwZ4pxA2WGrIGAU6RKjKwYF35MpBskjM56s-1713488410-0.0.1.1-1578%22%2C%22%24initial_referring_domain%22%3A%20%22stake.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D',
    '_ga': 'GA1.1.666642434.1713488411',
    '_ga_TWGX3QNXGG': 'GS1.1.1713488411.1.0.1713488411.0.0.0',
    'intercom-id-cx1ywgf2': '92e9305e-cb92-4886-b9a5-1c17f8c044fc',
    'intercom-session-cx1ywgf2': '',
    'intercom-device-id-cx1ywgf2': '94df984a-52ff-450f-85b0-491f4fb74b14',
    'cookie_consent': 'true',
    '_dd_s': '',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,ar-EG;q=0.6,ar;q=0.5',
    'access-control-allow-origin': '*',
    'content-type': 'application/json',
    # 'cookie': 'cf_chl_3=7c7d266e66720bf; __cf_bm=vrp9e5sIoBFt64hsgrwq1u0UScyRPx6miinglm9b13c-1713488413-1.0.1.1-PWbVJjdeJbUtJLcLqZqvEQ2g5IstD_iSGfbCAInEffnqFKKQ09JbUV.eI_oXxefB3PStHWzPsEj9gXfIRB.DPw; currency_currency=btc; currency_hideZeroBalances=false; currency_currencyView=crypto; session_info=undefined; fiat_number_format=en; leftSidebarView_v2=expanded; sidebarView=hidden; casinoSearch=["Monopoly","Crazy Time","Sweet Bonanza","Money Train","Reactoonz"]; sportsSearch=["Liverpool FC","Kansas City Chiefs","Los Angeles Lakers","FC Barcelona","FC Bayern Munich"]; sportMarketGroupMap={}; oddsFormat=decimal; cf_clearance=T9HUNNEmWJd2cDvqk5tbwGtJksVq0mvlPwy_l6lnWWo-1713488415-1.0.1.1-GzojYnzOX5U9F6Ga4pe6jztxJjYZacty2IKgOLLE.BfSCqJbYKEgPKKH5Ht55lnxBumcQwnA2ZbNXr89CbaJ6g; locale=en; mp_e29e8d653fb046aa5a7d7b151ecf6f99_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18ef3de3ab68d4-06348d5e2c94d5-26001a51-1aeaa0-18ef3de3ab68d4%22%2C%22%24device_id%22%3A%20%2218ef3de3ab68d4-06348d5e2c94d5-26001a51-1aeaa0-18ef3de3ab68d4%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fstake.com%2Fsports%2Fhome%3F__cf_chl_tk%3DmeYKA8xYiwZ4pxA2WGrIGAU6RKjKwYF35MpBskjM56s-1713488410-0.0.1.1-1578%22%2C%22%24initial_referring_domain%22%3A%20%22stake.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fstake.com%2Fsports%2Fhome%3F__cf_chl_tk%3DmeYKA8xYiwZ4pxA2WGrIGAU6RKjKwYF35MpBskjM56s-1713488410-0.0.1.1-1578%22%2C%22%24initial_referring_domain%22%3A%20%22stake.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _ga=GA1.1.666642434.1713488411; _ga_TWGX3QNXGG=GS1.1.1713488411.1.0.1713488411.0.0.0; intercom-id-cx1ywgf2=92e9305e-cb92-4886-b9a5-1c17f8c044fc; intercom-session-cx1ywgf2=; intercom-device-id-cx1ywgf2=94df984a-52ff-450f-85b0-491f4fb74b14; cookie_consent=true; _dd_s=',
    'origin': 'https://stake.com',
    'referer': 'https://stake.com/sports/home',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"123.0.6312.124"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="123.0.6312.124", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.124"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-language': 'en',
}

json_data = {
    'query': 'query highrollerSportBets($limit: Int!) {\n  highrollerSportBets(limit: $limit) {\n    id\n    iid\n    bet {\n      ...BetsBoardSports_BetBet\n    }\n  }\n}\n\nfragment BetsBoardSports_BetBet on BetBet {\n  __typename\n  ... on SwishBet {\n    __typename\n    id\n    updatedAt\n    createdAt\n    potentialMultiplier\n    amount\n    currency\n    user {\n      id\n      name\n    }\n    outcomes {\n      __typename\n      id\n      odds\n      outcome {\n        __typename\n        id\n        market {\n          id\n          competitor {\n            name\n          }\n          game {\n            id\n            fixture {\n              id\n              tournament {\n                id\n                category {\n                  id\n                  sport {\n                    id\n                    slug\n                  }\n                }\n              }\n            }\n          }\n        }\n      }\n    }\n  }\n  ... on SportBet {\n    __typename\n    id\n    updatedAt\n    createdAt\n    potentialMultiplier\n    amount\n    currency\n    user {\n      id\n      name\n    }\n    outcomes {\n      id\n      odds\n      fixtureAbreviation\n      fixtureName\n      fixture {\n        id\n        tournament {\n          id\n          category {\n            id\n            sport {\n              id\n              slug\n            }\n          }\n        }\n      }\n    }\n  }\n  ... on RacingBet {\n    __typename\n    id\n    updatedAt\n    createdAt\n    betPotentialMultiplier: potentialMultiplier\n    amount\n    currency\n    betStatus: status\n    payoutMultiplier\n    adjustments {\n      payoutMultiplier\n    }\n    user {\n      id\n      name\n    }\n    outcomes {\n      id\n      type\n      derivativeType\n      prices {\n        odds\n      }\n      event {\n        meeting {\n          racing {\n            slug\n          }\n        }\n      }\n      selectionSlots {\n        runners {\n          name\n        }\n      }\n    }\n  }\n}\n',
    'variables': {
        'limit': 10,
    },
}

# Define CSV file header
csv_header = ['Odds', 'CreatedAt', 'UpdatedAt', 'Betting Amount', 'Currency', 'Value (USD)', 'Actual Payout', 'Fixture Name', 'Sport']

# Track IDs of fetched bets
fetched_bet_ids = set()

while True:
    try:
        response = requests.request("POST", url, headers=headers, cookies=cookies, json=json_data)
        data = json.loads(response.text)
        bets = data['data']['highrollerSportBets']
        
        with open('Tennis_Bets.csv', 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_header)
            if csv_file.tell() == 0:
                writer.writeheader()
            for bet in bets:
                bet_id = bet['id']
                if bet_id not in fetched_bet_ids:
                    fetched_bet_ids.add(bet_id)
                    if 'outcomes' in bet['bet']:
                        for outcome in bet['bet']['outcomes']:
                            slug = outcome['fixture']['tournament']['category']['sport']['slug']
                            if slug == "tennis":
                                amount = bet['bet']['amount']
                                from_currency = bet['bet']['currency'].upper()  # Convert to uppercase
                                # Convert currency using scraping
                                total_usd = scrape_final_converted_value(amount, from_currency)
                                Actual_Payout =  (float(total_usd) * float(outcome['odds'])) 
                                if total_usd is not None:
                                    row = {
                                        'Odds': outcome['odds'],
                                        'CreatedAt': bet['bet']['createdAt'],
                                        'UpdatedAt': bet['bet']['updatedAt'],
                                        'Betting Amount': bet['bet']['amount'],
                                        'Currency': bet['bet']['currency'],
                                        'Value (USD)': total_usd,  # Add converted value here
                                        'Actual Payout': Actual_Payout,
                                        'Fixture Name': outcome['fixtureName'],
                                        'Sport': slug
                                    }
                                    writer.writerow(row)
                                    print(row)
                                    print("feching done")
        
        # Add a delay before making the next request
        print("______________________________________________")
        print("waiting before fetching any new data")
        time.sleep(15)  # Sleep for 15 seconds
    except Exception as e:
        print(f"An error occurred: {e}")
