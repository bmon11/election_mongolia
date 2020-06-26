"""empty message

Revision ID: 390863cf11da
Revises: cb8cc4657c3e
Create Date: 2020-05-16 02:34:58.310598

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '390863cf11da'
down_revision = 'cb8cc4657c3e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_post_timestamp', table_name='post')
    op.drop_column('post', 'body')
    op.drop_column('post', 'timestamp')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('timestamp', mysql.DATETIME(), nullable=True))
    op.add_column('post', sa.Column('body', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True))
    op.create_index('ix_post_timestamp', 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###