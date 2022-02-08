from sqlalchemy.orm import declarative_base

from db.models.base_model import BaseModel

Base = declarative_base(cls=BaseModel)
