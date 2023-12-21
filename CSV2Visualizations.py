import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from datetime import datetime

# Set the style for dark background
plt.style.use('grayscale')
sns.set_palette("colorblind")

def read_and_process_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Convert timestamp to readable date format
    data['Date'] = pd.to_datetime(data['timestamp'], unit='s')

    # Calculate daily price volatility
    data['Volatility'] = data['high'] - data['low']

    return data

def plot_closing_price(data):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='close', data=data, label='Closing Price')
    plt.title('Closing Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def plot_trading_volume(data):
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Date', y='volume', data=data)
    plt.title('Trading Volume Trend')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.xticks(rotation=45)
    plt.show()

def plot_price_volatility(data):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Volatility', data=data, label='Daily Volatility')
    plt.title('Price Volatility')
    plt.xlabel('Date')
    plt.ylabel('Volatility (USD)')
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def main():
    # Generate today's date in yyyy-mm-dd format
    today = datetime.now().strftime("%Y-%m-%d")

    # Construct the file path with today's date
    file_path = rf"C:\Temp\Solana_Historical_Data_{today}.csv"
    

    data = read_and_process_data(file_path)
    
    plot_closing_price(data)
    plot_trading_volume(data)
    plot_price_volatility(data)

if __name__ == "__main__":
    main()
