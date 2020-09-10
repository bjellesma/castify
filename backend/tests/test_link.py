from flaskr import create_app
import unittest
import json
from tests.test_agency import public_headers
from flask_sqlalchemy import SQLAlchemy
from secure import TEST_CONNECT_STRING
from models.models import setup_db


class LinkTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, TEST_CONNECT_STRING)

        self.test_movie_actor_link = {
            'movie_id': 1,
            'actor_id': 1
        }

        self.test_movie_actor_link_404 = {
            'movie_id': 9999,
            'actor_id': 9999
        }

        self.test_movie_actor_link_400 = {
            'movie_id': '9999',
            'actor_id': 9999
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

    def test_post_movie_actor(self):
        res = self.client().post(
            '/api/links/movie_actor',
            data=json.dumps(self.test_movie_actor_link),
            headers=public_headers
        )
        self.assertEqual(res.status_code, 200)

    def test_post_movie_actor_404(self):
        res = self.client().post(
            '/api/links/movie_actor',
            data=json.dumps(self.test_movie_actor_link_404),
            headers=public_headers
        )
        self.assertEqual(res.status_code, 404)

    def test_post_movie_actor_400(self):
        res = self.client().post(
            '/api/links/movie_actor',
            data=json.dumps(self.test_movie_actor_link_400),
            headers=public_headers
        )
        self.assertEqual(res.status_code, 400)
