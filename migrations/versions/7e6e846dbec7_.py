"""empty message

Revision ID: 7e6e846dbec7
Revises: be6feeb71b7c
Create Date: 2022-09-23 09:11:56.661963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e6e846dbec7'
down_revision = 'be6feeb71b7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=200), nullable=True, comment='user password'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###
