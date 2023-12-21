import json
import pandas as pd
import requests
from datetime import datetime, timedelta

def get_historical_data(symbol, start, end):
    url = f"https://www.bitstamp.net/api/v2/ohlc/{symbol}/"
    params = {
        "step": 86400,  # Daily data, 86400 seconds in a day
        "limit": 1000,  # Maximum limit
        "start": int(start.timestamp()),
        "end": int(end.timestamp())
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return pd.DataFrame(response.json()['data']['ohlc'])
    else:
        return None

# Define the cryptocurrency symbol for Solana and the date range (last 5 years)
symbol = "solusd"  # Symbol for Solana in Bitstamp
end_date = datetime.now()
start_date = end_date - timedelta(days=5*365)  # Last 5 years

# Fetch historical data
historical_data = get_historical_data(symbol, start_date, end_date)

# Generate the file name with today's date
today = datetime.now().strftime("%Y-%m-%d")
file_path = rf"C:\temp\Solana_Historical_Data_{today}.csv"

# Save the data to a CSV file with the dynamically generated name
historical_data.to_csv(file_path, index=False)
