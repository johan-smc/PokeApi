from business.evolution.models import ChainLink
from business.evolution.services import fetch_evolution_chain_from_id
from business.pokemon.constants import URL_POKEMON
from business.pokemon.models import Pokemon, PokemonStat
from business.pokemon.selectors import get_pokemon_by_id
from business.pokemon.serializers import PokemonSerializer
from business.pokemon_species.models import PokemonSpecies
from business.stats.selectors import get_or_create_stat
from utils.requests import get_request


def create_pokemon(
        *,
        id: int,
        name: str,
        height: int,
        weight: int,
        species: PokemonSpecies,
        stats: dict
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

    for stat in stats:
        stat['pokemon'] = pokemon
        create_pokemon_stat(**stat)

    return pokemon


def update_pokemon(
        *,
        id: int,
        name: str,
        height: int,
        weight: int,
        species: PokemonSpecies,
        stats: dict
) -> Pokemon:
    """Update a Pokemon in the date base with the values provided as
    parameters """

    pokemon = get_pokemon_by_id(id=id)

    pokemon.name = name
    pokemon.height = height
    pokemon.weight = weight
    pokemon.species = species
    pokemon.full_clean()
    pokemon.save()

    for stat in stats:
        stat['pokemon'] = pokemon
        create_pokemon_stat(**stat)

    return pokemon


def create_or_update_pokemon(
        *,
        id: int,
        name: str,
        height: int,
        weight: int,
        species: PokemonSpecies,
        stats: dict
) -> Pokemon:
    """Create or update a Pokemon in the date base with the values
    provided as parameters """
    if Pokemon.objects.filter(id=id).exists():
        return update_pokemon(
            id=id,
            name=name,
            height=height,
            weight=weight,
            species=species,
            stats=stats
        )
    return create_pokemon(
        id=id,
        name=name,
        height=height,
        weight=weight,
        species=species,
        stats=stats
    )


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
    pokemon_stat = PokemonStat(
        base_stat=base_stat,
        effort=effort,
        pokemon=pokemon,
        stat=stat_db
    )
    pokemon_stat.full_clean()
    pokemon_stat.save()

    return pokemon_stat


def create_pokemon_by_species(
        *,
        species: PokemonSpecies
) -> Pokemon:
    """
    Creates a new Pokemon in the date base with the values provided as
    parameters in raw data, execute a query to api pokeapi and save this
    information in a Pokemon
    """

    url = URL_POKEMON + species.name
    json = get_request(url=url)
    serializer = PokemonSerializer(data=json)
    serializer.is_valid(raise_exception=True)
    serializer.validated_data['species'] = species
    return create_or_update_pokemon(**serializer.validated_data)


def create_pokemon_by_chain_link(
        *,
        chain_link: ChainLink
) -> None:
    """
    Creates a new Pokemon in the date base with the values provided as
    parameters in raw data, this function execute recursive in every chain link
    """
    create_pokemon_by_species(species=chain_link.species)
    evolves_to = chain_link.evolves_to.all()
    for chain in evolves_to:
        create_pokemon_by_chain_link(chain_link=chain)


def fetch_pokemons_from_evolution_chain_by_id(
        *,
        id: int
) -> None:
    """
    Fetch and save pokemons from evolution chain by an id, with the url save in
    constants file
    :param id:int
    :return evolution_chain:EvolutionChain
    """
    evolution_chain = fetch_evolution_chain_from_id(id=id)
    create_pokemon_by_chain_link(chain_link=evolution_chain.chain)
