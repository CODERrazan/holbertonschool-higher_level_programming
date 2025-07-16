from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_products(file_path):
    """Read and parse products from JSON file"""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def read_csv_products(file_path):
    """Read and parse products from CSV file"""
    try:
        products = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert id to int and price to float
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except (FileNotFoundError, ValueError, KeyError):
        return None

def read_sql_products(db_path):
    """Read products from SQLite database"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        products = []
        for row in cursor.fetchall():
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
        return products
    except sqlite3.Error:
        return None

def filter_product_by_id(products, product_id):
    """Filter products by ID"""
    for product in products:
        if product['id'] == product_id:
            return [product]
    return None

@app.route('/products')
def display_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)
    
    error = None
    products = None
    
    if source == 'json':
        products = read_json_products('products.json')
    elif source == 'csv':
        products = read_csv_products('products.csv')
    elif source == 'sql':
        products = read_sql_products('products.db')
    else:
        error = "Wrong source. Please use 'json', 'csv', or 'sql'."
    
    if products is None and not error:
        error = "Failed to read product data."
    
    if not error and product_id is not None:
        filtered = filter_product_by_id(products, product_id)
        if filtered:
            products = filtered
        else:
            error = "Product not found."
    
    return render_template('product_display.html', 
                         products=products, 
                         error=error, 
                         source=source)

if __name__ == '__main__':
    app.run(debug=True)
