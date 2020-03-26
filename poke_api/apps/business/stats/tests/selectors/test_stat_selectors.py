from django.test import TestCase

from business.stats.models import Stat
from business.stats.selectors import get_or_create_stat


class GetSingleStatTests(TestCase):
    """Group of tests that check if stat are fetched correctly"""

    def setUp(self):
        self.data = {
            'name': 'test'
        }
        self.stat = Stat.objects.create(**self.data)
        self.selector = get_or_create_stat

    def test_get_stat_by_id(self):
        """
        Fetched  evolution chain by id and compare with the course create
        """
        response = self.selector(
            **self.data
        )
        self.assertEqual(self.stat, response)

    def test_stat_not_exists(self):
        """
        Fetched  evolution chain by id  whit invalid id
         and verify if the stat is created
        """
        self.data['name'] = 'test2'
        self.selector(**self.data)
        self.assertEqual(2, Stat.objects.count())
