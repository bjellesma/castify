from flaskr import create_app
import os
import unittest
import json

class AgencyTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_init(self):
        res = self.client().get('/api/test')
        self.assertEqual(res.status_code, 200)