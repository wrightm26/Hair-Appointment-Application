from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField, FileField
from wtforms.validators import InputRequired, EqualTo

class SignUpForm(FlaskForm):
    full_name = StringField('Full Name:', validators=[InputRequired()])
    username = StringField('Username:', validators=[InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired()])
    confirm_password = StringField('Confirm Password:', validators=[InputRequired(), EqualTo('password')])
    number = IntegerField('Number:', validators=[InputRequired()])
    email = EmailField('Email:', validators=[InputRequired()])
    submit = SubmitField('Submit')

class LogInForm(FlaskForm):
    username = StringField('Username:', validators=[InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired()])
    submit = SubmitField('Submit')
