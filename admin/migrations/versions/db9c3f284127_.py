"""empty message

Revision ID: db9c3f284127
Revises: f375f4ed9d0b
Create Date: 2020-05-16 12:42:47.255498

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'db9c3f284127'
down_revision = 'f375f4ed9d0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('name_en', sa.String(length=140), nullable=True))
    op.add_column('category', sa.Column('name_mn', sa.String(length=140), nullable=True))
    op.add_column('category', sa.Column('status', sa.Integer(), nullable=True))
    op.drop_column('category', 'name')
    op.add_column('sub_category', sa.Column('name_en', sa.String(length=140), nullable=True))
    op.add_column('sub_category', sa.Column('name_mn', sa.String(length=140), nullable=True))
    op.drop_column('sub_category', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sub_category', sa.Column('name', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True))
    op.drop_column('sub_category', 'name_mn')
    op.drop_column('sub_category', 'name_en')
    op.add_column('category', sa.Column('name', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True))
    op.drop_column('category', 'status')
    op.drop_column('category', 'name_mn')
    op.drop_column('category', 'name_en')
    # ### end Alembic commands ###