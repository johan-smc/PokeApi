from business.stats.models import Stat


def create_stat(
        *,
        name: str,
) -> Stat:
    """Creates a new Stat in the date base with the values
    provided as parameters """
    stat = Stat(
        name=name
    )
    stat.full_clean()
    stat.save()
    return stat
