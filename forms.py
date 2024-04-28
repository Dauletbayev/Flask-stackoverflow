from flask_wtf import FlaskForm
from wtforms import (StringField, EmailField,
                     PasswordField, SubmitField, TextAreaField)
from wtforms.validators import DataRequired

# форма для регистрации
class RegisterForm(FlaskForm):
    name = StringField("Имя",
                       validators=[DataRequired("Заполните имя")])
    email = EmailField("Почта",
                       validators=[DataRequired("Введите почту")])
    password = PasswordField("Пароль",
                             validators=[DataRequired("Введите пароль")])
    password2 = PasswordField("Повторите пароль",
                             validators=[DataRequired("Повторите пароль")])

    button = SubmitField("Зарегистрироваться")
class LoginForm(FlaskForm):
    email = EmailField("Почта",
                       validators=[DataRequired("Введите почту")])
    password = PasswordField("Пароль",
                             validators=[DataRequired("Введите пароль")])
    button = SubmitField("Войти")

class QuestionForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    main_text = TextAreaField('Основной текст', validators=[DataRequired()])
    button = SubmitField('Отправить')
