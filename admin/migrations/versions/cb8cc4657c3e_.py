"""empty message

Revision ID: cb8cc4657c3e
Revises: 014c814fd91f
Create Date: 2020-05-15 01:34:16.500772

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cb8cc4657c3e'
down_revision = '014c814fd91f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('public_id', table_name='user')
    op.drop_column('user', 'public_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('public_id', mysql.VARCHAR(collation='utf8_unicode_ci', length=500), nullable=True))
    op.create_index('public_id', 'user', ['public_id'], unique=True)
    # ### end Alembic commands ###