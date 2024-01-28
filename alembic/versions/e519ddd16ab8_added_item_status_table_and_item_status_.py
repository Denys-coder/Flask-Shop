"""added item_status table and item.status column

Revision ID: e519ddd16ab8
Revises: 5e2dd9f67062
Create Date: 2024-01-25 01:28:43.211464

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e519ddd16ab8'
down_revision: Union[str, None] = '5e2dd9f67062'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('item', sa.Column('status', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'item', 'item_status', ['status'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'item', type_='foreignkey')
    op.drop_column('item', 'status')
    op.drop_table('item_status')
    # ### end Alembic commands ###
