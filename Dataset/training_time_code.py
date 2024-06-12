import sys
sys.path.append("c:\\users\\chinhanl\\appdata\\local\\programs\\python\\python38\\lib\\site-packages")
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv('Cleaned_dataset.csv', encoding='utf-8')

# Adjust the date conversion to match the actual format of the date strings
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')
# Assuming each row represents a sale, count sales by region, product category, and month
df['month_year'] = df['date'].dt.to_period('M')
sales_data = df.groupby(['geolocation_state', 'product_category_name_english', 'month_year']).size().reset_index(name='sales_count')

# Identify high-demand products for each region and month (top 25% of sales)
high_demand_threshold = sales_data.groupby(['geolocation_state', 'month_year'])['sales_count'].quantile(0.75).reset_index(name='threshold')
high_demand_products = pd.merge(sales_data, high_demand_threshold, on=['geolocation_state', 'month_year'])
high_demand_products = high_demand_products[high_demand_products['sales_count'] > high_demand_products['threshold']]

# Assuming a simplistic approach to increase prices by 10% for high-demand products
high_demand_products['adjusted_price_increase'] = '10%'

# Display the high-demand products and their adjusted price increase
print(high_demand_products[['geolocation_state', 'product_category_name_english', 'month_year', 'sales_count', 'adjusted_price_increase']])

# Note: This script identifies high-demand products based on historical sales data.
# For actual forecasting, consider using time series models for each product and region.