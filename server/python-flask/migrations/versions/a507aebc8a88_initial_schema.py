"""Initial schema

Revision ID: a507aebc8a88
Revises: 
Create Date: 2022-02-06 17:47:54.915927

"""
from alembic import op


# revision identifiers, used by Alembic.
from sqlalchemy import Column, BigInteger, String, DateTime, func

revision = 'a507aebc8a88'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "url",
        Column("id", BigInteger, primary_key=True),
        Column("short_url", String, nullable=False),
        Column("long_url", String, nullable=False),
        Column("hits", BigInteger, nullable=False, default=0),
        Column("created_at", DateTime(timezone=True), server_default=func.now()),
        Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
    )


def downgrade():
    op.drop_table("url")
