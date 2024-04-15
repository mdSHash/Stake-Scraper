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
payload = "{\"query\":\"query highrollerSportBets($limit: Int!) {\\n  highrollerSportBets(limit: $limit) {\\n    id\\n    iid\\n    bet {\\n      __typename\\n      ... on SportBet {\\n        __typename\\n        id\\n        updatedAt\\n        createdAt\\n        potentialMultiplier\\n        amount\\n        currency\\n        user {\\n          id\\n          name\\n          preferenceHideBets\\n        }\\n        outcomes {\\n          id\\n          odds\\n          fixtureAbreviation\\n          fixtureName\\n          fixture {\\n            id\\n            tournament {\\n              id\\n              category {\\n                id\\n                sport {\\n                  id\\n                  slug\\n                }\\n              }\\n            }\\n          }\\n        }\\n      }\\n    }\\n  }\\n}\\n\",\"variables\":{\"limit\":40}}"
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,ar-EG;q=0.6,ar;q=0.5',
  'access-control-allow-origin': '*',
  'content-type': 'application/json',
  'cookie': 'currency_currency=btc; currency_hideZeroBalances=false; currency_currencyView=crypto; session_info=undefined; fiat_number_format=en; casinoSearch=["Monopoly","Crazy Time","Sweet Bonanza","Money Train","Reactoonz"]; sportsSearch=["Liverpool FC","Kansas City Chiefs","Los Angeles Lakers","FC Barcelona","FC Bayern Munich"]; sportMarketGroupMap={}; oddsFormat=decimal; _ga=GA1.1.1484616581.1711994775; intercom-id-cx1ywgf2=7e7edf06-759d-416f-a024-a3e48da766f1; intercom-session-cx1ywgf2=; intercom-device-id-cx1ywgf2=c8665743-edd5-4317-af93-aef41f804553; g_state={"i_p":1712428871075,"i_l":2}; cookie_consent=true; locale=en; sidebarView=hidden; cf_clearance=MSdechxfNmYCzgSWRVLJKG9Goa9hXErk9EygjkRqK8A-1712936634-1.0.1.1-iZxJlkTr.cu2Rc6SMImcCloVt.q7LACUo.00hVh3.ZtCxFM7GAgVIu8b3WvsTf94yqeE3QP4bZMMsUsh8RctXg; leftSidebarView_v2=expanded; __cf_bm=dCgM7AniLRTUGvTRnOz8CEieUgA4kWXZhaYa90xJho4-1712951860-1.0.1.1-15w6x2SoqqgCU46J4j_BswWQoKbtt0JMXwVxs1ce54iHD9au6BRx0khAiglAuUZyqlhY5bZfw7MjApzdmPKq5A; mp_e29e8d653fb046aa5a7d7b151ecf6f99_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18e9ad72674a16-016709195fcde5-26001a51-1aeaa0-18e9ad72674a16%22%2C%22%24device_id%22%3A%20%2218e9ad72674a16-016709195fcde5-26001a51-1aeaa0-18e9ad72674a16%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _ga_TWGX3QNXGG=GS1.1.1712952043.6.1.1712952063.0.0.0; __cf_bm=HFeAD6ZT9CDPJ5SrquKkiLyiUjWUiRHQWBF5RvFS9uc-1712951760-1.0.1.1-XXk6lkL12s1Trf68CCa9Djqutga6OUUq3bR7R3ue5d2hfPsPn_1CTvC.2404ZyB14_H7bQ1n8BTm58H5.UmFCw',
  'origin': 'https://stake.com',
  'referer': 'https://stake.com/sports/tennis',
  'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
  'sec-ch-ua-arch': '"x86"',
  'sec-ch-ua-bitness': '"64"',
  'sec-ch-ua-full-version': '"123.0.6312.107"',
  'sec-ch-ua-full-version-list': '"Google Chrome";v="123.0.6312.107", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.107"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-model': '""',
  'sec-ch-ua-platform': '"Windows"',
  'sec-ch-ua-platform-version': '"10.0.0"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
  'x-language': 'en'
}

# Define CSV file header
csv_header = ['Odds', 'CreatedAt', 'UpdatedAt', 'Betting Amount', 'Currency', 'Value (USD)', 'Actual Payout', 'Fixture Name', 'Sport']

# Track IDs of fetched bets
fetched_bet_ids = set()

while True:
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        bets = data['data']['highrollerSportBets']
        
        with open('Tennis_Bets.csv', 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_header)
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
        print("waitng before featching any new data")
        time.sleep(15)  # Sleep for 15 seconds
    except Exception as e:
        print(f"An error occurred: {e}")
