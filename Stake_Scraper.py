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
import requests

cookies = {
    'cf_chl_3': '2efe7c380b0870b',
    '__cf_bm': 'qkKDhBagiLnEsX5MUGGlDsZYx2z8rADqrsZT2gXU0lc-1713409918-1.0.1.1-C6.VnOlgC6NLmL5XKbYuEA_7B5Lr98B.KhgvU.YfEFsCq5f_EAg5WpZXaiaYwRKHAzj6Gs5U4KHgB04ZSqjpKg',
    'currency_currency': 'btc',
    'currency_hideZeroBalances': 'false',
    'currency_currencyView': 'crypto',
    'fiat_number_format': 'en',
    'leftSidebarView_v2': 'expanded',
    'sidebarView': 'hidden',
    'casinoSearch': '["Monopoly","Crazy Time","Sweet Bonanza","Money Train","Reactoonz"]',
    'sportsSearch': '["Liverpool FC","Kansas City Chiefs","Los Angeles Lakers","FC Barcelona","FC Bayern Munich"]',
    'sportMarketGroupMap': '{}',
    'oddsFormat': 'decimal',
    'locale': 'en',
    'cf_clearance': 'Ng8iHMWbxamUhzlNAhhSJdWhh3FAHiyF4.oetAxslBI-1713409919-1.0.1.1-kOuR8as26SxjiTDw8145yllP7qB3eZyJ51hBRsh.peV5CTzDcLC8l7jPUDhj_Dxehj8UMJ7drf3sEwwunbzE8Q',
    '_ga': 'GA1.1.555245548.1713409917',
    'intercom-id-cx1ywgf2': '015046ce-b8cd-4001-b8f6-6f4625d05ea8',
    'intercom-device-id-cx1ywgf2': 'cc4e2d4a-adb7-4fca-9b7c-35a6f8ecfc0e',
    'cookie_consent': 'true',
    'session': '9014bcfd5c7c63790f41033cf42e83fcffe3e2aafbe5d0c24eb7a27f49be13caaf00b8cb19cb1d419aec3d10558d7cde',
    'session_info': '{"id":"fd585d4e-acba-4656-8c48-31678b85cb28","sessionName":"Chrome (Unknown)","ip":"41.45.4.79","country":"EG","city":"Giza","active":true,"updatedAt":"Thu, 18 Apr 2024 03:17:15 GMT","__typename":"UserSession"}',
    'mp_e29e8d653fb046aa5a7d7b151ecf6f99_mixpanel': '%7B%22distinct_id%22%3A%20%2239ccf22052999ee21fccddd535ecaa663abf51f1f45ec8e9196c41f556785a07%22%2C%22%24device_id%22%3A%20%2218eef30809d9f6-020b0ac0918968-26001a51-1aeaa0-18eef30809d9f6%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fstake.com%2Fsports%2Fhome%2Flive%2Ftennis%3F__cf_chl_tk%3DfMnNRCPy3YK_pzB04l_182UTfghO9BvrknBt6nIlNnU-1713409913-0.0.1.1-1621%22%2C%22%24initial_referring_domain%22%3A%20%22stake.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%2239ccf22052999ee21fccddd535ecaa663abf51f1f45ec8e9196c41f556785a07%22%7D',
    '_ga_TWGX3QNXGG': 'GS1.1.1713409917.1.1.1713410255.0.0.0',
    '_dd_s': 'rum=0&expire=1713411156854',
    'intercom-session-cx1ywgf2': 'bkFwaFNFZnFsMkt6SWxMM3ZnZko2WDhSMkhkRFZzSlM3b0pNTnRWT2xvMlgyMTZTSXpmL2ZIakhKUzVObEdoeC0tWUs3UHc1aXZCZFQxWFlONjEzZjlUQT09--fca582eb2bbb492b1f27f263d34d8e7e145610ac',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,ar-EG;q=0.6,ar;q=0.5',
    'access-control-allow-origin': '*',
    'content-type': 'application/json',
    # 'cookie': 'cf_chl_3=2efe7c380b0870b; __cf_bm=qkKDhBagiLnEsX5MUGGlDsZYx2z8rADqrsZT2gXU0lc-1713409918-1.0.1.1-C6.VnOlgC6NLmL5XKbYuEA_7B5Lr98B.KhgvU.YfEFsCq5f_EAg5WpZXaiaYwRKHAzj6Gs5U4KHgB04ZSqjpKg; currency_currency=btc; currency_hideZeroBalances=false; currency_currencyView=crypto; fiat_number_format=en; leftSidebarView_v2=expanded; sidebarView=hidden; casinoSearch=["Monopoly","Crazy Time","Sweet Bonanza","Money Train","Reactoonz"]; sportsSearch=["Liverpool FC","Kansas City Chiefs","Los Angeles Lakers","FC Barcelona","FC Bayern Munich"]; sportMarketGroupMap={}; oddsFormat=decimal; locale=en; cf_clearance=Ng8iHMWbxamUhzlNAhhSJdWhh3FAHiyF4.oetAxslBI-1713409919-1.0.1.1-kOuR8as26SxjiTDw8145yllP7qB3eZyJ51hBRsh.peV5CTzDcLC8l7jPUDhj_Dxehj8UMJ7drf3sEwwunbzE8Q; _ga=GA1.1.555245548.1713409917; intercom-id-cx1ywgf2=015046ce-b8cd-4001-b8f6-6f4625d05ea8; intercom-device-id-cx1ywgf2=cc4e2d4a-adb7-4fca-9b7c-35a6f8ecfc0e; cookie_consent=true; session=9014bcfd5c7c63790f41033cf42e83fcffe3e2aafbe5d0c24eb7a27f49be13caaf00b8cb19cb1d419aec3d10558d7cde; session_info={"id":"fd585d4e-acba-4656-8c48-31678b85cb28","sessionName":"Chrome (Unknown)","ip":"41.45.4.79","country":"EG","city":"Giza","active":true,"updatedAt":"Thu, 18 Apr 2024 03:17:15 GMT","__typename":"UserSession"}; mp_e29e8d653fb046aa5a7d7b151ecf6f99_mixpanel=%7B%22distinct_id%22%3A%20%2239ccf22052999ee21fccddd535ecaa663abf51f1f45ec8e9196c41f556785a07%22%2C%22%24device_id%22%3A%20%2218eef30809d9f6-020b0ac0918968-26001a51-1aeaa0-18eef30809d9f6%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fstake.com%2Fsports%2Fhome%2Flive%2Ftennis%3F__cf_chl_tk%3DfMnNRCPy3YK_pzB04l_182UTfghO9BvrknBt6nIlNnU-1713409913-0.0.1.1-1621%22%2C%22%24initial_referring_domain%22%3A%20%22stake.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%2239ccf22052999ee21fccddd535ecaa663abf51f1f45ec8e9196c41f556785a07%22%7D; _ga_TWGX3QNXGG=GS1.1.1713409917.1.1.1713410255.0.0.0; _dd_s=rum=0&expire=1713411156854; intercom-session-cx1ywgf2=bkFwaFNFZnFsMkt6SWxMM3ZnZko2WDhSMkhkRFZzSlM3b0pNTnRWT2xvMlgyMTZTSXpmL2ZIakhKUzVObEdoeC0tWUs3UHc1aXZCZFQxWFlONjEzZjlUQT09--fca582eb2bbb492b1f27f263d34d8e7e145610ac',
    'origin': 'https://stake.com',
    'referer': 'https://stake.com/sports/home/live/tennis',
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
    'x-access-token': '9014bcfd5c7c63790f41033cf42e83fcffe3e2aafbe5d0c24eb7a27f49be13caaf00b8cb19cb1d419aec3d10558d7cde',
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
