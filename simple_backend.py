from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Load data
def load_data():
    try:
        with open('data/data.json', 'r') as f:
            return json.load(f)
    except:
        return {"customers": [], "products": [], "purchases": [], "expenses": []}

data = load_data()

@app.route('/')
def home():
    return "AI Backend Running!"

@app.route('/ai/query', methods=['POST'])
def ai_query():
    user_query = request.json.get('query', '').lower()
    
    if 'financial' in user_query or 'money' in user_query or 'profit' in user_query:
        response = {
            "total_revenue": 15000,
            "net_profit": 5000,
            "total_sales_count": 50
        }
    elif 'inventory' in user_query or 'stock' in user_query or 'restock' in user_query:
        response = {
            "low_stock_alerts": [
                {"product_id": "P001", "name": "Product 1", "current_stock": 25, "alert": "Low Stock"}
            ],
            "restocking_recommendations": [
                {"product_id": "P001", "name": "Product 1", "order_quantity": 100}
            ]
        }
    elif 'reward' in user_query or 'loyalty' in user_query:
        response = {
            "recommendation": "15% off your next purchase of Product 2 as a loyalty reward!"
        }
    elif 'design' in user_query:
        response = {
            "design_idea": {
                "trend": "Minimalist",
                "description": "Clean, modern design with simple navigation",
                "color_palette_suggestion": ["#FFFFFF", "#333333", "#E0E0E0"],
                "typography_suggestion": {"headings": "Montserrat", "body": "Open Sans"},
                "mock_design_preview_url": "https://via.placeholder.com/800x450/e0e0e0/333333?text=Minimalist+Design"
            }
        }
    elif 'website' in user_query or 'problem' in user_query:
        response = {
            "website_problems": [
                {"type": "WARNING", "description": "High page load time detected", "suggested_fix": "Optimize images"}
            ]
        }
    else:
        response = "I can help with: financials, inventory, loyalty rewards, design ideas, and website health. What would you like to know?"
    
    return jsonify({"response": response})

@app.route('/customers')
def get_customers():
    return jsonify(data.get('customers', []))

@app.route('/inventory')
def get_inventory():
    return jsonify(data.get('products', []))

@app.route('/financials')
def get_financials():
    return jsonify({
        "total_revenue": 15000,
        "net_profit": 5000,
        "total_sales_count": 50,
        "total_cogs": 8000,
        "gross_profit": 7000,
        "operating_expenses": 2000,
        "tax_payable": 750
    })

if __name__ == '__main__':
    print("Starting AI Backend on http://127.0.0.1:5000")
    print("Open index2.html and try the AI Assistant!")
    app.run(debug=True, port=5000)