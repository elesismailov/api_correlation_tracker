from django.test import TestCase

from django.http import JsonResponse
from django.test import Client

from users.models import CustomUser as User
from api.tracks.models import Track
from django.db import transaction

from api.tracks.operators import *
from api.tracks.exceptions import *

import datetime


class DeletingTrackEntries(TestCase):

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


    def test_returns_entry(self):
        with transaction.atomic():
            created = createTrackEntry(
                    track = self.track,
                    rating = 4,
                    date = '2000-09-21',
                    )

        self.assertEqual(TrackEntry.objects.count(), 1)

        deleted = deleteTrackEntry(entry_id=created.id)

        self.assertIsInstance(deleted, TrackEntry)


    def test_deleting(self):

        with transaction.atomic():
            created = createTrackEntry(
                    track = self.track,
                    rating = 4,
                    date = '2000-09-21',
                    )

        self.assertEqual(TrackEntry.objects.count(), 1)

        deleted = deleteTrackEntry(entry_id=created.id)

        self.assertEqual(TrackEntry.objects.count(), 0)


    def test_none_id(self):

        self.assertEqual(TrackEntry.objects.count(), 0)

        try:

            deleted = deleteTrackEntry(entry_id=None)
            self.fail('Did not raise an exception.')

        except InvalidTrackEntryError:
            pass

        except Exception:
            self.fail('Other exception was raised')


    def test_invalid_id(self):

        with transaction.atomic():
            created = createTrackEntry(
                    track = self.track,
                    rating = 4,
                    date = '2000-09-21',
                    )

        self.assertEqual(TrackEntry.objects.count(), 1)

        try:

            deleted = deleteTrackEntry(entry_id=created.id+1234)
            self.fail('Did not raise an exception.')

        except TrackEntry.DoesNotExist:
            pass

        except Exception:
            self.fail('Other exception was raised')



















