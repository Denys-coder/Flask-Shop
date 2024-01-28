"""added autoincrement=true for some columns

Revision ID: e9070a19123a
Revises: 2e20c099f260
Create Date: 2024-02-03 21:36:37.167031

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'e9070a19123a'
down_revision: Union[str, None] = '2e20c099f260'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('feedback', 'id', existing_type=sa.INTEGER(), autoincrement=True)
    op.alter_column('item', 'id', existing_type=sa.INTEGER(), autoincrement=True)
    op.alter_column('item_status', 'id', existng_type=sa.INTEGER(), autoincrement=True)
    op.alter_column('item_category', 'id', existing_type=sa.INTEGER(), autoincrement=True)
    op.alter_column('order', 'id', existing_type=sa.INTEGER(), autoincrement=True)
    op.alter_column('wishlist', 'id', existing_type=sa.INTEGER(), autoincrement=True)
    op.alter_column('compare_list', 'id', existing_type=sa.INTEGER(), autoincrement=True)

    # ### end Alembic commands ###

    def downgrade() -> None:
        op.alter_column('feedback', 'id', existing_type=sa.INTEGER(), autoincrement=False)
        op.alter_column('item', 'id', existing_type=sa.INTEGER(), autoincrement=False)
        op.alter_column('item_status', 'id', existng_type=sa.INTEGER(), autoincrement=False)
        op.alter_column('item_category', 'id', existing_type=sa.INTEGER(), autoincrement=False)
        op.alter_column('order', 'id', existing_type=sa.INTEGER(), autoincrement=False)
        op.alter_column('wishlist', 'id', existing_type=sa.INTEGER(), autoincrement=False)
        op.alter_column('compare_list', 'id', existing_type=sa.INTEGER(), autoincrement=False)
        pass
        # ### end Alembic commands ###
