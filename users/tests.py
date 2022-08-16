from django.test import TestCase

# Create your tests here.

from django.test import Client
from users.models import CustomUser as User
import json


class UserLogin(TestCase):

    def setUp(self):

        self.c = Client()

        self.user = User(username='testuser1', email='testuser1@gmail.com')

        self.user.set_password('1231')

        self.user.save()

    def tearDown(self):

        self.user.delete()

    def test_getting_apikey_email(self):

        response = self.c.post('/log-in/', 
                {
                    'email': 'testuser1@gmail.com',
                    'password': '1231'
                },
                content_type='application/json'
            )

        string = response.content.decode('utf8')

        data = json.loads(string)

        self.assertEqual(data['key'], self.user.api_key)
