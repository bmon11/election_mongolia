"""empty message

Revision ID: 92937272cd20
Revises: f0c521e34a71
Create Date: 2020-05-03 17:21:19.189295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92937272cd20'
down_revision = 'f0c521e34a71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('category', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'category')
    # ### end Alembic commands ###