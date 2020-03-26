from django.utils.translation import ugettext_lazy as _
from django.db import models

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
