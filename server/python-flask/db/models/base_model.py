from app.create_app import db


class BaseModel(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column("created_at", db.DateTime(timezone=True), server_default=db.func.now())
    updated_at = db.Column("updated_at", db.DateTime(timezone=True), onupdate=db.func.now())
