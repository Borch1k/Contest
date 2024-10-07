import datetime
import os

import flask_login
from flask import Flask, render_template, request, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import Tester

# Было сделанно 3 компромиса
# TODO: Сделать лимит по времени выполнения
# TODO: Дописать проверку логина по MAC-адресу
# TODO: Обфусцировать доступ к папке с ответами / Отключить возможность считывать файлы из кода студентов
# TODO: Создать фейковую папку с ответами, в которой будут файлы с текстом, передовать код с ссылкой на эту папку
# TODO: Переписать загрузку файлов, чтобы сайт не зависал

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_unique'

ALLOWED_EXTENSIONS = {'py'}

db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER'] = 'temp_solutions/'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme_index = db.Column(db.Text, nullable=False)
    theme_text = db.Column(db.Text, nullable=False)
    task_index = db.Column(db.String(1), nullable=False)
    task_text = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    inputs = db.Column(db.Text, nullable=True)
    outputs = db.Column(db.Text, nullable=True)
    example_inputs = db.Column(db.Text, nullable=True)
    example_outputs = db.Column(db.Text, nullable=True)
    generator = db.Column(db.Text, nullable=True)
    example_inputs_1 = db.Column(db.Text, nullable=True)
    example_outputs_1 = db.Column(db.Text, nullable=True)
    example_inputs_2 = db.Column(db.Text, nullable=True)
    example_outputs_2 = db.Column(db.Text, nullable=True)
    custom_tester = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Task(theme=%s, task=%s)>' % (self.theme_index, self.task_index)


class Solution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    file_name = db.Column(db.Text)
    time_stamp = db.Column(db.DateTime, nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey("task.id"))
    task = db.relationship("Task")
    success = db.Column(db.Integer, nullable=False)  # Может принимать одно из 4 значений: -2 - неправильный файл, -1 - ошибка при выполнении, 0 - неправильный ответ, 1 - правильный ответ
    test_data = db.Column(db.Text)
    true_answer = db.Column(db.Text)
    student_answer = db.Column(db.Text)

    student = db.relationship("Student", back_populates="solutions")

    def __repr__(self):
        return '<Solution(task=%s, file_name=%s, student=%s)>' % (self.task, self.file_name, self.student.name)


class Student(db.Model, flask_login.UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    rating = db.Column(db.Float)
    style = db.Column(db.Text)

    contests_scores = db.relationship("ContestScore", back_populates="student")
    solutions = db.relationship("Solution", order_by=Solution.id, back_populates="student")

    def __repr__(self):
        return '<Student(id=%s, name=%s)>' % (self.id, self.name)


class ContestScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contest_index = db.Column(db.Text)
    score = db.Column(db.Float)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))

    student = db.relationship("Student", back_populates="contests_scores")

    def __repr__(self):
        return '<Score(student=%s, score=%s)>' % (self.student.name, self.score)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@login_manager.user_loader
def load_user(student_id):
    return Student.query.get(student_id)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def main_page():
    return render_template("index.html", titles=db.session.query(Task.theme_index, Task.theme_text).distinct())


@app.route('/contest/<theme>/<task>')
@flask_login.login_required
def contest(theme, task):
    task_info = db.session.query(Task).filter(Task.theme_index == theme, Task.task_index == task).first()
    other_tasks = db.session.query(Task.theme_index, Task.task_index, Task.task_text).filter(
        Task.theme_index == theme)
    task_success = db.session.query(Solution).join(Student).join(Task) \
        .filter(Task.theme_index == theme, Solution.success == 1, Student.id == flask_login.current_user.id) \
        .with_entities(Task.task_index).all()
    packages = db.session.query(Solution).filter(Solution.student_id == flask_login.current_user.id,
                                                 Solution.task == task_info).order_by(desc(Solution.time_stamp))
    examples = []
    if task_info.example_inputs:
        examples.append({'inputs': task_info.example_inputs, 'outputs': task_info.example_outputs})
    if task_info.example_inputs_1:
        examples.append({'inputs': task_info.example_inputs_1, 'outputs': task_info.example_outputs_1})
    if task_info.example_inputs_2:
        examples.append({'inputs': task_info.example_inputs_2, 'outputs': task_info.example_outputs_2})
    return render_template("contest_template.html", content={'task': task_info, 'titles': other_tasks,
                                                             'packages': packages,
                                                             'examples': enumerate(examples), 'len': len(examples),
                                                             'success': task_success})


