"""create account table

Revision ID: 1ad8e502798b
Revises: 
Create Date: 2024-06-30 02:27:06.647021

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '1ad8e502798b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

TABLE_NAME = 'user'


def upgrade() -> None:
    op.create_table(
        TABLE_NAME,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('display_name', sa.Unicode(200)),
        sa.Column('bio', sa.Text()),
    )


def downgrade() -> None:
    op.drop_table(TABLE_NAME)
