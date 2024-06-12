# Import necessary libraries
import xgboost as xgb
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import root_mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

# Load your dataset
df = pd.read_csv('Comfirm_dataset.csv', encoding='ISO-8859-1')

# Feature Engineering
df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'], dayfirst=True)
df['shipping_limit_date'] = df['shipping_limit_date'].astype('int64') // 10**9

# Select features and target variable
X = df[['zip_code_prefix', 'shipping_limit_date', 'geolocation_lat', 'geolocation_lng', 'product_description_lenght', 'product_photos_qty']]
y = df['price']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the XGBoost regressor within a Pipeline
# Assuming all features need scaling
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), X.columns)
    ])

xgb_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('regressor', xgb.XGBRegressor(objective='reg:squarederror'))])

param_grid = {
    'regressor__max_depth': [3, 4, 5, 6, 7, 8],
    'regressor__n_estimators': [100, 200, 300, 400],
    'regressor__learning_rate': [0.01, 0.05, 0.1, 0.2],
    'regressor__subsample': [0.6, 0.7, 0.8, 0.9, 1.0],
    'regressor__colsample_bytree': [0.6, 0.7, 0.8, 0.9, 1.0],
    'regressor__gamma': [0, 0.1, 0.2, 0.3, 0.4],
    'regressor__min_child_weight': [1, 2, 3, 4, 5],
    'regressor__lambda': [0, 0.1, 1, 10],
    'regressor__alpha': [0, 0.1, 1, 10]
}

# Adjust GridSearchCV setup accordingly
grid_search = GridSearchCV(estimator=xgb_pipeline, param_grid=param_grid, cv=5, scoring='neg_root_mean_squared_error', verbose=2)

# Perform the grid search
grid_search.fit(X_train, y_train)

# Print the best parameters and best score (RMSE)
print("Best parameters found: ", grid_search.best_params_)
print("Best RMSE found: ", -grid_search.best_score_)

# Use the best estimator to make predictions
best_model = grid_search.best_estimator_
y_pred = best_model.predict