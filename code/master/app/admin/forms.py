#create forms
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, PasswordField, BooleanField,SubmitField, TextAreaField, validators, TextField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.fields.html5 import EmailField

class AddUserForm(FlaskForm):
    username = TextField('Username'     , validators=[DataRequired()])
    email    = TextField('Email'        , validators=[DataRequired(), Email()])
    password = PasswordField('Password' , validators=[DataRequired()])
    role = TextField('Role'           , validators=[DataRequired()])
    submit = SubmitField('Add User')

class UpdateUserForm(FlaskForm):
    username = TextField('Username'     , validators=[DataRequired()])
    email    = TextField('Email'        , validators=[DataRequired(), Email()])
    password = PasswordField('Password' , validators=[DataRequired()])
    role = TextField('Role'           , validators=[DataRequired()])
    submit = SubmitField('Add User')