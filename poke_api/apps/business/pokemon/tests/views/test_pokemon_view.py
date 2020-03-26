from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from business.pokemon.models import Pokemon, PokemonStat
from business.pokemon_species.models import PokemonSpecies
from business.stats.models import Stat


class GetPokemonByIdTests(APITestCase):

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

    def test_get_company_by_owner(self):
        url = reverse('pokemon', args=(self.pokemon.name, ))
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.data.get('id'), self.data.get('id'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
