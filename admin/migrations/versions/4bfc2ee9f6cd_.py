"""empty message

Revision ID: 4bfc2ee9f6cd
Revises: a9c2c57e9040
Create Date: 2020-05-16 02:42:42.786098

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4bfc2ee9f6cd'
down_revision = 'a9c2c57e9040'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'body')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('body', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True))
    # ### end Alembic commands ###