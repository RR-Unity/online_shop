"""create tables products and basket

Revision ID: 9df4c033ca37
Revises: 
Create Date: 2023-02-10 02:39:05.873573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9df4c033ca37'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.BIGINT, sa.Identity(), primary_key=True, nullable=False),

        sa.Column('name', sa.VARCHAR(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
    )

    op.create_table(
        'basket',
        sa.Column('id', sa.BIGINT, sa.Identity(), primary_key=True, nullable=False),

        sa.Column('product_id', sa.BIGINT, nullable=False),
        sa.Column('count', sa.Integer(), nullable=False),
        sa.Column('total_price', sa.Float(), nullable=False),

        sa.ForeignKeyConstraint(('product_id',), ['products.id'], onupdate='RESTRICT', ondelete='RESTRICT'),
    )

    op.create_index('basket_products_product_id', 'basket', ['product_id'], unique=True)


def downgrade() -> None:
    op.drop_table('products')
    op.drop_table('basket')
