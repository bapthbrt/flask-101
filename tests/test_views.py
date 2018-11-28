# tests/test_views.py
from flask import json
from flask_testing import TestCase
from wsgi import app


class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_product_json(self):
        response = self.client.get("/api/v1/products/2")
        product = response.json
        self.assertIsInstance(product, dict)

    def test_product_not_found(self):
        response = self.client.get("/api/v1/products/99")
        self.assertEqual(response.status_code, 404)

    def test_product_delete(self):
        response = self.client.delete("/api/v1/products/1")
        self.assertEqual(response.status_code, 204)
        response = self.client.get("/api/v1/products/1")
        self.assertEqual(response.status_code, 404)

    def test_product_create(self):
        response = self.client.post("/api/v1/products", data=json.dumps(dict(name='Genial')), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        product = response.json
        self.assertIsInstance(product, dict)
