from django.test import TestCase

# Create your tests here.

from django.http import JsonResponse
from django.test import Client

from users.models import CustomUser as User
from api.tracks.models import Track
from django.db import transaction

from api.tracks.operators import createTrack
from api.tracks.exceptions import *


class CreatingTrack(TestCase):

    def setUp(self):

        # Create test user
        self.user = User.objects.create_user(
                    username='testuser',
                    email='testuser@gmail.com',
                    password='123'
                )

    def test_creating(self):

        self.assertEqual(len(Track.objects.all()), 0)

        with transaction.atomic():

            result = createTrack(
                    user=self.user,
                    title='Testing Title',
                    )

        self.assertEqual(result, Track.objects.first())

    def test_no_user(self):

        self.assertEqual(len(Track.objects.all()), 0)

        try:
            with transaction.atomic():

                result = createTrack(
                        user=None,
                        title='Testing Title',
                        )
            self.fail('Did not raise an exception.')

        except InvalidUserError:
            pass

        except Exception:
            self.fail('Other exception was raised')


    def test_no_title(self):

        self.assertEqual(len(Track.objects.all()), 0)

        try:
            with transaction.atomic():

                result = createTrack(
                        user=self.user,
                        title=None,
                        )
            self.fail('Did not raise an exception.')

        except InvalidTrackTitleError:
            pass

        except Exception:
            self.fail('Other exception was raised')

    def test_already_exists(self):

        self.assertEqual(len(Track.objects.all()), 0)

        # create first track
        with transaction.atomic():
            result = createTrack(
                    user=self.user,
                    title='Test Title',
                    )

        # check track was created
        self.assertEqual(len(Track.objects.all()), 1)

        try:
            with transaction.atomic():

                result = createTrack(
                        user=self.user,
                        title='Test Title',
                        )

            self.fail('Did not raise an exception.')

        except TrackAlreadyExistsError:
            pass

        except Exception:
            self.fail('Other exception was raised')







