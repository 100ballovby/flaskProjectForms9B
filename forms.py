from flask_wtf import FlaskForm, RecaptchaField
# flask web text forms
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, DateField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, URL


class ContactForm(FlaskForm):
    """Contact Form"""
    name = StringField('Имя', [DataRequired()])
    email = StringField('Email', [DataRequired()])
    body = TextAreaField('Текст', [DataRequired(),
                                   Length(min=5, message='Your message is too short')])
    submit = SubmitField('Отправить')


class RegisterForm(FlaskForm):
    """Sign up form class"""
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Пароль', [DataRequired(message='Введите пароль!')])
    password_again = PasswordField('Пароль (подтверждение)',
                                   [EqualTo(password, message='Пароль не совпадает!')])

    title = SelectField('Профессия',
                        [DataRequired()],
                        choices=[
                            ('Политик', 'politics'),
                            ('Фермер', 'farmer'),
                            ('Тренер покемонов', 'pokemon'),
                            ('Просто чел', 'man')])
    website = StringField('Сайт', [URL()])
    birthday = DateField('Ваша дата рождения: ')
    recaptcha = RecaptchaField()
    submit = SubmitField('Зарегистрироваться')