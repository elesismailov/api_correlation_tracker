from django.test import TestCase

from django.http import JsonResponse
from django.test import Client

from users.models import CustomUser as User
from api.tracks.models import Track
from django.db import transaction

from api.tracks.operators import *
from api.tracks.exceptions import *

import datetime


class DeletingTracks(TestCase):

    def setUp(self):

        # Create test user
        self.user = User.objects.create_user(
                    username='testuser',
                    email='testuser@gmail.com',
                    password='123'
                )

    
    def test_invalid_id(self):

        with transaction.atomic():
            c = createTrack( user=self.user, title='title1',)

        try:
            d = deleteTrack(track_id=c.id+1231)

            self.fail('Did not raise an exception.')

        except Track.DoesNotExist:
            pass

        except Exception:
            self.fail('Other exception was raised')


    def test_no_id(self):

        with transaction.atomic():
            c = createTrack( user=self.user, title='title1',)

        try:
            d = deleteTrack(track_id=None)

            self.fail('Did not raise an exception.')

        except InvalidTrackError:
            pass

        except Exception:
            self.fail('Other exception was raised')
    
    
    def test_deletion(self):

        self.assertEqual(Track.objects.count(), 0)

        with transaction.atomic():
            c = createTrack(user=self.user, title='title1')

        self.assertEqual(Track.objects.count(), 1)

        d = deleteTrack(track_id=c.id)

        self.assertEqual(Track.objects.count(), 0)
        

    def test_returns_track(self):

        self.assertEqual(Track.objects.count(), 0)

        with transaction.atomic():
            c = createTrack(user=self.user, title='title1')

        self.assertEqual(Track.objects.count(), 1)

        d = deleteTrack(track_id=c.id)

        self.assertEqual(Track.objects.count(), 0)
        self.assertIsInstance(d, Track)
    
    
    
    
    
    
    
    
    
    
    
    
    