@app.route('/about/<int:_id>')
def about_page(_id):
    solution = db.session.query(Solution).filter(Solution.id == _id).first()

    if not solution.file_name:
        return render_template('about.html', content={'code': None, 'id': _id, 'task': solution.task,
                                                      'success': solution.success, 'test_data': solution.test_data,
                                                      'ref': solution.true_answer, 'stu': solution.student_answer})

    file_name = solution.file_name
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    f = open(file_path, encoding='utf-8')
    code = f.read()
    return render_template('about.html', content={'code': code, 'id': _id, 'task': solution.task,
                                                  'success': solution.success, 'test_data': solution.test_data,
                                                  'ref': solution.true_answer, 'stu': solution.student_answer})


@app.route('/rating')
def rating():
    students = db.session.query(Student).order_by(desc(Student.rating)).all()
    contests_names = db.session.query(Task.theme_text).distinct(Task.theme_text).all()
    students_rating = []
    content = {'contests': contests_names, 'students': students_rating}
    for student in students:
        _per_contest_rating = db.session.query(ContestScore).filter(ContestScore.student == student).all()
        students_rating.append({'name': student.name, 'sum': student.rating, 'contests': _per_contest_rating})
    return render_template('main_table.html', content=content)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return redirect('/')

    name = request.form['name']
    print(name)
    if not name.strip():
        return redirect('/')

    if not db.session.query(Student).filter(Student.name == name).all():
        new_user = Student(name=name, rating=0, style='light')
        _contests = db.session.query(Task.theme_index).distinct()
        for _contest in _contests:
            new_user.contests_scores.append(ContestScore(contest_index=_contest[0], score=0))
        db.session.add(new_user)
        db.session.commit()

    flask_login.login_user(db.session.query(Student).filter(Student.name == name)[0])
    return redirect('/')


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect('/')


@app.route('/load_file', methods=['POST', 'GET'])
def upload_solution():
    if request.method == 'GET':
        return redirect('/')

    file = request.files['file']
    time_stamp = datetime.datetime.now(datetime.timezone.utc)
    task = db.session.query(Task).filter(Task.theme_index == request.form['theme_index'],
                                         Task.task_index == request.form['task_index']).first()
    user = flask_login.current_user

    if not allowed_file(file.filename):
        user.solutions.append(Solution(file_name=None, time_stamp=time_stamp, task=task, success=-2,
                                       test_data=None, true_answer=None, student_answer=None))
        db.session.commit()
        return redirect('/contest/%s/%s' % (task.theme_index, task.task_index))

    hex_code = hex(int(time_stamp.timestamp() * 1000000))
    file_name = hex_code + '.py'
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    file.save(file_path)
    file.close()

    success = Tester.Tester(file_path, 'true_solutions/%s/%s.py' % (task.theme_index, task.task_index),
                            task.generator, task.custom_tester)
    if success[0] == -2:
        user.solutions.append(Solution(file_name=None, time_stamp=time_stamp, task=task, success=-2,
                                       test_data=None, true_answer=None, student_answer=None))
        db.session.commit()
        return redirect('/contest/%s/%s' % (task.theme_index, task.task_index))

    if success[0] == 1:
        is_already_done = db.session.query(Solution).filter(Solution.student_id == user.id,
                                                            Solution.task_id == task.id,
                                                            Solution.success == 1).all()
        if not is_already_done:
            task_count = db.session.query(Task).filter(Task.theme_index == task.theme_index).count()
            user.rating += 10 / task_count
            db.session.query(ContestScore).filter(ContestScore.student_id == user.id,
                                                  ContestScore.contest_index == task.theme_index) \
                .first().score += 10 / task_count

    user.solutions.append(Solution(file_name=file_name, time_stamp=time_stamp, task=task, success=success[0],
                                   test_data=success[1], true_answer=success[2], student_answer=success[3]))

    db.session.commit()
    return redirect('/contest/%s/%s' % (task.theme_index, task.task_index))


@app.route('/download/<int:_id>')
def download_file(_id):
    name = db.session.query(Solution).filter(Solution.id == _id).first().file_name
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)


@app.route('/change_theme', methods=['POST', 'GET'])
@flask_login.login_required
def change():
    change_theme = {'light': 'dark', 'dark': 'ortem', 'ortem': 'light'}
    flask_login.current_user.style = change_theme[flask_login.current_user.style]
    db.session.commit()
    if request.method == 'GET':
        return redirect('/')
    print(request)
    return redirect(request.form['last'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
