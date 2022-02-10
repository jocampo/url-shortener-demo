from abc import ABC

from db.models.base_model import BaseModel
from app.create_app import db


class AbstractDAO(ABC):
    """
    Base class for DAOs. Needs to be extended for more complex handling of objects in the DB.
    The idea is to NOT have to pass around/import the db object everywhere.
    """

    @staticmethod
    def create(entity):
        """
        Generic implementation to create a given entity. Useful for creates/updates
        :param entity: SQLAlchemy entity
        """
        assert entity
        db.session.add(entity)
        db.session.commit()

    @staticmethod
    def delete(entity: BaseModel):
        """
        Generic implementation for the delete operation of a given entity
        :param entity: SQLAlchemy entity
        """
        assert entity
        assert entity.id > 0
        db.session.delete(entity)
        db.session.commit()

    @staticmethod
    def get(entity: BaseModel):
        """
        Generic implementation to fetch a single given entity with a matching id
        :param entity: SQLAlchemy entity with a valid id
        :return matching SQLAlchemy entity from the database
        """
        assert entity.id > 0
        return (db.session.connection
                .query(entity.__class__)
                .filter(entity.__class__.id == entity.id)
                .one())

    @staticmethod
    def begin():
        """
        Manually begin a db transaction
        """
        db.session.begin()

    @staticmethod
    def rollback():
        """
        Manually rolls back a db transaction
        """
        db.session.rollback()

    @staticmethod
    def commit():
        """
        Manually commits a db transaction
        """
        db.session.commit()

    @staticmethod
    def flush():
        """
        Manually flushes the pending db transactions
        """
        db.session.flush()
