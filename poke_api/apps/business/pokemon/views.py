from rest_framework import status, viewsets, serializers
from rest_framework.response import Response

from business.pokemon.models import Pokemon
from business.pokemon.selectors import get_pokemon_by_id, get_pokemon_by_name
from utils.mixins import ExceptionHandlerMixin
from utils.serializers import inline_serializer


class PokemonViewSet(ExceptionHandlerMixin, viewsets.ViewSet):
    """
    View set for Pokemon Model
    """

    class OutputSerializer(serializers.ModelSerializer):
        species = inline_serializer(
            fields={
                'name': serializers.CharField(),
            },
        )
        stats = inline_serializer(
            fields={
                'base_stat': serializers.IntegerField(),
                'effort': serializers.IntegerField(),
                'stat': inline_serializer(
                    fields={
                        'name': serializers.CharField()
                    }
                )
            },
            many=True
        )
        all_evolutions = inline_serializer(
            fields={
                'name': serializers.CharField(),
                'id': serializers.CharField(),
                'type': serializers.CharField(),
            },
            many=True
        )

        class Meta:
            model = Pokemon
            fields = (
                'id',
                'name',
                'height',
                'weight',
                'species',
                'stats',
                'all_evolutions'
            )

    def get_pokemon_by_name(self, request, name):
        """
        return pokemon with serializer output by id in request param
        """
        company_serializer = self.OutputSerializer(
            get_pokemon_by_name(name=name),
            many=False
        )
        return Response(company_serializer.data, status=status.HTTP_200_OK)
