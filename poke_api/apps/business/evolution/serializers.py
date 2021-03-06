from rest_framework import serializers

from business.evolution.models import ChainLink
from business.pokemon_species.serializers import PokemonSpeciesSerializer


class ChainLinkSerializer(serializers.Serializer):
    evolves_to = serializers.ListField()
    species = PokemonSpeciesSerializer()

    class Meta:
        model = ChainLink


class EvolutionChainSerializer(serializers.Serializer):
    id = serializers.CharField()
    chain = ChainLinkSerializer()
