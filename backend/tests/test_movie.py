from flaskr import create_app
import unittest
import json
from tests.test_agency import casting_assistant_headers, casting_director_headers, executive_producer_headers, public_headers
from flask_sqlalchemy import SQLAlchemy
from secure import TEST_CONNECT_STRING
from models.models import setup_db

class MovieTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, TEST_CONNECT_STRING)

        self.test_movie_original = {
            'title': 'Monty Python',
            'release date': '2020-09-05 17:07:43'
        }

        self.test_movie = {
            'title': 'test6',
            'release_date': '2020-09-05 17:07:43'
        }

        self.test_movie_error = {
            "bad": "string"
        }

        self.test_movie_update = {
            'title': 'test-update'
        }

        self.test_movie_update_error = {
            'title': 4
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

    def test_read_all_movies(self):
        res = self.client().get('/api/movies',headers=casting_assistant_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['movies'], list)

    def test_read_single_movie(self):
        res = self.client().get('/api/movies/1',headers=casting_assistant_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['movie'], dict)
        self.assertEqual(data['movie']['title'], self.test_movie_original.get('title'))

    def test_read_single_movie_error(self):
        res = self.client().get('/api/movies/4004',headers=casting_assistant_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not Found")

    def test_create_movie(self):
        res = self.client().post(
            '/api/movies',
            data=json.dumps(self.test_movie),
            headers=executive_producer_headers 
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['movie_id'], int)

    def test_create_movie_error(self):
        res = self.client().post(
            '/api/movies',
            data=json.dumps(self.test_movie_error),
            headers=executive_producer_headers 
        )
        self.assertEqual(res.status_code, 400)

    def test_create_movie_bad_method(self):
        res = self.client().patch(
            '/api/movies',
            data=json.dumps(self.test_movie_error),
            headers=public_headers 
        )
        self.assertEqual(res.status_code, 405)

    def test_create_movie_underauthenticated(self):
        """trying to create a movie as a casting director"""
        res = self.client().post(
            '/api/movies',
            data=json.dumps(self.test_movie),
            headers=casting_director_headers 
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized')

    def test_create_movie_unauthenticated(self):
        """trying to create a movie as a casting director"""
        res = self.client().post(
            '/api/movies',
            data=json.dumps(self.test_movie),
            headers=public_headers
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized')

    def test_update_movie(self):
        res = self.client().patch(
            '/api/movies/1',
            data=json.dumps(self.test_movie_update),
            headers=casting_director_headers 
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['movie']['title'], self.test_movie_update['title'])
        # Test that getting id 1 will result in the new title
        res = self.client().get('/api/movies/1', headers=casting_director_headers)
        self.assertEqual(res.status_code, 200)

    def test_update_movie_underauthenticated(self):
        """trying to update a movie as a casting assistant"""
        res = self.client().patch(
            '/api/movies/1',
            data=json.dumps(self.test_movie_update),
            headers=casting_assistant_headers 
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized')

    def test_update_movie_error(self):
        res = self.client().patch(
            '/api/movies/1',
            data=json.dumps(self.test_movie_update_error),
            headers=casting_director_headers 
        )
        self.assertEqual(res.status_code, 400)

    def test_delete_single_movie(self):
        # First test that id 2 exists
        res = self.client().get('/api/movies/2', headers=casting_director_headers)
        self.assertEqual(res.status_code, 200)
        # Now delete id 2
        res = self.client().delete('/api/movies/2', headers=executive_producer_headers)
        self.assertEqual(res.status_code, 200)
        # test that it doesn't exist anymore
        res = self.client().get('/api/movies/2', headers=casting_director_headers)
        self.assertEqual(res.status_code, 404)

    def test_delete_single_movie_error(self):
        res = self.client().delete('/api/movies/9999', headers=executive_producer_headers)
        self.assertEqual(res.status_code, 404)