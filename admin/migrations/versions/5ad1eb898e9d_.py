"""empty message

Revision ID: 5ad1eb898e9d
Revises: 716f2d5710af
Create Date: 2020-06-27 00:29:15.215985

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5ad1eb898e9d'
down_revision = '716f2d5710af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('branch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=50), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=50), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('address', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('candidate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=50), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=50), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(length=50), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('gender', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('coalition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=50), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=50), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('device',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=50), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=50), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(length=50), nullable=True),
    sa.Column('device_type', sa.String(length=40), nullable=True),
    sa.Column('device_number', sa.String(length=40), nullable=True),
    sa.Column('software_version', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('district',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=50), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=50), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(length=50), nullable=True),
    sa.Column('code', sa.String(length=10), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('quote', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('party',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=50), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=50), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('code', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=50), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=50), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_by', sa.String(length=50), nullable=True),
    sa.Column('vote_number', sa.Integer(), nullable=True),
    sa.Column('is_approved', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('answer')
    op.drop_table('survey_image')
    op.drop_table('quiz_image')
    op.drop_table('survey')
    op.drop_table('post')
    op.drop_table('survey_answer')
    op.drop_table('sub_category')
    op.drop_table('category')
    op.drop_table('survey_choice')
    op.drop_table('subscriber')
    op.drop_table('podcast')
    op.drop_table('dictionary')
    op.drop_table('election')
    op.drop_table('question')
    op.drop_table('quiz')
    op.drop_table('result')
    op.add_column('image', sa.Column('branch_id', sa.Integer(), nullable=True))
    op.add_column('image', sa.Column('device_id', sa.Integer(), nullable=True))
    op.add_column('image', sa.Column('is_approved', sa.Boolean(), nullable=True))
    op.drop_constraint('image_ibfk_1', 'image', type_='foreignkey')
    op.create_foreign_key(None, 'image', 'device', ['device_id'], ['id'])
    op.create_foreign_key(None, 'image', 'branch', ['branch_id'], ['id'])
    op.drop_column('image', 'post_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('post_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'image', type_='foreignkey')
    op.drop_constraint(None, 'image', type_='foreignkey')
    op.create_foreign_key('image_ibfk_1', 'image', 'post', ['post_id'], ['id'])
    op.drop_column('image', 'is_approved')
    op.drop_column('image', 'device_id')
    op.drop_column('image', 'branch_id')
    op.create_table('result',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('result', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('threshold', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('quiz_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['quiz_id'], ['quiz.id'], name='result_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('quiz',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('body', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('title', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('date_from', mysql.DATETIME(), nullable=True),
    sa.Column('date_to', mysql.DATETIME(), nullable=True),
    sa.Column('status', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('question',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('question', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('quiz_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['quiz_id'], ['quiz.id'], name='question_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('election',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('name', mysql.VARCHAR(collation='utf8_unicode_ci', length=100), nullable=True),
    sa.Column('first', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('second', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('third', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('party', mysql.VARCHAR(collation='utf8_unicode_ci', length=100), nullable=True),
    sa.Column('toirog', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('total', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('dictionary',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('desc', mysql.VARCHAR(collation='utf8_unicode_ci', length=5000), nullable=True),
    sa.Column('word_en', mysql.VARCHAR(collation='utf8_unicode_ci', length=600), nullable=True),
    sa.Column('word_mn', mysql.VARCHAR(collation='utf8_unicode_ci', length=6000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('podcast',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('body', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('name', mysql.VARCHAR(collation='utf8_unicode_ci', length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('subscriber',
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
    op.create_table('survey_choice',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('choice', mysql.VARCHAR(collation='utf8_unicode_ci', length=600), nullable=True),
    sa.Column('survey_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['survey_id'], ['survey.id'], name='survey_choice_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('category',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('category_type', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('name_en', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('name_mn', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('status', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('sub_category',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('category_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('name_en', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('name_mn', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], name='sub_category_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('survey_answer',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('choice', mysql.VARCHAR(collation='utf8_unicode_ci', length=600), nullable=True),
    sa.Column('survey_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('survey_choice_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['survey_choice_id'], ['survey_choice.id'], name='survey_answer_ibfk_1'),
    sa.ForeignKeyConstraint(['survey_id'], ['survey.id'], name='survey_answer_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('post',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('category', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('title', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('body', mysql.VARCHAR(collation='utf8_unicode_ci', length=21000), nullable=True),
    sa.Column('is_featured', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('is_pinned', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('survey',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('title', mysql.VARCHAR(collation='utf8_unicode_ci', length=600), nullable=True),
    sa.Column('question', mysql.VARCHAR(collation='utf8_unicode_ci', length=6000), nullable=True),
    sa.Column('desc', mysql.VARCHAR(collation='utf8_unicode_ci', length=5000), nullable=True),
    sa.Column('status', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('is_multi_choice', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('date_from', mysql.DATETIME(), nullable=True),
    sa.Column('date_to', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('quiz_image',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('name', mysql.VARCHAR(collation='utf8_unicode_ci', length=80), nullable=True),
    sa.Column('path', mysql.VARCHAR(collation='utf8_unicode_ci', length=100), nullable=True),
    sa.Column('quiz_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('question_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], name='quiz_image_ibfk_1'),
    sa.ForeignKeyConstraint(['quiz_id'], ['quiz.id'], name='quiz_image_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('survey_image',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('name', mysql.VARCHAR(collation='utf8_unicode_ci', length=80), nullable=True),
    sa.Column('path', mysql.VARCHAR(collation='utf8_unicode_ci', length=100), nullable=True),
    sa.Column('survey_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['survey_id'], ['survey.id'], name='survey_image_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('answer',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_by', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('answer', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('answer_letter', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('is_correct', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('question_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('score', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('quiz_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], name='answer_ibfk_1'),
    sa.ForeignKeyConstraint(['quiz_id'], ['quiz.id'], name='answer_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('vote')
    op.drop_table('party')
    op.drop_table('district')
    op.drop_table('device')
    op.drop_table('coalition')
    op.drop_table('candidate')
    op.drop_table('branch')
    # ### end Alembic commands ###