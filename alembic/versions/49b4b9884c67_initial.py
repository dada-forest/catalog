"""Initial

Revision ID: 49b4b9884c67
Revises:
Create Date: 2024-05-15 21:08:21.403631

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "49b4b9884c67"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "documents",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("identifier", sa.String(length=125), nullable=True),
        sa.Column("url", sa.String(length=250), nullable=True),
        sa.Column("description", sa.String(length=2500), nullable=True),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone="TRUE"),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone="TRUE"),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("identifier"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("documents")
    # ### end Alembic commands ###
