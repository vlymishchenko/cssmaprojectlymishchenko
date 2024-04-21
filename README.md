Unraveling the Dynamics: A Time Series Analysis of NFT Market Prices

This project focuses on extracting and analyzing NFT market price data to understand the dynamics of the Web3 market, 
particularly the STEPN platform which integrates cryptocurrency and NFTs in a unique Move-to-Earn model. 
The project utilizes various Python scripts, each tailored to handle different aspects of data collection and analysis.

Project Structure

Scripts
main.py
Purpose: Automates the process of web page interaction using Selenium to extract data and transform it into a CSV format.
Usage: Run this script to initiate data extraction from the STEPN marketplace web page. Requires a WebDriver compatible with your browser version.

HTMLparser.py
Purpose: Parses the HTML content of the web page, including interactions like button clicks to start the data extraction process.
Usage: This script is called by main.py to handle page interactions.

pandas_sma.py
Purpose: Performs Simple Moving Average (SMA) analysis to identify individual price trends versus overall market trends.
Usage: Use this script to analyze the output CSV from main.py, providing insights into market behavior over time.

pandas_adf_asf.py
Purpose: Conducts Time Series Decomposition and applies the Augmented Dickey-Fuller (ADF) test and ASF to determine the stationarity and structural components of the NFT pricing data.
Usage: This script further analyzes the time series data, helping to understand the underlying patterns such as seasonality and trends.

pandas_stats.py
Purpose: Applies various statistical regression methods to the data to explore the relationships between different market variables.
Usage: Execute this script to perform regression analysis and output statistical measures like F-statistic, t-value, p-value, and R-squared.

How to Run the Scripts

Ensure Python and necessary libraries (Selenium, pandas, numpy, statsmodels, matplotlib) are installed.

Clone this repository to your local machine.
Set up the necessary WebDriver for Selenium in the main.py.
Run each script from the terminal or an IDE, ensuring the data path in each script points to your CSV data file location.
Review the output files and console outputs for analysis results.

Project Goals

The aim of this project is to automate the collection and analysis of NFT price data from the STEPN platform, 
providing actionable insights into price trends, market behavior, and the overall impact of economic factors within the Web3 ecosystem.

Database

Web Address: STEPN Market Guide Web3 Website: https://stepn-market.guide/
