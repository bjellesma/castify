from flaskr import create_app
import unittest
from flask_sqlalchemy import SQLAlchemy
from secure import TEST_CONNECT_STRING
from models.models import setup_db
from secure import CASTING_ASSISTANT_JWT, CASTING_DIRECTOR_JWT, EXECUTIVE_PRODUCER_JWT

casting_assistant_headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {CASTING_ASSISTANT_JWT}'
}

casting_director_headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {CASTING_DIRECTOR_JWT}'
}

executive_producer_headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {EXECUTIVE_PRODUCER_JWT}'
}

public_headers = {
    'Content-Type': 'application/json'
}

class AgencyTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, TEST_CONNECT_STRING)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_init(self):
        res = self.client().get('/api/test')
        self.assertEqual(res.status_code, 200)

    def test_init_404(self):
        res = self.client().get('/api/testd')
        self.assertEqual(res.status_code, 404)

