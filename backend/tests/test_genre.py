from flaskr import create_app
import unittest
import json
from tests.test_agency import casting_assistant_headers, casting_director_headers
from flask_sqlalchemy import SQLAlchemy
from secure import TEST_CONNECT_STRING
from models.models import setup_db

class GenreTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, TEST_CONNECT_STRING)

        self.test_genre_original = {
            'name': 'soul'
        }

        self.test_genre = {
            'name': 'punk'
        }

        self.test_genre_error = {
            "bad": "string"
        }

        self.test_genre_update = {
            'name': 'metal'
        }

        self.test_genre_update_error = {
            'name': 4
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_read_all_genres(self):
        res = self.client().get('/api/genres',headers=casting_assistant_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['genres'], list)

    def test_read_single_genre(self):
        res = self.client().get('/api/genres/1',headers=casting_assistant_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['genre'], dict)
        self.assertEqual(data['genre']['name'], self.test_genre_original.get('name'))

    def test_read_single_genre_error(self):
        res = self.client().get('/api/genres/4004',headers=casting_assistant_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not Found")

    def test_create_genre(self):
        res = self.client().post(
            '/api/genres',
            data=json.dumps(self.test_genre),
            headers=casting_director_headers 
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['genre_id'], int)

    def test_create_genre_error(self):
        res = self.client().post(
            '/api/genres',
            data=json.dumps(self.test_genre_error),
            headers=casting_director_headers 
        )
        self.assertEqual(res.status_code, 400)

    def test_update_genre(self):
        res = self.client().patch(
            '/api/genres/1',
            data=json.dumps(self.test_genre_update),
            headers=casting_director_headers 
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['genre']['name'], self.test_genre_update['name'])
        # test that getting id 1 will result in the new name
        res = self.client().get('/api/genres/1', headers=casting_director_headers)
        data = json.loads(res.data)
        self.assertEqual(data['genre']['name'], self.test_genre_update['name'])

    def test_update_genre_error(self):
        res = self.client().patch(
            '/api/genres/1',
            data=json.dumps(self.test_genre_update_error),
            headers=casting_director_headers 
        )
        self.assertEqual(res.status_code, 400)

    def test_delete_single_genre(self):
        # First test that id 2 exists
        res = self.client().get('/api/genres/2', headers=casting_director_headers)
        self.assertEqual(res.status_code, 200)
        # Now delete id 2
        res = self.client().delete('/api/genres/2', headers=casting_director_headers)
        self.assertEqual(res.status_code, 200)
        # test that it doesn't exist anymore
        res = self.client().get('/api/genres/2', headers=casting_director_headers)
        self.assertEqual(res.status_code, 404)

    def test_delete_single_genre_error(self):
        res = self.client().delete('/api/genres/9999', headers=casting_director_headers)
        self.assertEqual(res.status_code, 404)