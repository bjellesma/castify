from flaskr import create_app
import unittest
import json
from tests.test_agency import casting_assistant_headers, casting_director_headers
from flask_sqlalchemy import SQLAlchemy
from secure import TEST_CONNECT_STRING
from models.models import setup_db

class ActorTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, TEST_CONNECT_STRING)

        self.test_actor_original = {
            'name': 'Tom Hardy',
            'age': 42,
            'gender': 'male'
        }

        self.test_actor = {
            'name': 'Test McTesterson',
            'age': 25,
            'gender': 'male'
        }

        self.test_actor_error = {
            "bad": "string"
        }

        self.test_actor_update = {
            'name': 'Testina',
            'gender': 'female'
        }

        self.test_actor_update_error = {
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

    def test_read_all_actors(self):
        res = self.client().get('/api/actors',headers=casting_assistant_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['actors'], list)

    def test_read_single_actor(self):
        res = self.client().get('/api/actors/1',headers=casting_assistant_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['actor'], dict)
        self.assertEqual(data['actor']['name'], self.test_actor_original.get('name'))

    def test_read_single_actor_error(self):
        res = self.client().get('/api/actors/4004',headers=casting_assistant_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not Found")

    def test_create_actor(self):
        res = self.client().post(
            '/api/actors',
            data=json.dumps(self.test_actor),
            headers=casting_director_headers 
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['actor_id'], int)

    def test_create_actor_error(self):
        res = self.client().post(
            '/api/actors',
            data=json.dumps(self.test_actor_error),
            headers=casting_director_headers 
        )
        self.assertEqual(res.status_code, 400)

    def test_update_actor(self):
        res = self.client().patch(
            '/api/actors/1',
            data=json.dumps(self.test_actor_update),
            headers=casting_director_headers 
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['actor']['name'], self.test_actor_update['name'])
        res = self.client().get('/api/actors/1', headers=casting_director_headers)
        data = json.loads(res.data)
        self.assertEqual(data['actor']['name'], self.test_actor_update['name'])

    def test_update_actor_error(self):
        res = self.client().patch(
            '/api/actors/1',
            data=json.dumps(self.test_actor_update_error),
            headers=casting_director_headers 
        )
        self.assertEqual(res.status_code, 400)

    def test_delete_single_actor(self):
        # First test that id 2 exists
        res = self.client().get('/api/actors/2', headers=casting_director_headers)
        self.assertEqual(res.status_code, 200)
        # Now delete id 2
        res = self.client().delete('/api/actors/2', headers=casting_director_headers)
        self.assertEqual(res.status_code, 200)
        # test that id doesn't exist anymore
        res = self.client().get('/api/actors/2', headers=casting_director_headers)
        self.assertEqual(res.status_code, 404)

    def test_delete_single_actor_error(self):
        res = self.client().delete('/api/actors/9999', headers=casting_director_headers)
        self.assertEqual(res.status_code, 404)