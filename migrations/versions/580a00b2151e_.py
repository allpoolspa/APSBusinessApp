"""empty message

Revision ID: 580a00b2151e
Revises: 2e24645394a0
Create Date: 2015-09-11 15:50:47.873297

"""

# revision identifiers, used by Alembic.
revision = '580a00b2151e'
down_revision = '2e24645394a0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'catalog_listing_asin_fkey', 'catalog', type_='foreignkey')
    op.drop_constraint(u'image_catalog_id_fkey', 'image', type_='foreignkey')
    op.drop_column('catalog', 'id')
    op.drop_column('image', 'catalog_id')
    op.drop_column('catalog', 'listing_asin')
    op.create_primary_key("catalog_pkey", "catalog", ["sku"])
    op.add_column('image', sa.Column('catalog_sku', sa.String(), nullable=True))
    op.create_foreign_key(None, 'image', 'catalog', ['catalog_sku'], ['sku'])
    op.add_column('listing', sa.Column('catalog_sku', sa.String(), nullable=True))
    op.create_foreign_key(None, 'listing', 'catalog', ['catalog_sku'], ['sku'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'listing', type_='foreignkey')
    op.drop_column('listing', 'catalog_sku')
    op.add_column('image', sa.Column('catalog_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'image', type_='foreignkey')
    op.create_foreign_key(u'image_catalog_id_fkey', 'image', 'catalog', ['catalog_id'], ['id'])
    op.drop_column('image', 'catalog_sku')
    op.add_column('catalog', sa.Column('listing_asin', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('catalog', sa.Column('id', sa.INTEGER(), nullable=False))
    op.create_foreign_key(u'catalog_listing_asin_fkey', 'catalog', 'listing', ['listing_asin'], ['asin'])
    ### end Alembic commands ###