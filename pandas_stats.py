import pandas as pd
import numpy as np
import statsmodels.api as sm

def perform_statistical_analysis(fname):
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

        # Convert 'date' to a numeric value: the number of days since the start of the dataset
        data['date_ordinal'] = (data['date'] - data['date'].min()).dt.days

        # OLS Regression with 'date_ordinal' as the predictor
        X = sm.add_constant(data['date_ordinal'])  # Add a constant term to the predictor
        y = data['price']
        model = sm.OLS(y, X).fit()

        # Print the summary of OLS Regression
        print(model.summary())

    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Input parameters
fname = 'shoes_old.csv'

# Call the function to perform exploratory analysis
perform_statistical_analysis(fname)
