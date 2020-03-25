from rest_framework import serializers


class PokemonSpeciesSerializer(serializers.Serializer):
    name = serializers.CharField()
