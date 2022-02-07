from dataclasses import dataclass
from datetime import datetime

from sqlalchemy.ext.hybrid import hybrid_property

from app.create_app import db


@dataclass
class BaseModel(db.Model):
    id: int
    created_at: datetime
    updated_at: datetime

    @hybrid_property
    def id(self) -> int:
        """
        Gets the id of the entity
        :return: id of the entity
        """
        return self.__id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of the entity
        :param id: identifier of the entity
        """
        assert isinstance(id, int), type(id)
        assert id > 0, id

        self.__id = id

    @hybrid_property
    def created_at(self) -> datetime:
        """
        Gets the created_at datetime
        :return: datetime indicating when the entity was created
        """
        return self.__created_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        """
        Sets the created_at datetime of the entity
        :param created_at: datetime indicating when the entity was created
        """
        assert isinstance(created_at, datetime), type(created_at)
        self.__created_at = created_at

    @hybrid_property
    def updated_at(self) -> datetime:
        """
        Gets the updated_at datetime
        :return: datetime indicating when the entity was updated
        """
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, updated_at: datetime):
        """
        Sets the updated_at datetime of the entity
        :param updated_at: datetime indicating when the entity was updated
        """
        assert isinstance(updated_at, datetime), type(updated_at)
        self.__updated_at = updated_at

    __id = db.Column(db.BigInteger, primary_key=True)
    __created_at = db.Column("created_at", db.DateTime(timezone=True), server_default=db.func.now())
    __updated_at = db.Column("updated_at", db.DateTime(timezone=True), onupdate=db.func.now())
