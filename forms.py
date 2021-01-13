from flask_wtf import FlaskForm
# flask web text forms
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    """Contact Form"""
    name = StringField('Имя', [DataRequired()])
    email = StringField('Email', [DataRequired()])
    body = TextAreaField('Текст', [DataRequired(),
                                   Length(min=5, message='Your message is too short')])
    submit = SubmitField('Отправить')
