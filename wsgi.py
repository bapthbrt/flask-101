# wsgi.py
from flask import Flask, jsonify, request
from counter import Counter

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
counter = Counter()
counter.id = 4


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/api/v1/products', methods=['GET', 'POST'])
def get_products():
    if request.method == 'POST':
        product = {"id": counter.next(), "name": request.get_json()['name']}
        PRODUCTS.append(product)
        return jsonify(product), 201
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
