from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_data():
    with open('products.json', 'r') as file:
        return json.load(file)

def read_csv_data():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert price to float and id to int
            row['price'] = float(row['price'])
            row['id'] = int(row['id'])
            products.append(row)
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', None)
    
    # Initialize variables
    products = []
    error = None
    
    try:
        if source == 'json':
            products = read_json_data()
        elif source == 'csv':
            products = read_csv_data()
        else:
            error = "Wrong source. Please use 'json' or 'csv'"
        
        # Filter by ID if provided
        if product_id and not error:
            try:
                product_id = int(product_id)
                filtered = [p for p in products if p['id'] == product_id]
                if not filtered:
                    error = f"Product with ID {product_id} not found"
                else:
                    products = filtered
            except ValueError:
                error = "Invalid ID format"
                
    except Exception as e:
        error = f"Error reading data: {str(e)}"
    
    return render_template('product_display.html', 
                         products=products, 
                         error=error,
                         source=source)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
