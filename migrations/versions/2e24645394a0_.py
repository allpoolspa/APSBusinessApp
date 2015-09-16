"""empty message

Revision ID: 2e24645394a0
Revises: a8bd27a39b5
Create Date: 2015-09-10 10:41:13.978779

"""

# revision identifiers, used by Alembic.
revision = '2e24645394a0'
down_revision = 'a8bd27a39b5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('catalog', sa.Column('cost', sa.Float(), nullable=True))
    op.drop_constraint(u'image_tiny_image_key', 'image', type_='unique')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(u'image_tiny_image_key', 'image', ['tiny_image'])
    op.drop_column('catalog', 'cost')
    ### end Alembic commands ###