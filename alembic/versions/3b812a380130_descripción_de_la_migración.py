"""Descripción de la migración

Revision ID: 3b812a380130
Revises: 387dad8e29e6
Create Date: 2023-10-26 17:46:37.011933

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b812a380130'
down_revision: Union[str, None] = '387dad8e29e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('requireManagement', sa.Boolean(), nullable=True))
    op.drop_column('events', 'requireManagement')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('requireManagement', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('events', 'requireManagement')
    # ### end Alembic commands ###
