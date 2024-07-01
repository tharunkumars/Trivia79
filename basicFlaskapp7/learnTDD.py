import unittest
import json
from __init__ import create_app
from models import setup_db

def learn_testing_behavior(self):
        """Test _____________"""
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

class LearnTestCase(unittest.TestCase):
    def __init__(self, first_name, last_name, age):
       self.first_name = first_name
       self.last_name = last_name
       self.age= age

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "test_db"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

    def tearDown(self):
        """Executed after each test"""
        # this is basically to Clear any db connections or any such test
        # related item we used in testing
        pass

    def test_LearnTest(self):
        """Executed after each test"""
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)
        pass

    def test_404_sent_requesting_beyond_valid_pag(self):
        """Executed after each test"""
        res = self.client().get('/')
        self.assertEqual(res.status_code, 404)
        pass

if __name__ == "__main__":
    unittest.main()

##Run from command line
##python3 test_flaskr.py
# assertTrue to Check whether an attribute is there
# assertEqual checks the value
#  SQLAlchemy method to explore
# Query.filter.one_or_none()
# 
# 