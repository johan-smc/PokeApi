from django.core.exceptions import ValidationError
from django.test import TestCase

from business.stats.models import Stat
from business.stats.services import create_stat


class CreateStatTests(TestCase):
    """Group of tests that ensures check if a stat is being created
    correctly """

    def setUp(self):
        self.data = {
            'name': 'test'
        }
        self.service = create_stat

    def test_create_stat(self):
        self.assertEqual(0, Stat.objects.count())
        new_stat = self.service(**self.data)
        self.assertEqual(1, Stat.objects.count())
        self.assertEqual(new_stat, Stat.objects.first())
