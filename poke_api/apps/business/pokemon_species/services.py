from business.pokemon_species.models import PokemonSpecies


def create_pokemon_species(
        *,
        name: str,
) -> PokemonSpecies:
    """Creates a new PokemonSpecies in the date base with the values
    provided as parameters """

    pokemon_species = PokemonSpecies(
        name=name
    )
    pokemon_species.full_clean()
    pokemon_species.save()
    return pokemon_species
