from business.pokemon.models import Pokemon, PokemonStat
from business.pokemon_species.models import PokemonSpecies
from business.stats.selectors import get_or_create_stat


def create_pokemon(
        *,
        id: int,
        name: str,
        height: int,
        weight: int,
        species: PokemonSpecies,
) -> Pokemon:
    """Creates a new Pokemon in the date base with the values
    provided as parameters """

    pokemon = Pokemon(
        id=id,
        name=name,
        height=height,
        weight=weight,
        species=species
    )
    pokemon.full_clean()
    pokemon.save()

    return pokemon


def create_pokemon_stat(
        *,
        base_stat: int,
        effort: int,
        pokemon: Pokemon,
        stat: dict
) -> PokemonStat:
    """Creates a new PokemonStat in the date base with the values
    provided as parameters """

    stat_db = get_or_create_stat(**stat)
    print(stat_db)
    pokemon_stat = PokemonStat(
        base_stat=base_stat,
        effort=effort,
        pokemon=pokemon,
        stat=stat_db
    )
    pokemon_stat.full_clean()
    pokemon_stat.save()

    return pokemon_stat
