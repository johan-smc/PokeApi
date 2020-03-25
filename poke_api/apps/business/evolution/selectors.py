from django.core.exceptions import ValidationError

from business.evolution.models import EvolutionChain


def get_evolution_chain_by_id(
        *,
        id: int
) -> EvolutionChain:
    """
    Return a EvolutionChain by id, if the element not exists raise a error.
    """
    evolution_chain = EvolutionChain.objects.filter(id=id)
    if not evolution_chain.exists():
        raise ValidationError("EvolutionChain not exists.")
    return evolution_chain[0]
