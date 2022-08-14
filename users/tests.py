from django.test import TestCase

from .helpers import generate_key

# Create your tests here.

class GeneratingKeys(TestCase):

    def test1(self):
        self.assertEqual(len(generate_key(120)), 120)
        self.assertEqual(len(generate_key(12)), 12)
        self.assertEqual(len(generate_key(10)), 10)
        self.assertEqual(len(generate_key(20)), 20)
        self.assertEqual(len(generate_key(1)), 1)
