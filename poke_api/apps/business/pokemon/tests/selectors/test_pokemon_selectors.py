from django.core.exceptions import ValidationError
from django.test import TestCase

from business.pokemon.models import Pokemon
from business.pokemon.models import PokemonStat
from business.pokemon.selectors import get_pokemon_by_id, get_pokemon_by_name
from business.pokemon_species.models import PokemonSpecies
from business.stats.models import Stat


class GetSinglePokemonTests(TestCase):
    """Group of tests that check if Pokemon are fetched correctly"""

    def setUp(self):
        self.pokemon_species = PokemonSpecies.objects.create(name="test")
        self.data = {
            'id': 1,
            'name': 'test',
            'height': 12,
            'weight': 13,
            'species': self.pokemon_species,
        }
        self.pokemon = Pokemon.objects.create(**self.data)
        self.stat = Stat.objects.create(name="speed")
        self.pokemon_stat = PokemonStat.objects.create(
            base_stat=12,
            effort=12,
            pokemon=self.pokemon,
            stat=self.stat
        )

    def test_get_pokemon_by_id(self):
        """
        Fetched  Pokemon by id and compare with the course create
        """
        response = get_pokemon_by_id(
            id=self.pokemon.id
        )
        self.assertEqual(self.pokemon, response)

    def test_pokemon_not_exists_by_id(self):
        """
        Fetched  Pokemon by id  whit invalid id
         and verify if the exception handler
        """
        with self.assertRaises(ValidationError):
            get_pokemon_by_id(
                id=-1
            )

    def test_get_pokemon_by_name(self):
        """
        Fetched  Pokemon by name and compare with the course create
        """
        response = get_pokemon_by_name(
            name=self.pokemon.name
        )
        self.assertEqual(self.pokemon, response)

    def test_pokemon_not_exists_by_name(self):
        """
        Fetched  Pokemon by name  whit invalname name
         and verify if the exception handler
        """
        with self.assertRaises(ValidationError):
            get_pokemon_by_name(
                name=''
            )
