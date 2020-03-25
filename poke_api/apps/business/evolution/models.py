from django.utils.translation import ugettext_lazy as _
from django.db import models

from business.pokemon_species.models import PokemonSpecies


class ChainLink(models.Model):
    evolves_to = models.ManyToManyField(
        "self",
        related_name='chain_link',
        verbose_name=_(u'evolves_to'),
    )
    species = models.OneToOneField(
        PokemonSpecies,
        on_delete=models.PROTECT,
        related_name='chain_link',
        verbose_name=_(u'species')
    )


class EvolutionChain(models.Model):
    id = models.IntegerField(primary_key=True)
    chain = models.OneToOneField(
        ChainLink,
        on_delete=models.PROTECT,
        related_name='evolution_chain',
        verbose_name=_(u'chain')
    )
