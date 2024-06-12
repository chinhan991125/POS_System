import sys
sys.path.append("c:\\users\\chinhanl\\appdata\\local\\programs\\python\\python38\\lib\\site-packages")
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import joblib
# from pymongo import MongoClient
# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# app = Flask(__name__)
# CORS(app)  # Enable CORS

# # Load your model and scaler
# model = joblib.load('Dissertation_kmeans_model.joblib')
# scaler = joblib.load('Dissertation_scaler.joblib')

# # MongoDB connection parameters
# mongo_uri = "mongodb://localhost:27017/"
# db_name = "POS_System"
# collection_name = "POS_Dataset"

# @app.route('/get_dynamic_pricing', methods=['POST'])
# def get_dynamic_pricing():
#     try:
#         data = request.json
#         region = data['region']
#         product_id = data['product_id']
        
#         # Connect to the MongoDB database
#         client = MongoClient(mongo_uri)
#         db = client[db_name]
#         collection = db[collection_name]
        
#         # MongoDB query
#         query = {
#             'geolocation_state': region,
#             'product_id': product_id
#         }
#         cursor = collection.find(query, {'_id': 0, 'geolocation_state': 1, 'product_category_name_english': 1})
        
#         # Convert cursor to DataFrame
#         df = pd.DataFrame(list(cursor))
        
#         print("Hey there")
#         print(df)
        
#         if df.empty:
#             return jsonify({'error': 'No data found for the specified region and product ID'}), 404
        
#         # Assuming you need to aggregate sales_count in some way since MongoDB query is different
#         # You might need to adjust this part based on your actual data structure and requirements
#         # For demonstration, let's assume 'sales_count' is a field you can directly use
#         # If 'sales_count' needs to be calculated, you'll need to use MongoDB's aggregation framework
        
#         # Ensure preprocessing steps match those used during model training
#         scaled_data = scaler.transform(df[['sales_count']])
        
#         price = model.predict(scaled_data)
        
#         return jsonify({'price': price.tolist()})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection parameters
mongo_uri = "mongodb://localhost:27017/"
db_name = "POS_System"
collection_name = "POS_Dataset"

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # Connect to the MongoDB database
        client = MongoClient(mongo_uri)
        db = client[db_name]
        collection = db[collection_name]
        
        # Fetch data from the collection
        data = collection.find({}, {'_id': 0})  # Exclude the '_id' field
        
        # Convert cursor to list
        data_list = list(data)
        
        return jsonify(data_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)