"""empty message

Revision ID: 40daed2899ba
Revises: 580a00b2151e
Create Date: 2015-09-11 16:30:28.903827

"""

# revision identifiers, used by Alembic.
revision = '40daed2899ba'
down_revision = '580a00b2151e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('abbreviation', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('company', 'abbreviation')
    ### end Alembic commands ###
