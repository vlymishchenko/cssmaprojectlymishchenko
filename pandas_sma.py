import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Loading the dataset
data = pd.read_csv('/Users/valeria/PycharmProjects/pandas/Stepin Parsing/shoes_old.csv')

# Convert 'price' to float after cleaning
data['price'] = data['price'].str.replace(' GMT', '').astype(float)

# Parse 'date' column by appending the year 2024 and converting to datetime
data['date'] = pd.to_datetime(data['date'].apply(lambda x: f"{x}/2024"), format='%m/%d/%Y', errors='coerce')

# Drop rows with null values
data.dropna(subset=['date', 'price'], inplace=True)

# Sort by date to ensure correct order in plots and calculations
data.sort_values(by='date', inplace=True)

# Aggregate the data to get daily median prices
daily_data = data.groupby(data['date'].dt.date)['price'].median()

# Calculate the long-term moving average for the market trend (a 30-day SMA)
market_trend = daily_data.rolling(window=30, min_periods=1).mean()

# Calculate the correlation between daily prices and the market trend
correlation = daily_data.corr(market_trend)

# Print out the correlation
print(f"The correlation between individual prices and the market trend is: {correlation:.2f}")

# Plotting the results
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Daily Median Price', color=color)
ax1.plot(daily_data.index, daily_data.values, color=color, label='Daily Median Price')
ax1.tick_params(axis='y', labelcolor=color)

# Set the locator
locator = mdates.MonthLocator()  # every month
# Specify the format - full month name + 1 day of the month
fmt = mdates.DateFormatter('%b %d')

ax1.xaxis.set_major_locator(locator)
ax1.xaxis.set_major_formatter(fmt)

# Rotate and align the tick labels so they look better
fig.autofmt_xdate()

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('Market Trend (30-day SMA)', color=color)
ax2.plot(market_trend.index, market_trend.values, color=color, linestyle='--', label='Market Trend')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # to make sure that the labels don't get cut off
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.title('Price Trend vs. Market Trend')

# Save the plot to a file
plt.savefig('/Users/valeria/PycharmProjects/pandas/Stepin Parsing/market_trend_plot.png')

# plt.show()  # This should be used if a user prefers to display the plot instead
