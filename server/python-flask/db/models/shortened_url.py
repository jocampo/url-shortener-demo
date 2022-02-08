from dataclasses import dataclass

from sqlalchemy import Column, String, BigInteger

from sqlalchemy.ext.hybrid import hybrid_property

from db.models.base_model import BaseModel


@dataclass
class ShortenedUrl(BaseModel):
    short_url: str
    long_url: str
    hits: int

    @hybrid_property
    def short_url(self) -> str:
        """
        Gets the shortened url
        :return: shortened url of the entity
        """
        return self.__short_url

    @short_url.setter
    def short_url(self, short_url: str):
        """
        Sets the shortened url of the entity
        :param short_url: short url of the entity
        """
        assert isinstance(short_url, str), type(short_url)
        assert short_url, short_url

        self.__short_url = short_url

    @hybrid_property
    def long_url(self) -> str:
        """
        Gets the long url
        :return: long url of the entity
        """
        return self.__long_url

    @long_url.setter
    def long_url(self, long_url: str):
        """
        Sets the long url of the entity
        :param long_url: long url of the entity
        """
        assert isinstance(long_url, str), type(long_url)
        assert long_url, long_url

        self.__long_url = long_url

    @hybrid_property
    def hits(self) -> int:
        """
        Gets the number of hits of the shortened url
        :return: number of hits of the entity
        """
        return self.__hits

    @hits.setter
    def hits(self, hits: int):
        """
        Sets the number of hits of the entity
        :param hits: number of hits of the url
        """
        assert isinstance(hits, int), type(hits)
        assert hits > 0, hits

        self.__hits = hits

    __short_url = Column("short_url", String, nullable=False)
    __long_url = Column("long_url", String, nullable=False)
    __hits = Column("hits", BigInteger, nullable=False, default=0)
    __tablename__ = 'url'

    def __repr__(self):
        return f"<URL Model@{self.__id}: {self.__short_url} <-> {self.__long_url}>"
