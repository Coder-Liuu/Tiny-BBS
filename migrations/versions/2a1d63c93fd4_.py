"""empty message

Revision ID: 2a1d63c93fd4
Revises: c8398f5da146
Create Date: 2022-09-23 13:18:51.702191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a1d63c93fd4'
down_revision = 'c8398f5da146'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'create_time')
    # ### end Alembic commands ###
