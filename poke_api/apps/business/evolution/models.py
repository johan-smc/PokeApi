from django.utils.translation import ugettext_lazy as _
from django.db import models

from business.pokemon_species.models import PokemonSpecies


class ChainLink(models.Model):
    evolves_from = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name='chain_link',
        verbose_name=_(u'evolves_from'),
        null=True,
        blank=True
    )
    species = models.OneToOneField(
        PokemonSpecies,
        on_delete=models.PROTECT,
        related_name='chain_link',
        verbose_name=_(u'species')
    )

    @property
    def evolves_to(self):
        return ChainLink.objects.filter(evolves_from__id=self.id)


class EvolutionChain(models.Model):
    id = models.IntegerField(primary_key=True)
    chain = models.OneToOneField(
        ChainLink,
        on_delete=models.PROTECT,
        related_name='evolution_chain',
        verbose_name=_(u'chain')
    )
