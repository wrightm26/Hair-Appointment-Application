from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField, FileField, TextAreaField, TextAreaField
from wtforms.validators import InputRequired, EqualTo

class SignUpForm(FlaskForm):
    first_name = StringField('First Name:', validators=[InputRequired()])
    last_name = StringField('Last Name:', validators=[InputRequired()])
    username = StringField('Username:', validators=[InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password:', validators=[InputRequired(), EqualTo('password')])
    number = IntegerField('Cell Number:', validators=[InputRequired()])
    email = EmailField('Email:', validators=[InputRequired()])
    submit = SubmitField('Submit')

class LogInForm(FlaskForm):
    username = StringField('Username:', validators=[InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired()])
    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):
    review = TextAreaField('Review:', validators=[InputRequired()])
    submit = SubmitField('Submit')

class GuestForm(FlaskForm):
    first_name = StringField('First Name:', validators=[InputRequired()])
    last_name = StringField('Last Name:', validators=[InputRequired()])
    number = IntegerField('Cell Number:', validators=[InputRequired()])
    email = EmailField('Email:', validators=[InputRequired()])
