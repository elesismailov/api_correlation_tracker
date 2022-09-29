from unittest import TestCase
from django.test import Client

# Create your tests here.

from django.http import JsonResponse

from users.models import CustomUser

import os

from api.tracks.tests_.test_delete_track_route import *


class UpdatingTrack(TestCase):

    def setUp(self):

        self.user = CustomUser.objects.create_user(
                    username='testuser2',
                    email='testuser2@gmail.com',
                    password='123'
                )

        self.api_key = self.user.api_key

        self.c = Client()
        self.track_id = '12/'

    def tearDown(self):

        self.user.delete()

    def test_no_api_key(self):

        response = self.c.put('/api/tracks/' + self.track_id) 

        self.assertEqual(response.status_code, 400)

    def test_get_jsonresponse(self):

        response = self.c.put(
                '/api/tracks/' + self.track_id,
                content_type = 'application/json',
                HTTP_X_API_KEY = self.api_key
                )

        self.assertIsInstance(response, JsonResponse)

    # def test_ok_message(self):

    #     response = self.c.put(
    #             '/api/tracks/' + self.track_id,
    #             {

    #                 },
    #             content_type = 'application/json',
    #             HTTP_X_API_KEY = self.api_key
    #             )
    #     print(self.api_key)

    #     self.assertEqual(response.content, '')







