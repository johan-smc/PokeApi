from rest_framework import serializers

from business.pokemon_species.serializers import PokemonSpeciesSerializer
from business.stats.serializers import StatSerializer


class PokemonStatSerializer(serializers.Serializer):
    base_stat = serializers.IntegerField()
    effort = serializers.IntegerField()
    stat = StatSerializer()


class PokemonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    height = serializers.IntegerField()
    weight = serializers.IntegerField()
    stats = PokemonStatSerializer(many=True)
    species = PokemonSpeciesSerializer()
