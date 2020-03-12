from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,BooleanField,SubmitField
from wtforms.validators import DataRequired, Email , EqualTo

class Contact(FlaskForm):
    name = StringField('Name:',validators=[DataRequired()])
    email = StringField('Email:',validators=[DataRequired(),Email()])
    message = TextAreaField('Message:',validators=[DataRequired()])
    submit= SubmitField('Send')
