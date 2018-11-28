# wsgi.py
from flask import Flask, jsonify, request


app = Flask(__name__)

PRODUCTS = [
        {
            'id': 1, 'name': 'Skello'
        }, {
            'id': 2, 'name': 'Socialive.tv'
        }, {
            'id': 3, 'name': 'Test'
        }, {
            'id': 4, 'name': 'Toto'
        }
    ]

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/api/v1/products')
def get_products():
    return jsonify(PRODUCTS)


@app.route('/api/v1/products/<int:id>', methods=['GET', 'DELETE'])
def get_product(id):
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i].get('id') == id:
            if request.method == 'GET':
                return jsonify(PRODUCTS[i]), 200
            if request.method == 'DELETE':
                del PRODUCTS[i]
                return '', 204
    return 'Product not found', 404
