"""add blank user

Revision ID: dd8de187ff0a
Revises: 1ad8e502798b
Create Date: 2024-06-30 02:50:35.926957

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import MetaData, Table

# revision identifiers, used by Alembic.
revision: str = 'dd8de187ff0a'
down_revision: Union[str, None] = '1ad8e502798b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # get metadata from current connection
    meta = MetaData()

    # pass in tuple with tables we want to reflect, otherwise whole database will get reflected
    meta.reflect(only=('user',), bind=op.get_bind())

    # define table representation
    some_table_tbl = Table('user', meta)

    # insert records
    op.bulk_insert(
        some_table_tbl,
        [
            {
                "username": "alice_from_alice_and_bob",
                "display_name": "Alice P",
                "bio": "Hi there, stranger!"
            }
        ]
    )


def downgrade() -> None:
    pass
