"""empty message

Revision ID: bae110e1a783
Revises: 7ff62f83de7d
Create Date: 2020-05-15 00:56:59.257339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bae110e1a783'
down_revision = '7ff62f83de7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('public_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'public_id')
    # ### end Alembic commands ###