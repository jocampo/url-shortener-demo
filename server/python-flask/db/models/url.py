from db.models.base_model import BaseModel
from app.create_app import db


class Url(BaseModel):
    short_url = db.Column("short_url", db.String, nullable=False)
    long_url = db.Column("long_url", db.String, nullable=False)
    hits = db.Column("hits", db.BigInteger, nullable=False, default=0)
