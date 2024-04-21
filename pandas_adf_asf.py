import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt


def perform_exploratory_analysis(fname):
    try:
        # Load the data
        data = pd.read_csv(fname)
        print(data.head())

        # Clean and convert 'price' column
        data['price'] = data['price'].str.replace(' GMT', '').astype(float)
        high_cap = data['price'].quantile(0.95)
        data['price'] = np.where(data['price'] > high_cap, high_cap, data['price'])

        # Convert 'date' to datetime and sort
        data['date'] = pd.to_datetime(data['date'] + '/2024', format='%m/%d/%Y', errors='coerce')
        data.dropna(subset=['date', 'price'], inplace=True)
        data.sort_values('date', inplace=True)

        # Summarize the data
        print(data.describe())

        # Set 'date' as the index
        data.set_index('date', inplace=True)

        # Time Series Decomposition
        decomposition = seasonal_decompose(data['price'], model='additive', period=30)
        decomposition.plot()
        plt.show()

        # ADF Test
        adf_result = adfuller(data['price'])
        print(f'ADF Statistic: {adf_result[0]}')
        print(f'p-value: {adf_result[1]}')
        for key, value in adf_result[4].items():
            print('Critial Values:')
            print(f'   {key}, {value}')

        # ACF and PACF plots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        plot_acf(data['price'], lags=40, ax=ax1)
        plot_pacf(data['price'], lags=40, ax=ax2)
        plt.show()

        # OLS Regression
        X = sm.add_constant(data['date'].dt.dayofyear)  # Add a constant term to the predictor
        y = data['price']
        model = sm.OLS(y, X).fit()
        print(model.summary())

    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")
    except Exception as e:
        print("An unexpected error occurred:", e)


# Input parameters
fname = 'shoes_old.csv'

# Call the function to perform exploratory analysis
perform_exploratory_analysis(fname)
