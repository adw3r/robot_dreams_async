"""generate uuid automatically

Revision ID: 48ca0af67f0d
Revises: f4cf9f9a67dd
Create Date: 2024-07-12 13:15:06.860307

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "48ca0af67f0d"
down_revision: Union[str, None] = "f4cf9f9a67dd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "users",
        "id",
        server_default=sa.text("gen_random_uuid()"),
    )
    op.alter_column(
        "addresses",
        "id",
        server_default=sa.text("gen_random_uuid()"),
    )


def downgrade() -> None:
    op.alter_column(
        "users",
        "id",
        server_default=None,
    )
    op.alter_column(
        "addresses",
        "id",
        server_default=None,
    )
