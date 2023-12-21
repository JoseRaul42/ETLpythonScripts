import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from datetime import datetime

# Your PostgreSQL connection details
server = 'localhost'
database = 'SolanaHistorical'
username = 'postgres'  # Replace with your actual PostgreSQL username
password = ''  # Replace with your actual PostgreSQL password

# Create a connection string and engine
connection_string = f"postgresql://{username}:{password}@{server}/{database}"
engine = create_engine(connection_string)

# Generate today's date in yyyy-mm-dd format
today = datetime.now().strftime("%Y-%m-%d")

# Construct the file path with today's date
file_path = rf"C:\Temp\Solana_Historical_Data_{today}.csv"

# Load data from CSV
df = pd.read_csv(file_path)

# Write data into the database
df.to_sql('solana_historical_data', engine, if_exists='replace', index=False)
