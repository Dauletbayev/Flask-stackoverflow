from flask import Blueprint, render_template
from forms import RegisterForm, LoginForm
# создаем объект компонента
user_bp = Blueprint('user', __name__, url_prefix="/user")

@user_bp.route("/")
def user():
    registration_link = "<a href='/user/registration'> Регистрация </a><br>"
    login_link = "<a href='/user/login'> Вход в аккаунт </a><br>"
    return registration_link + login_link
@user_bp.route("/registration")
def registration():
    form = RegisterForm()
    return render_template("register.html", form=form)
@user_bp.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)
