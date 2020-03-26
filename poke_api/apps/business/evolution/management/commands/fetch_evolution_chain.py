from django.core.management import BaseCommand

from business.pokemon.services import fetch_pokemons_from_evolution_chain_by_id
from utils.constants import POKE_API_URL


class Command(BaseCommand):
    help = 'Fetch and save pokemons from evolution chain by an id,' \
           'The information is request to ' + POKE_API_URL

    def add_arguments(self, parser):
        parser.add_argument('id', type=int)

    def handle(self, *args, **options):
        id = options.get('id')
        fetch_pokemons_from_evolution_chain_by_id(id=id)
        self.stdout.write(
            self.style.SUCCESS('Successfully fetched content in '
                               'Evolution chain  "%s"' % id))
