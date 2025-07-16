from flask import Flask, render_template
import json

app = Flask(__name__)

def load_items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            return data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def show_items():
    items = load_items()
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
