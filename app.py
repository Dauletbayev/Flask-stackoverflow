from flask import Flask
from users import user_bp
from questions import question_bp


app = Flask(__name__)
app.config["CSRF_ENABLED"] = True
app.config["SECRET_KEY"] = "sof-project-49-flask-13123123123213123123"
# регистрация наших блюпринтов(компонентов проекта)
app.register_blueprint(user_bp)
app.register_blueprint(question_bp)

@app.route("/")
def home():
    user_link = "<a href='/user/'> Юзеры </a><br>"
    question_link = "<a href='/question/'> Вопросы </a><br>"
    all_question_link = "<a href='/question/all'> Все вопросы </a><br>"
    return user_link + question_link + all_question_link
# запуск
app.run(debug=True)
