from django.core.exceptions import ValidationError

from business.pokemon.models import Pokemon


def get_pokemon_by_id(
        *,
        id: int
) -> Pokemon:
    """
    Return a Pokemon by id, if the element not exists raise a error.
    """
    pokemon = Pokemon.objects.filter(id=id)
    if not pokemon.exists():
        raise ValidationError("Pokemon not exists.")
    return pokemon[0]


def get_pokemon_by_name(
        *,
        name: str
) -> Pokemon:
    """
    Return a Pokemon by name, if the element not exists raise a error.
    """
    pokemon = Pokemon.objects.filter(name=name)
    if not pokemon.exists():
        raise ValidationError("Pokemon not exists.")
    return pokemon[0]
