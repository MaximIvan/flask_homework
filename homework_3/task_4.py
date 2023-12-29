'''
Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
содержать следующие поля:
○ Имя пользователя (обязательное поле)
○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
заполнено или данные не прошли валидацию, то должно выводиться соответствующее
сообщение об ошибке.
Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
об ошибке.
'''

from task_4_add_user import add_user_in_database
from flask import Flask, flash, request, render_template
from task_4_forms import UserRegistration
from sqlalchemy.exc import IntegrityError
from modules_4 import db
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SECRET_KEY'] = '12a04fbf05514c10b1860a2b0e143b840e6dae2f5a8b6e2ff766fbed1e4c2a66'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_4.db'
db.init_app(app)
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('database has been created')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = UserRegistration()

    if request.method == 'POST' and form.validate():

        username = form.username.data
        email = form.email.data
        password = form.password.data


        try:
            add_user_in_database(email=email,
                                 username=username,
                                 password=password)
            flash(f'Пользователь {username} успешно зарегистрирован !')
        except IntegrityError as error:


            error_code = error.orig.args[0]

            if 'UNIQUE' in error_code and 'email' in error_code:
                flash(f'Пользователь {username} с такой электронной почтой {email} уже зарегестрирован')

            if 'UNIQUE' in error_code and 'username' in error_code:
                flash(f'Пользователь {username} с таким ником уже зарегестрирован')

        except:
            flash(f'Пользователь {username} НЕ зарегистрирован (произошла ошибка) !')

    context = {
        'title_pag': 'Регистрация пользователя'
    }

    return render_template('registration.html',
                           **context,
                           form=form)


if __name__ == '__main__':
    app.run()