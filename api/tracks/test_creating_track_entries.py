
from django.test import TestCase

from django.http import JsonResponse
from django.test import Client

from users.models import CustomUser as User
from api.tracks.models import Track
from django.db import transaction

from api.tracks.operators import *
from api.tracks.exceptions import *

import datetime


class CreatingTrackEntry(TestCase):

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


    def test_no_user(self):

        self.assertEqual(len(TrackEntry.objects.all()), 0)

        try:
            with transaction.atomic():

                result = createTrackEntry(
                        user = None,
                        track = self.track,
                        rating = 10,
                        date = '2000-09-23',
                        )
            self.fail('Did not raise an exception.')

        except InvalidUserError:
            pass

        except Exception:
            self.fail('Other exception was raised')


    def test_no_track(self):

        self.assertEqual(len(TrackEntry.objects.all()), 0)

        try:
            with transaction.atomic():

                result = createTrackEntry(
                        user = self.user,
                        track = None,
                        rating = 10,
                        date = '2000-09-23',
                        )
            self.fail('Did not raise an exception.')

        except InvalidTrackError:
            pass

        except Exception:
            self.fail('Other exception was raised')


    def test_no_rating(self):

        self.assertEqual(len(TrackEntry.objects.all()), 0)

        try:
            with transaction.atomic():

                result = createTrackEntry(
                        user = self.user,
                        track = self.track,
                        rating = None,
                        date = '2000-09-23',
                        )
            self.fail('Did not raise an exception.')

        except InvalidTrackEntryRatingError:
            pass

        except Exception:
            self.fail('Other exception was raised')


    def test_invalid_rating(self):
        pass


    def test_creating_track_entry(self):

        self.assertEqual(len(TrackEntry.objects.all()), 0)

        with transaction.atomic():
            result = createTrackEntry(
                    user = self.user,
                    track = self.track,
                    rating = 10,
                    date = '2000-09-23',
                    )

        self.assertEqual(len(TrackEntry.objects.all()), 1)
        
        saved = TrackEntry.objects.first()

        self.assertEqual(saved.rating, 10)
        self.assertEqual(saved.date, datetime.date(2000, 9, 23))

        self.assertEqual(result, saved)


    def test_modifying_track_entry(self):

        self.assertEqual(len(TrackEntry.objects.all()), 0)
        with transaction.atomic():
            result = createTrackEntry(
                    user = self.user,
                    track = self.track,
                    rating = 10,
                    date = '2000-09-23',
                    )
        self.assertEqual(len(TrackEntry.objects.all()), 1)
        saved = TrackEntry.objects.first()
        self.assertEqual(saved.rating, 10)
        self.assertEqual(saved.date, datetime.date(2000, 9, 23))
        self.assertEqual(result, saved)

        with transaction.atomic():
            result = createTrackEntry(
                    user = self.user,
                    track = self.track,
                    rating = 5,
                    date = '2000-09-23',
                    )

        self.assertEqual(len(TrackEntry.objects.all()), 1)
        saved = TrackEntry.objects.first()
        self.assertEqual(saved.rating, 5)
        self.assertEqual(saved.date, datetime.date(2000, 9, 23))
        self.assertEqual(result, saved)

