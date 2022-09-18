
from django.test import TestCase

from django.http import JsonResponse
from django.test import Client

from users.models import CustomUser as User
from api.tracks.models import Track
from django.db import transaction

from api.tracks.operators import *
from api.tracks.exceptions import *

import datetime


class GettingTrack(TestCase):

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

        result = getTrack(
                user = self.user,
                track_id=c.id
                )

        self.assertIsInstance(result, Track)


    def test_no_user(self):

        with transaction.atomic():
            createTrack( user=self.user, title='title1',)

        try:
            track = getTrack(user=None, track_id=0)

            self.fail('Did not raise an exception.')

        except InvalidUserError:
            pass

        except Exception:
            self.fail('Other exception was raised')


    def test_invalid_id(self):

        with transaction.atomic():
            c = createTrack( user=self.user, title='title1',)

        try:
            track = getTrack(user=self.user, track_id=None)

            self.fail('Did not raise an exception.')

        except InvalidTrackError:
            pass

        except Exception:
            self.fail('Other exception was raised')


    def test_getting_track(self):

        with transaction.atomic():
            c = createTrack( user=self.user, title='title1',)

        track = getTrack(user=self.user, track_id=c.id)

        self.assertEqual(c.title, track.title)





