"""create_table_Product

Revision ID: 0a8e8b2cf7b2
Revises: 
Create Date: 2024-11-14 12:33:44.146462

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '0a8e8b2cf7b2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('products',
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('category', sa.String(length=128), nullable=False),
    sa.Column('sale_date', sa.Date(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('products')
