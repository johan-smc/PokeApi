import urllib.request
import io

from rest_framework.parsers import JSONParser


def get_request(
        *,
        url: str
) -> str:
    """
    Return a json response result of get petition of the web page in url
    :param url: The url of the web page to request
    :return json:  Json response of the page
    """
    request = urllib.request.Request(url)
    request.add_header('User-Agent', "cheese")
    data = urllib.request.urlopen(request).read()
    return JSONParser().parse(io.BytesIO(data))
