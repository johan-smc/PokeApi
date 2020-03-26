from django.test import TestCase

from business.evolution.models import ChainLink
from business.evolution.services import create_chain_link, \
    create_chain_link_from_raw_data


class CreateChainLinkTests(TestCase):
    """Group of tests that ensures check if a chain link is being created
    correctly """

    def setUp(self):
        self.data = {
            'species': {
                'name': 'test'
            },
            'evolves_to': []
        }
        self.service = create_chain_link

    def test_create_chain_link(self):
        self.assertEqual(0, ChainLink.objects.count())
        new_chain_link = self.service(**self.data)
        self.assertEqual(1, ChainLink.objects.count())
        self.assertEqual(new_chain_link, ChainLink.objects.first())

    def test_create_chain_link_depth(self):
        self.assertEqual(0, ChainLink.objects.count())
        self.data['evolves_to'].append({
            'species': {
                'name': 'second'
            },
            'evolves_to': []
        })
        self.service(**self.data)
        self.assertEqual(2, ChainLink.objects.count())

    def test_create_chain_from_raw_data(self):
        self.assertEqual(0, ChainLink.objects.count())
        self.data['evolves_to'].append({
            'species': {
                'name': 'second'
            },
            'evolves_to': []
        })
        create_chain_link_from_raw_data(data=self.data)
        self.assertEqual(2, ChainLink.objects.count())

    def test_create_chain_link_depth_2_levels(self):
        self.assertEqual(0, ChainLink.objects.count())
        self.data['evolves_to'].append({
            'species': {
                'name': 'second'
            },
            'evolves_to': [{
                'species': {
                    'name': 'second'
                },
                'evolves_to': []
            }]
        })
        final = self.service(**self.data)
        self.assertEqual(3, ChainLink.objects.count())
