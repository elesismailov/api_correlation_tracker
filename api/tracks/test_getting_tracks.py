from django.test import TestCase

from django.http import JsonResponse
from django.test import Client

from users.models import CustomUser as User
from api.tracks.models import Track
from django.db import transaction

from api.tracks.operators import *
from api.tracks.exceptions import *

import datetime


class GettingAllTracks(TestCase):

    def setUp(self):

        # Create test user
        self.user = User.objects.create_user(
                    username='testuser',
                    email='testuser@gmail.com',
                    password='123'
                )

    def test_getting_array(self):

        result = getTracks(
                user = self.user,
                )

        self.assertIsInstance(result, list)

    
    def test_getting_tracks(self):

        with transaction.atomic():
            createTrack( user=self.user, title='title1',)
            createTrack( user=self.user, title='title2',)
            createTrack( user=self.user, title='title3',)
        
        result = getTracks(user=self.user)

        self.assertIsInstance(result, list)
        self.assertEqual(result[0].title, 'title1')
        self.assertEqual(result[1].title, 'title2')
        self.assertEqual(result[2].title, 'title3')

        
    def test_getting_limit(self):
        
        with transaction.atomic():
            for i in range(20):
                createTrack(user=self.user, title='title' + str(i))

        self.assertEqual(len(getTracks(user=self.user)), 7)

        self.assertEqual(len(getTracks(user=self.user, limit=11)), 11)


    def test_no_user(self):

        with transaction.atomic():
            createTrack( user=self.user, title='title1',)

        try:
            tracks = getTracks(user=None)

            self.fail('Did not raise an exception.')

        except InvalidUserError:
            print('Landed NoUserError.')

        except Exception:
            self.fail('Other exception was raised')













