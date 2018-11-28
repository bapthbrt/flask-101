# wsgi.py
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World! Bonjour"


@app.route('/api/v1/products')
def get_products():
    return jsonify([{'id': 1, 'name': 'Skello'}, {'id': 2, 'name': 'Socialive.tv'}])
