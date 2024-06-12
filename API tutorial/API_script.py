import sys
sys.path.append("c:\\users\\chinhanl\\appdata\\local\\programs\\python\\python38\\lib\\site-packages")
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from db_connector import insert_transaction_with_products

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

@app.route('/upload-transaction', methods=['POST'])
def upload_transaction():
    data = request.json
    user_name = data.get('user_name')
    transaction_date = data.get('transaction_date')  # Ensure this is in 'YYYY-MM-DD HH:MM:SS' format
    region = data.get('region')
    total_price = data.get('total_price')
    products = data.get('products')
    
    if not all([user_name, transaction_date, region, total_price, products]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        insert_transaction_with_products(user_name, transaction_date, region, total_price, products)
        return jsonify({'success': True}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)