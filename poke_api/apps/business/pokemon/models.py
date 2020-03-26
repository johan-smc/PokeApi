from django.utils.translation import ugettext_lazy as _
from django.db import models

from business.evolution.models import ChainLink
from business.pokemon_species.models import PokemonSpecies
from business.stats.models import Stat


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    height = models.IntegerField()
    weight = models.IntegerField()
    species = models.OneToOneField(
        PokemonSpecies,
        on_delete=models.CASCADE,
        related_name='pokemon',
        verbose_name=_(u'species')
    )

    @property
    def stats(self):
        return PokemonStat.objects.filter(pokemon__id=self.id)

    def evolutions(self):
        chain_link = ChainLink.objects.get(species__id=self.species.id)\
            .evolves_from
        evolves_from = []
        if chain_link is not None:
            pokemon = chain_link.species.pokemon
            pokemon.type = "Evolution"
            evolves_from.append(pokemon)
            evolves_from += pokemon.evolutions()
        return evolves_from

    def preevolution(self):
        chain_link = ChainLink.objects.get(species__id=self.species.id)\
            .evolves_to
        evolves_to = []
        for chain in chain_link:
            pokemon = chain.species.pokemon
            pokemon.type="PreEvolution"
            evolves_to.append(pokemon)
            evolves_to += pokemon.preevolution()
        return evolves_to

    @property
    def all_evolutions(self):
        return self.preevolution() + self.evolutions()


class PokemonStat(models.Model):
    base_stat = models.IntegerField()
    effort = models.IntegerField()
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.PROTECT,
        related_name='stats',
        verbose_name=_(u'pokemon')
    )
    stat = models.ForeignKey(
        Stat,
        on_delete=models.CASCADE,
        related_name='pokemon_stat',
        verbose_name=_(u'stat')
    )
