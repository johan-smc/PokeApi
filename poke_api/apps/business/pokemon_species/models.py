from django.utils.translation import ugettext_lazy as _
from django.db import models


class PokemonSpecies(models.Model):
    name = models.CharField(max_length=255)
    evolves_from_species = models.OneToOneField(
        "self",
        on_delete=models.PROTECT,
        related_name='pokemon_species',
        verbose_name=_(u'evolves_from_species'),
        null=True,
        blank=True
    )
