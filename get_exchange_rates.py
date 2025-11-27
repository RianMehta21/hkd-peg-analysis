import requests
import pandas as pd
import time
from datetime import datetime

def fetch_exchange_rate_data(offset, pagesize):
    url = f"https://api.hkma.gov.hk/public/market-data-and-statistics/monthly-statistical-bulletin/er-ir/er-eeri-daily?offset={offset}&pagesize={pagesize}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(f"fetched offset: {offset}, pagesize: {pagesize}")
    return data

def fetch_all_data():
    all_data = []
    offset = 0
    pagesize = 1000
    while True:
        data_chunk = fetch_exchange_rate_data(offset, pagesize)["result"]["records"]
        print(type(data_chunk))
        if not data_chunk:
            break
        all_data.extend(data_chunk)
        offset += pagesize
        time.sleep(1)
        print(f"total fetched: {len(all_data)}")
    return all_data

def save_to_csv(data, filename='hkd_usd_exchange_rates.csv'):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['end_of_day'])
    df = df.sort_values(by='date')
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    data = fetch_all_data()
    save_to_csv(data)