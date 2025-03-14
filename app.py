from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend

# Database connection
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Archstudia123",  # Change this to your MySQL root password
        database="arch_studio",
        cursorclass=pymysql.cursors.DictCursor
    )

# Get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Products")
        data = cursor.fetchall()
    conn.close()
    return jsonify(data)

# Add a product
@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    conn = get_db_connection()
    with conn.cursor() as cursor:
        sql = "INSERT INTO Products (category_id, product_name, description, price, dimension_data, stock_status) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (data['category_id'], data['product_name'], data['description'], data['price'], data['dimension_data'], data['stock_status']))
        conn.commit()
    conn.close()
    return jsonify({"message": "Product added successfully!"})

# Update a product
@app.route('/api/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    conn = get_db_connection()
    with conn.cursor() as cursor:
        sql = "UPDATE Products SET product_name=%s, description=%s, price=%s, dimension_data=%s, stock_status=%s WHERE id=%s"
        cursor.execute(sql, (data['product_name'], data['description'], data['price'], data['dimension_data'], data['stock_status'], id))
        conn.commit()
    conn.close()
    return jsonify({"message": "Product updated successfully!"})

# Delete a product
@app.route('/api/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        sql = "DELETE FROM Products WHERE id=%s"
        cursor.execute(sql, (id,))
        conn.commit()
    conn.close()
    return jsonify({"message": "Product deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)