from abc import ABC

from db.dao.abstract_dao import AbstractDAO
from db.models.base_model import BaseModel
from app.create_app import db
from db.models.shortened_url import ShortenedUrl


class ShortenedUrlDAO(AbstractDAO):
    """
    Shortened URL DAO that contains specific operations for this entity type in the db
    """

    @staticmethod
    def get_by_short_url(short_url: str) -> ShortenedUrl:
        """
        Fetches the url record based on the provided shortened url.
        :param short_url: shortened version of the URL to look for in the db
        :return matching SQLAlchemy entity from the database
        """
        assert short_url, short_url
        return (db.session.connection
                .query(ShortenedUrl)
                .filter(ShortenedUrl.short_url == short_url)
                .one())

    @staticmethod
    def get_by_long_url(long_url: str) -> ShortenedUrl:
        """
        Fetches the url record based on the provided long/original url.
        :param long_url: long version of the URL to look for in the db
        :return matching SQLAlchemy entity from the database
        """
        assert long_url, long_url
        return (db.session.connection
                .query(ShortenedUrl)
                .filter(ShortenedUrl.long_url == long_url)
                .one())
