from unittest import TestCase
from app import app
from flask import session



class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def test_setUp(self):
        with app.test_client() as client: 
            res = client.get('/')
            html= res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<form method="GET" action="/result">', html)
            app.config['TESTING'] = True

    def test_form(self):
        with app.test_client() as client: 
            res = client.get('/result',query_string= {'starting_currency': "USD", 'conversion_currency': "USD", 'amount': 1} )
            self.assertEqual(res.total,1)
    def test_invalid_country(self):
        with app.test_client() as client: 
            res = client.get('/result',query_string= {'starting_currency': 'USD', 'conversion_currency': 'LAM', 'amount': 1} )
            self.assertFalse(res)
