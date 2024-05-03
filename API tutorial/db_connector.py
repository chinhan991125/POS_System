import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Intel@123",
        database="new_pos_db"
    )

def insert_transaction_with_products(user_name, transaction_date, region, total_price, products):
    db = connect_to_db()
    cursor = db.cursor()
    
    # Insert the transaction and get its ID
    transaction_query = """
    INSERT INTO transactions (user_name, transaction_date, region, total_price) 
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(transaction_query, (user_name, transaction_date, region, total_price))
    transaction_id = cursor.lastrowid
    
    # Insert each product for this transaction
    product_query = """
    INSERT INTO transaction_products (transaction_id, product_name, quantity) 
    VALUES (%s, %s, %s)
    """
    for product in products:
        cursor.execute(product_query, (transaction_id, product['product_name'], product['quantity']))
    
    db.commit()
    cursor.close()
    db.close()
    
# def insert_transaction_with_products(total_price, products):
#     db = connect_to_db()
#     cursor = db.cursor()
    
#     # Insert the transaction and get its ID
#     transaction_query = "INSERT INTO transactions (total_price) VALUES (%s)"
#     cursor.execute(transaction_query, (total_price,))
#     transaction_id = cursor.lastrowid
    
#     # Insert each product for this transaction
#     product_query = "INSERT INTO transaction_products (transaction_id, product_name, quantity) VALUES (%s, %s, %s)"
#     for product in products:
#         cursor.execute(product_query, (transaction_id, product['product_name'], product['quantity']))
    
#     db.commit()
#     cursor.close()
#     db.close()