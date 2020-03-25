
from business.stats.models import Stat
from business.stats.services import create_stat


def get_or_create_stat(
        *,
        name: str
) -> Stat:
    """
    Return a Stat by name, if the element not exists create the element.
    """
    stat = Stat.objects.filter(name=name)
    if not stat.exists():
        return create_stat(name=name)
    return stat[0]
