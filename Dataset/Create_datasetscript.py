import sys
sys.path.append("c:\\users\\chinhanl\\appdata\\local\\programs\\python\\python38\\lib\\site-packages")
import pandas as pd

# Load your dataset
df = pd.read_csv('Comfirm_dataset.csv', encoding='ISO-8859-1', parse_dates=['date'])

# Fill NaN, null, or empty cells with the previous data (forward fill)
df.fillna(method='ffill', inplace=True)

# Additionally, you might want to back-fill to ensure that NaN values at the start are also filled
df.fillna(method='bfill', inplace=True)

# Save the cleaned dataset to a new Excel file
df.to_csv('Cleaned_dataset.csv', index=False)

print("The cleaned dataset has been saved to 'Cleaned_dataset.xlsx'.")
# import pandas as pd

# # Load the translation table from a CSV file
# translation_df = pd.read_csv('product_category_name_translation.csv')
# # Convert the translation DataFrame into a dictionary
# category_translation = pd.Series(translation_df.product_category_name_english.values, index=translation_df.product_category_name).to_dict()

# # Load your database into a pandas DataFrame
# # Replace 'your_database.csv' with the actual path to your database file
# df = pd.read_csv('updated_first_dataset.csv')

# # Function to translate product category names
# def translate_category(category):
#     return category_translation.get(category, category)  # Returns original category if not found in the dictionary

# # Apply the translation function to the 'product_category_name' column
# df['product_category_name_english'] = df['product_category_name'].apply(translate_category)

# # Now, your DataFrame 'df' has a new column 'product_category_name_english' with the translated category names
# # You can inspect the DataFrame to verify the translations
# print(df.head())

# # Optionally, save the updated DataFrame back to a new CSV file
# df.to_csv('translated_database.csv', index=False)


# # import pandas as pd

# # # Read the datasets
# # df1 = pd.read_csv('merged_latest_with_geolocation.csv')  # Replace 'first_dataset.csv' with the actual filename
# # df2 = pd.read_csv('olist_products_dataset.csv')  # Replace 'second_dataset.csv' with the actual filename

# # # Merge the datasets based on 'product_id'
# # merged_df = pd.merge(df1, df2, on='product_id', how='left')

# # # Update the relevant columns in the first dataset with values from the second dataset
# # relevant_columns = ['product_category_name', 'product_name_lenght', 'product_description_lenght', 'product_photos_qty', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']
# # for col in relevant_columns:
# #     df1[col] = merged_df[col]

# # # Save the updated dataset
# # df1.to_csv('updated_first_dataset.csv', index=False)  # Replace 'updated_first_dataset.csv' with the desired output filename


# # # import pandas as pd

# # # # Load the latest dataset (assuming it's saved as 'latest_dataset.csv')
# # # latest_dataset = pd.read_csv('matched_sellers.csv')

# # # # Load the geolocation dataset (assuming it's saved as 'geolocation_dataset.csv')
# # # geolocation_dataset = pd.read_csv('olist_geolocation_dataset.csv')

# # # # Since the geolocation dataset might have multiple entries for the same zip_code_prefix,
# # # # you might want to drop duplicates or aggregate data before merging.
# # # # Here, we'll drop duplicates for simplicity. You might choose a different approach based on your needs.
# # # geolocation_dataset_unique = geolocation_dataset.drop_duplicates(subset=['zip_code_prefix'])

# # # # Merge datasets on 'zip_code_prefix'
# # # # Note: Ensure the column names for zip code prefix match in both datasets. Adjust column names as necessary.
# # # merged_df = pd.merge(latest_dataset, geolocation_dataset_unique, left_on='zip_code_prefix', right_on='zip_code_prefix', how='left')

# # # # Save the merged dataset to a new CSV file
# # # merged_df.to_csv("merged_latest_with_geolocation.csv", index=False)

# # # import pandas as pd

# # # # Replace 'path_to_first_dataset.xlsx' and 'path_to_third_dataset.xlsx' with the actual paths to your Excel files
# # # df1 = pd.read_csv('olist_geolocation_dataset.csv')
# # # df3 = pd.read_csv('matched_sellers.csv')

# # # # Merge datasets on 'seller_id'
# # # merged_df = pd.merge(df1, df3, on='geolocation_zip_code_prefix')

# # # # Save the merged dataset to a new Excel file
# # # merged_df.to_csv("matched_sellers1.csv", index=False)