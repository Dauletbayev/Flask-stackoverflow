from flask import Blueprint, render_template, request
from forms import QuestionForm
# Это просто заглушка для ваших данных вопросов, замените её на свою логику получения вопросов
questions = []

# создаем объект компонента
question_bp = Blueprint('question', __name__, url_prefix="/question")


@question_bp.route("/", methods=['POST', 'GET'])
def question():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Получаем вопрос и текст от пользователя из формы
        title = form.title.data
        main_text = form.main_text.data

        # Добавляем вопрос и текст от пользователя в список вопросов
        questions.append({'title': title, 'main_text': main_text})

        all_question_link = "<a href='/question/all'> Все вопросы </a><br>"

        return render_template("add_question.html", form=form, success=True) + 'Question successfully sent' + all_question_link
    return render_template("add_question.html", form=form)


@question_bp.route("/all", methods=['GET'])
def all_questions():
    return render_template("all_questions.html", questions=questions)

