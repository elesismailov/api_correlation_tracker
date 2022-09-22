from django.test import TestCase

from django.http import JsonResponse
from django.test import Client

from users.models import CustomUser as User
from api.tracks.models import Track
from django.db import transaction

from api.tracks.operators import *
from api.tracks.exceptions import *

import datetime


class GettingTrackEntries(TestCase):

    def setUp(self):

        # Create test user
        self.user = User.objects.create_user(
                    username='testuser',
                    email='testuser@gmail.com',
                    password='123'
                )

        # Create test track
        self.assertEqual(len(Track.objects.all()), 0)
        with transaction.atomic():
            result = createTrack(
                    user=self.user,
                    title='Testing Title',
                    )
        self.assertEqual(result, Track.objects.first())

        self.track = result


    def test_getting_entries(self):

        for i in range(1, 10):

            with transaction.atomic():
                createTrackEntry(
                        track = self.track,
                        rating = i,
                        date = '2000-09-'+ str(i),
                        )

        result = getTrackEntries(track=self.track)

        self.assertEqual(result[1].rating, 8)
        self.assertEqual(result[0].rating, 9)
        

    def test_no_track(self):

        try:
            result = getTrackEntries(track=None)
            self.fail('Did not raise an exception.')

        except InvalidTrackError:
            pass

        except Exception:
            self.fail('Other exception was raised')


    def test_getting_array(self):

        result = getTrackEntries(track=self.track)

        self.assertIsInstance(result, list)

















