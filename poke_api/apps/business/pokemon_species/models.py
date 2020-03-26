from django.db import models


class PokemonSpecies(models.Model):
    name = models.CharField(max_length=255)
