from django.core.exceptions import ValidationError
from django.test import TestCase

from business.evolution.models import ChainLink, EvolutionChain
from business.evolution.selectors import get_evolution_chain_by_id
from business.pokemon_species.models import PokemonSpecies


class GetSingleEvolutionChainTests(TestCase):
    """Group of tests that check if evolution chain are fetched correctly"""

    def setUp(self):
        self.pokemon_species = PokemonSpecies.objects.create(name="test")
        self.chain = ChainLink.objects.create(species=self.pokemon_species)
        self.data = {
            'id': 1,
            'chain': self.chain
        }
        self.evolution_chain = EvolutionChain.objects.create(**self.data)
        self.selector = get_evolution_chain_by_id

    def test_get_evolution_chain_by_id(self):
        """
        Fetched  evolution chain by id and compare with the course create
        """
        response = self.selector(
            id=self.evolution_chain.id
        )
        self.assertEqual(self.evolution_chain, response)

    def test_evolution_chain_not_exists(self):
        """
        Fetched  evolution chain by id  whit invalid id
         and verify if the exception handler
        """
        with self.assertRaises(ValidationError):
            self.selector(
                id=-1
            )
