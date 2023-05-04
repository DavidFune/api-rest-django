from django.test import TestCase
from django.urls import reverse
import json
g_product = {
    "name": "Camara de ar",
    "kg": "1.00",
    "description": "camara de ar de trator"
    }

g_category = {
    "name": "Borracha",
    "description": "Ex: pneu, chinelo"
}

class ProductViewTestCase(TestCase):


    def test_create_product(self): 
        resposne = self.client.post('/products/',g_product)
        self.assertEqual(resposne.status_code, 201)

    def test_find_all_products(self):
        self.client.post('/products/', g_product).getvalue() 
        response = self.client.get('/products/')

        self.assertGreater(len(response.getvalue()), 0)

class RecycleTestCase(TestCase):

    def test_create_recycle(self): 

        resposne_p = self.client.post('/products/',g_product)
        self.assertEqual(resposne_p.status_code, 201)
        resposne_c = self.client.post('/categories/',g_category)
        self.assertEqual(resposne_c.status_code, 201)

        product = json.loads(resposne_p.getvalue())
        category = json.loads(resposne_c.getvalue())

        resposne_r = self.client.post('/recycling/',{
            "product": product['id'],
            "category": category['id']
        })

        self.assertEqual(resposne_r.status_code, 201)
