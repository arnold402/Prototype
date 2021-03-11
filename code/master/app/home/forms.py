#create wtf forms
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, PasswordField, BooleanField,SubmitField, TextAreaField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.fields.html5 import EmailField

class AddsalesForm(FlaskForm):
    cust_fname = StringField('First Name', validators=[DataRequired()])
    cust_lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    cust_phone_no = IntegerField('Customer Phone Number', [DataRequired()])
    product_code = StringField('Product Code', [DataRequired()])
    qnt = IntegerField('Quantity', [DataRequired()])
    warranty_status = StringField('Warranty Status')
    delivery = BooleanField("Delivery")
    submit = SubmitField('Submit')

class UpdatesalesForm(FlaskForm):
    cust_fname = StringField('First Name', validators=[DataRequired()])
    cust_lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    cust_phone_no = IntegerField('Customer Phone Number', [DataRequired()])
    product_code = StringField('Product Code', [DataRequired()])
    qnt = IntegerField('Quantity', [DataRequired()])
    warranty_status = StringField('Warranty Status')
    delivery = BooleanField("Delivery")
    submit = SubmitField('Submit')


class RecommendForm(FlaskForm):
    recommend = BooleanField(label=("Recommend for approval"))
    submit = SubmitField('Submit')

class ApproveForm(FlaskForm):
    approve = BooleanField(label=("Approve the application"))
    submit = SubmitField('Submit')

class MessageForm(FlaskForm):
    message = TextAreaField(label =('Message'), validators=[
        DataRequired(), Length(min=0, max=140)])
    submit = SubmitField('Submit')