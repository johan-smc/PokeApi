from unittest import mock

from django.core.exceptions import ValidationError
from django.test import TestCase

from business.evolution.models import EvolutionChain, ChainLink
from business.evolution.services import create_evolution_chain, \
    update_evolution_chain, create_or_update_evolution_chain, \
    fetch_evolution_chain_from_id
from business.pokemon_species.models import PokemonSpecies


class CreateEvolutionChainTests(TestCase):
    """Group of tests that ensures check if a evolution chain is being created
    correctly """

    def setUp(self):
        self.data = {
            'id': 1,
            'chain': {
                'species': {
                    'name': 'test'
                },
                'evolves_to': []
            }
        }
        self.service = create_evolution_chain

    def test_create_evolution_chain(self):
        self.assertEqual(0, EvolutionChain.objects.count())
        new_evolution_chain = self.service(**self.data)
        self.assertEqual(1, EvolutionChain.objects.count())
        self.assertEqual(new_evolution_chain, EvolutionChain.objects.first())


class UpdateEvolutionChainTests(TestCase):
    """Group of tests that ensures check if a evolution chain is being updated
    correctly """

    def setUp(self):
        self.pokemon_species = PokemonSpecies.objects.create(name="test")
        self.chain = ChainLink.objects.create(species=self.pokemon_species)
        self.data = {
            'id': 1,
            'chain': self.chain
        }
        self.evolution_chain = EvolutionChain.objects.create(**self.data)
        self.service = update_evolution_chain

    def test_update_evolution_chain(self):
        self.assertEqual(1, EvolutionChain.objects.count())
        self.data['id'] = self.evolution_chain.id
        self.data['chain'] = {
            'species': {
                'name': 'MM'
            },
            'evolves_to': []
        }
        now_evolution_chain = self.service(**self.data)
        self.assertEqual(1, EvolutionChain.objects.count())
        self.assertEqual(now_evolution_chain, EvolutionChain.objects.first())

    def test_update_evolution_chain_not_exists(self):
        self.assertEqual(1, EvolutionChain.objects.count())
        self.data['id'] = -1
        with self.assertRaises(ValidationError):
            self.service(**self.data)


class CreateOrUpdateEvolutionChainTests(TestCase):
    """Group of tests that ensures check if a evolution chain is being updated
    or created correctly """

    def setUp(self):
        self.pokemon_species = PokemonSpecies.objects.create(name="test")
        self.chain = ChainLink.objects.create(species=self.pokemon_species)
        self.data = {
            'id': 1,
            'chain': self.chain
        }
        self.evolution_chain = EvolutionChain.objects.create(**self.data)
        self.service = create_or_update_evolution_chain

    def test_update_evolution_chain(self):
        self.assertEqual(1, EvolutionChain.objects.count())
        self.data['id'] = self.evolution_chain.id
        self.data['chain'] = {
            'species': {
                'name': 'MM'
            },
            'evolves_to': []
        }
        now_evolution_chain = self.service(**self.data)
        self.assertEqual(1, EvolutionChain.objects.count())
        self.assertEqual(now_evolution_chain, EvolutionChain.objects.first())

    def test_create_evolution_chain_not_exists(self):
        self.assertEqual(1, EvolutionChain.objects.count())
        self.data['id'] = 2
        self.data['chain'] = {
            'species': {
                'name': 'MM'
            },
            'evolves_to': []
        }
        self.service(**self.data)
        self.assertEqual(2, EvolutionChain.objects.count())


class CreateFetchEvolutionChainFromIdTests(TestCase):
    """Group of tests that ensures check if a evolution is being created
    correctly """

    def setUp(self):
        self.data = {
            "id": 1,
            "chain": {
                "species": {
                    "name": "rattata",
                },
                "evolves_to": [
                    {
                        "species": {
                            "name": "raticate",
                        },
                        "evolves_to": []
                    }
                ]
            }
        }
        self.service = fetch_evolution_chain_from_id

    @mock.patch('business.evolution.services.get_request')
    def test_fetch_evolution_chain_from_id(self, mock_get):
        mock_get.return_value = self.data
        self.assertEqual(0, EvolutionChain.objects.count())
        new_pokemon = self.service(
            id=1
        )
        self.assertEqual(1, EvolutionChain.objects.count())
        self.assertEqual(new_pokemon, EvolutionChain.objects.first())
