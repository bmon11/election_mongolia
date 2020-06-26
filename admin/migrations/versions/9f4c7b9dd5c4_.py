"""empty message

Revision ID: 9f4c7b9dd5c4
Revises: b492deb3557e
Create Date: 2020-06-27 00:51:19.549752

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9f4c7b9dd5c4'
down_revision = 'b492deb3557e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('district')
    op.drop_table('device')
    op.drop_table('image')
    op.drop_table('party')
    op.drop_table('candidate')
    op.drop_table('branch')
    op.drop_table('vote')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vote',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('vote_number', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('is_approved', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('branch',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=140), nullable=True),
    sa.Column('address', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('candidate',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('first_name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.Column('last_name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.Column('gender', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('party',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.Column('code', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('image',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=80), nullable=True),
    sa.Column('path', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.Column('is_approved', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('branch_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('device_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['branch_id'], ['branch.id'], name='image_ibfk_1'),
    sa.ForeignKeyConstraint(['device_id'], ['device.id'], name='image_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('device',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('device_type', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=40), nullable=True),
    sa.Column('device_number', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=40), nullable=True),
    sa.Column('software_version', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=40), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('district',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=True),
    sa.Column('code', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=10), nullable=True),
    sa.Column('name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=40), nullable=True),
    sa.Column('quote', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###