from enum import Enum


class Routes(Enum):
    """
    Enum class that keeps the routes for the API entities
    """

    """ Pre-fix for all API URLs """
    API_BASE = "/api/v1"

    """ API route to shorten a URL """
    SHORTEN_URL = f"{API_BASE}/shortenUrl"

    """ API route to get a long URL from a shortened one """
    SHORT_URL = f"{API_BASE}/shortUrl"
