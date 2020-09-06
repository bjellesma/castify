from flaskr import create_app
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from secure import TEST_CONNECT_STRING
from models.models import setup_db

headers = {'Content-Type': 'application/json'}

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

class MovieTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, TEST_CONNECT_STRING)

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
        res = self.client().get('/api/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['movies'], list)

    # TODO what if the id is not there
    def test_read_single_movie(self):
        res = self.client().get('/api/movies/9')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['movie'], dict)

    # TODO what if the id is there
    def test_read_single_movie_error(self):
        res = self.client().get('/api/movies/4004')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not Found")

    def test_create_movie(self):
        res = self.client().post(
            '/api/movies',
            data=json.dumps(self.test_movie),
            headers=headers 
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['movie_id'], int)

    def test_create_movie_error(self):
        res = self.client().post(
            '/api/movies',
            data=json.dumps(self.test_movie_error),
            headers=headers 
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)

    def test_update_movie(self):
        res = self.client().patch(
            '/api/movies/9',
            data=json.dumps(self.test_movie_update),
            headers=headers 
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['movie']['title'], self.test_movie_update['title'])

    def test_update_movie_error(self):
        res = self.client().patch(
            '/api/movies/9',
            data=json.dumps(self.test_movie_update_error),
            headers=headers 
        )
        self.assertEqual(res.status_code, 400)

    def test_delete_single_movie(self):
        res = self.client().delete('/api/movies/10')
        self.assertEqual(res.status_code, 200)
        # also test that this movie is now a 404
        res = self.client().get('/api/movies/910')
        self.assertEqual(res.status_code, 404)

    def test_delete_single_movie_error(self):
        res = self.client().delete('/api/movies/9999')
        self.assertEqual(res.status_code, 404)