# **ETL Python Scripts for Crypto Market Data Analysis**

## Overview
This project comprises a suite of three Python scripts, each tailored for specific aspects of data handling and analysis in the realm of cryptocurrency markets. The scripts are designed with reusability and scalability in mind, making them ideal for both educational purposes and practical applications in data science and financial analysis.

## 1. API2CSV: Data Extraction and Transformation
**Functionality**: This script efficiently interfaces with cryptocurrency market APIs to fetch and store historical market data. 

**Features**:
  - Retrieves five years of historical price data for Solana (SOL) against USD (SolUsd).
  - Converts and saves the data into a CSV format.
  - Target directory: `C:\temp` for easy access and management.

**Use Case**: Ideal for analysts requiring historical data for backtesting trading strategies, studying market trends, or conducting financial research.

## 2. CSV2Database: Data Integration
**Functionality**: Seamlessly integrates CSV data into a relational database system.

**Features**:
  - Automates the process of importing CSV files.
  - Compatible with PostgreSQL, a robust and widely-used SQL database.
  - Ensures data integrity and efficient storage.

**Use Case**: Perfect for database administrators and data engineers looking to incorporate flat-file data into SQL databases for complex querying and data management.

## 3. CSV2Visualizations: Data Visualization
**Functionality**: Transforms data into insightful visual representations.

**Features**:
  - Generates visualizations focusing on price action, market volatility, and trading volume.
  - Offers customizable visualization options to cater to specific analytical needs.

**Use Case**: Designed for data analysts and financial experts interested in visualizing market dynamics and identifying patterns in cryptocurrency markets.

## 4. ExecuteYourScriptsWeekly.ps1: Automation for Windows Users
**Functionality**: Automates the weekly execution of the ETL (Extract, Transform, Load) process in Windows environments.

**Features**:
  - Schedules and runs the API2CSV, CSV2Database, and CSV2Visualizations scripts on a weekly basis.
  - Customizable parameters through Windows Task Scheduler to fit individual requirements.
  - Facilitates consistent and timely data extraction and processing without manual intervention.

**Use Case**: Ideal for users who need to regularly update their database with the latest market data and generate updated visualizations without manual effort.

## Technical Stack
- **Languages**: Python
- **Libraries/Frameworks**: Pandas for data manipulation, Matplotlib/Seaborn for visualization, psycopg2 for PostgreSQL integration
- **APIs**: [Bitstamp API](https://www.bitstamp.net/api/v2)
- **Database**: PostgreSQL
- **Visualization Tools**: Matplotlib

## Getting Started
Follow these steps to set up and run the ETL Python scripts:

1. **Prerequisites**:
   - Ensure you have Python installed on your system.
   - Install necessary Python libraries: Pandas, Matplotlib/Seaborn, psycopg2.
   - Set up a PostgreSQL database instance for CSV2Database.

2. **Data Retrieval**:
   - Run the API2CSV script to fetch data from the Bitstamp API.
   - The script will retrieve five years of Solana (SOL) price data and store it in a CSV file in the `C:\temp` directory.

3. **Data Processing**:
   - After retrieving and storing data in CSV format, choose your next action:
     - Run CSV2Database to import the data into a PostgreSQL database.
     - Run CSV2Visualizations to create visualizations for volume, volatility, or price action.

Each script is designed to be standalone, allowing flexibility in how you process and analyze the data.

## Contribution and Customization
This project is open for contributions and can be easily customized to suit various data extraction, transformation, and loading (ETL) needs in different domains. Feel free to fork, modify, and use these scripts as a foundation for your data processing tasks.
