
from django.test import TestCase

from django.http import JsonResponse
from django.test import Client

from users.models import CustomUser as User
from api.tracks.models import Track
from django.db import transaction

from api.tracks.operators import *
from api.tracks.exceptions import *

import datetime

class DeleteTrackRoute(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
                    username='testuser2',
                    email='testuser2@gmail.com',
                    password='123'
                )

        self.c = Client()


    def test_deletion(self):

        self.assertEqual(len(Track.objects.all()), 0)
        with transaction.atomic():
            track = createTrack(
                    user=self.user,
                    title='Testing Title',
                    )

        self.assertEqual(track, Track.objects.first())
        self.assertEqual(Track.objects.count(), 1)

        response = self.c.delete(
                '/api/tracks/' + str(track.id),
                content_type = 'application/json',
                HTTP_X_API_KEY = self.user.api_key
                )

        self.assertEqual(response.status_code, 200)


    def test_getting_json_response(self):
        self.assertEqual(len(Track.objects.all()), 0)
        with transaction.atomic():
            track = createTrack(
                    user=self.user,
                    title='Testing Title',
                    )

        self.assertEqual(track, Track.objects.first())
        self.assertEqual(Track.objects.count(), 1)

        response = self.c.delete(
                '/api/tracks/' + str(track.id),
                content_type = 'application/json',
                HTTP_X_API_KEY = self.user.api_key
                )

        self.assertIsInstance(response, JsonResponse)

    def test_error_404(self):
        self.assertEqual(len(Track.objects.all()), 0)
        with transaction.atomic():
            track = createTrack(
                    user=self.user,
                    title='Testing Title',
                    )

        self.assertEqual(track, Track.objects.first())
        self.assertEqual(Track.objects.count(), 1)

        response = self.c.delete(
                '/api/tracks/' + str(track.id + 1234),
                content_type = 'application/json',
                HTTP_X_API_KEY = self.user.api_key
                )

        self.assertEqual(response.status_code, 404)

    def test_error_505(self):
        pass



















