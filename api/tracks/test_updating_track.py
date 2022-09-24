from django.test import TestCase

from django.http import JsonResponse
from django.test import Client

from users.models import CustomUser as User
from api.tracks.models import Track
from django.db import transaction

from api.tracks.operators import *
from api.tracks.exceptions import *

import datetime


class UpdatingTrack(TestCase):

    def setUp(self):

        # Create test user
        self.user = User.objects.create_user(
                    username='testuser',
                    email='testuser@gmail.com',
                    password='123'
                )

    def test_getting_track_instance(self):

        with transaction.atomic():
            c = createTrack( user=self.user, title='title1',)

        result = updateTrack(
                track_id=c.id,
                title='newTitle',
                )

        self.assertIsInstance(result, Track)



    def test_no_id(self):

        with transaction.atomic():
            c = createTrack( user=self.user, title='title1',)

        self.assertEqual(c.title, 'title1')

        try:
            track = updateTrack(track_id=None, title='anotherTitle')

            self.fail('Did not raise an exception.')

        except InvalidTrackError:
            pass

        except Exception:
            self.fail('Other exception was raised')

    def test_invalid_id(self):

        with transaction.atomic():
            c = createTrack( user=self.user, title='title1',)

        self.assertEqual(c.title, 'title1')

        try:
            track = updateTrack(track_id=12345, title='anotherTitle')

            self.fail('Did not raise an exception.')

        except Track.DoesNotExist:
            pass

        except Exception:
            self.fail('Other exception was raised')


    def test_updating_title(self):

        with transaction.atomic():
            c = createTrack( user=self.user, title='title1',)

        self.assertEqual(c.title, 'title1')

        track = updateTrack(track_id=c.id, title='newTitle')

        self.assertEqual(track.title, 'newTitle')


    def test_updating_color(self):

        with transaction.atomic():
            c = createTrack( user=self.user, title='title1',)

        self.assertEqual(c.color, '')

        track = updateTrack(track_id=c.id, color='newColor')

        self.assertEqual(track.color, 'newColor')


    def test_updating_description(self):

        with transaction.atomic():
            c = createTrack( user=self.user, title='title1',)

        self.assertEqual(c.description, '')

        track = updateTrack(track_id=c.id, description='somethingnew')

        self.assertEqual(track.description, 'somethingnew')







