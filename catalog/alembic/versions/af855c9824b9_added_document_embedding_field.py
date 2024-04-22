"""Added document embedding field

Revision ID: af855c9824b9
Revises: e8152de43c47
Create Date: 2024-04-22 22:26:33.158436

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector

# revision identifiers, used by Alembic.
revision: str = 'af855c9824b9'
down_revision: Union[str, None] = 'e8152de43c47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('documents', sa.Column('embedding', Vector(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('documents', 'embedding')
    # ### end Alembic commands ###