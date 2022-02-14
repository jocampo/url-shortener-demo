from zlib import adler32

from sqlalchemy.exc import NoResultFound

from db.dao.shortened_url_dao import ShortenedUrlDAO
from db.models.shortened_url import ShortenedUrl


class UrlShortenerService:
    """
    Contains logic around shortening and resolving URLs
    """

    @staticmethod
    def shorten_url(long_url: str) -> str:
        """
        Shortens a URL and returns it.
        :return: shortened URL
        """
        short_url = UrlShortenerService.__hash_url(long_url)
        entity = ShortenedUrl(short_url=short_url, long_url=long_url, hits=0)
        ShortenedUrlDAO.create(entity)
        return short_url

    @staticmethod
    def __hash_url(long_url: str) -> str:
        """
        todo: doc me
        :return:
        """
        # Trims a part of the hex value to make the hash shorter, but risking collisions
        hashed_url = hex(adler32(long_url.encode("utf-8")))[2:-2]

        # If the hashed url already exists in the db, then try again, but suffix a preset string to the URL first to
        # "provoke" changes in the hashed value
        if not UrlShortenerService.__check_hash_validity(hashed_url):
            # TODO: This hits the db every time there's a conflicting hashed url. AKA inefficient af, probably change
            # approach re: how the url is hashed.
            return UrlShortenerService.__hash_url(long_url + UrlShortenerService.__HASH_RANDOMIZER_PRESET)
        else:
            return hashed_url

    @staticmethod
    def __check_hash_validity(hashed_url: str) -> bool:
        """
        todo: doc me
        :param hashed_url:
        :return:
        """
        try:
            ShortenedUrlDAO.get_by_short_url(hashed_url)
        except NoResultFound:
            return True
        return False

    """ Preset string to be suffixed to a URL in case the hashed value already exists """
    __HASH_RANDOMIZER_PRESET = "UrlShortenerApp"
