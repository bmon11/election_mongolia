from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User, District


class LoginForm(FlaskForm):
    districts = District.query.all()
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class ImageUploadForm(FlaskForm):
    file = FileField()
    district = SelectField('Дүүрэг', choices=[], validators=[DataRequired()])
    branch = StringField('Хэсгийн хороо', validators=[DataRequired()])
    submit = SubmitField('Submit')


class DistrictSelectForm(FlaskForm):
    district = SelectField('Дүүрэг', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')


class BranchSelectForm(FlaskForm):
    branch = SelectField('Хэсгийн хороо', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')


class VoteForm(FlaskForm):
    party = SelectField('Нам', choices=[], validators=[DataRequired()])
    candidate = StringField('Нэр дэвшигч', validators=[DataRequired()])
    vote = StringField('Саналын тоо', default=0)
    submit = SubmitField('Submit')
