from django.test import TestCase


class CartURLTests(TestCase):
   
    def test_cart_url(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
