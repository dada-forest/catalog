"""Modified USFS National Dataset model, url to unique

Revision ID: 3218a6606fc8
Revises: ddde9881c199
Create Date: 2024-05-16 17:22:11.023486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3218a6606fc8'
down_revision: Union[str, None] = 'ddde9881c199'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'usfs_national_dataset', ['metadata_url'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'usfs_national_dataset', type_='unique')
    # ### end Alembic commands ###