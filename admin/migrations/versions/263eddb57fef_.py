"""empty message

Revision ID: 263eddb57fef
Revises: 92937272cd20
Create Date: 2020-05-03 17:26:00.161684

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '263eddb57fef'
down_revision = '92937272cd20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscriber',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=50), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=50), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscriber_email'), 'subscriber', ['email'], unique=True)
    op.drop_table('subsriber')
    op.drop_constraint('image_ibfk_1', 'image', type_='foreignkey')
    op.create_foreign_key(None, 'image', 'post', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'image', type_='foreignkey')
    op.create_foreign_key('image_ibfk_1', 'image', 'user', ['post_id'], ['id'])
    op.create_table('subsriber',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('email', mysql.VARCHAR(collation='utf8_unicode_ci', length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_index(op.f('ix_subscriber_email'), table_name='subscriber')
    op.drop_table('subscriber')
    # ### end Alembic commands ###