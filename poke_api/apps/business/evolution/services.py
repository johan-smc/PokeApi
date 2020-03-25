from django.core.exceptions import ValidationError

from business.evolution.constants import URL_EVOLUTION_CHAIN
from business.evolution.models import ChainLink, EvolutionChain
from business.evolution.selectors import get_evolution_chain_by_id
from business.evolution.serializers import EvolutionChainSerializer, \
    ChainLinkSerializer
from business.pokemon_species.services import create_pokemon_species
from utils.requests import get_request


def create_evolution_chain(
        *,
        id: int,
        chain: dict,
) -> EvolutionChain:
    """Creates a new Evolution Chain in the date base with the values
    provided as parameters """

    if EvolutionChain.objects.filter(id=id).exists():
        raise ValidationError("Evolution chain exists.")

    chain = create_chain_link_from_raw_data(data=chain)

    evolution_chain = EvolutionChain(
        id=id,
        chain=chain
    )
    evolution_chain.full_clean()
    evolution_chain.save()

    return evolution_chain


def update_evolution_chain(
        *,
        id: int,
        chain: dict,
) -> EvolutionChain:
    """Update a Evolution Chain in the date base with the values provided as
    parameters """

    evolution_chain = get_evolution_chain_by_id(id=id)

    chain = create_chain_link_from_raw_data(data=chain)

    evolution_chain.chain = chain
    evolution_chain.full_clean()
    evolution_chain.save()

    return evolution_chain


def create_or_update_evolution_chain(
        *,
        id: int,
        chain: dict,
) -> EvolutionChain:
    """Create or update a Evolution Chain in the date base with the values
    provided as parameters """
    if EvolutionChain.objects.filter(id=id).exists():
        return update_evolution_chain(
            id=id,
            chain=chain
        )
    return create_evolution_chain(
        id=id,
        chain=chain
    )


def create_chain_link_from_raw_data(
        *,
        data: dict
) -> ChainLink:
    """
    Creates a new Chain link in the date base with the values provided as
    parameters in raw data
    """
    serializer = ChainLinkSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return create_chain_link(**serializer.validated_data)


def create_chain_link(
        *,
        species: dict,
        evolves_to: [dict] = None,
) -> ChainLink:
    """
    Creates a new Chain link in the date base with the values provided as
    parameters
    """
    species = create_pokemon_species(**species)
    chain_link = ChainLink(
        species=species
    )
    chain_link.full_clean()
    chain_link.save()
    for evolve in evolves_to:
        chain_link.evolves_to.add(create_chain_link_from_raw_data(data=evolve))
    chain_link.full_clean()
    chain_link.save()

    return chain_link


def fetch_evolution_chain_from_id(
        *,
        id: int
) -> EvolutionChain:
    """
    Fetch and save a evolution chain from an id, with the url saved in
    constants file
    :param id:int
    :return evolution_chain:EvolutionChain
    """
    url = URL_EVOLUTION_CHAIN + str(id)
    json = get_request(url=url)
    serializer = EvolutionChainSerializer(data=json)
    serializer.is_valid(raise_exception=True)
    return create_or_update_evolution_chain(**serializer.validated_data)
