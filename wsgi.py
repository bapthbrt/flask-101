# wsgi.py
from flask import Flask, jsonify


app = Flask(__name__)

PRODUCTS = [
        {
            'id': 1, 'name': 'Skello'
        }, {
            'id': 2, 'name': 'Socialive.tv'
        }, {
            'id': 3, 'name': 'Test'
        }
    ]

@app.route('/')
def hello():
    return "Hello World! Bonjour"


@app.route('/api/v1/products')
def get_products():
    return jsonify(PRODUCTS)


@app.route('/api/v1/products/<int:id>')
def get_product(id):
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i].get('id') == id:
            return jsonify(PRODUCTS[i])
    return 'Product not found', 404
