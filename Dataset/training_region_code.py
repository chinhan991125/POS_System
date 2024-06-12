import sys
sys.path.append("c:\\users\\chinhanl\\appdata\\local\\programs\\python\\python38\\lib\\site-packages")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from joblib import dump

# Load your dataset
df = pd.read_csv('Cleaned_dataset.csv', encoding='utf-8')

# Aggregate data to count sales for each product category in each state
df['sales_count'] = 1  # Add a helper column for counting
aggregated_df = df.groupby(['geolocation_state', 'product_category_name_english'], as_index=False).agg({'sales_count': 'count'})

# Pivot the aggregated table to get regions as rows and product categories as columns
pivot_df = aggregated_df.pivot(index='geolocation_state', columns='product_category_name_english', values='sales_count').fillna(0)

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(pivot_df)

# Perform K-means Clustering
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
cluster_labels = kmeans.fit_predict(scaled_data)


# Calculate the silhouette score
silhouette_avg = silhouette_score(scaled_data, cluster_labels)
print(f"Silhouette Score: {silhouette_avg}")

# Add the cluster labels back to the original pivot table
pivot_df['Cluster'] = cluster_labels

# Save the K-means model
dump(kmeans, 'Dissertation_kmeans_model.joblib')
print("K-means model saved as 'Dissertation_kmeans_model.joblib'.")

# Save the scaler
dump(scaler, 'Dissertation_scaler.joblib')
print("Scaler saved as 'Dissertation_scaler.joblib'.")


# Identifying High-Demand Regions based on the cluster with the highest mean sales count
pivot_df['Total_Sales'] = pivot_df.iloc[:, :-1].sum(axis=1)  # Sum sales across all product categories
high_demand_cluster = pivot_df.groupby('Cluster')['Total_Sales'].mean().idxmax()
high_demand_regions = pivot_df[pivot_df['Cluster'] == high_demand_cluster].index.tolist()

print(f"High-demand regions: {high_demand_regions}")

# Define your regions and initial product prices
regions = ["BA", "DF", "ES", "GO", "MG", "MS", "MT", "PB", "PR", "RJ", "RS", "SP", "SC"]
product_prices_data = {
    'region': regions,
    'product_a_price': [10] * len(regions),
    'product_b_price': [20] * len(regions),
    'product_c_price': [30] * len(regions),
    'product_d_price': [40] * len(regions),
    'product_e_price': [50] * len(regions)
}
product_prices_df = pd.DataFrame(product_prices_data)

# Print original prices
print("\nOriginal Product Prices:")
print(product_prices_df)

# Increase prices by 10% for products in high-demand regions
increase_percentage = 10 / 100  # 10% increase

# Apply price increase for high-demand regions
for region in high_demand_regions:
    if region in product_prices_df['region'].values:
        product_prices_df.loc[product_prices_df['region'] == region, product_prices_df.columns[1:]] *= (1 + increase_percentage)
        print(f"Adjusting prices for {region}")

# Print adjusted prices
print("\nAdjusted Product Prices for High-Demand Regions:")
print(product_prices_df)