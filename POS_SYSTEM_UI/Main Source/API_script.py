from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Load database configuration from a YAML file or define directly
db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.json
    totalPrice = data['totalPrice']
    products = data['products']
    
    cur = mysql.connection.cursor()
    for product in products:
        cur.execute("INSERT INTO orders (product_id, quantity, total_price) VALUES (%s, %s, %s)", (product['id'], product['quantity'], totalPrice))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)