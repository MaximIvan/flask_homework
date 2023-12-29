'''
Создать форму регистрации для пользователя.
Форма должна содержать поля: имя, электронная почта,
пароль (с подтверждением), дата рождения, согласие на
обработку персональных данных.
Валидация должна проверять, что все поля заполнены
корректно (например, дата рождения должна быть в
формате дд.мм.гггг).
При успешной регистрации пользователь должен быть
перенаправлен на страницу подтверждения регистрации.
'''

from flask import Flask, flash, request, render_template, redirect, url_for
from task_5_add_user import add_user_in_database
from task_5_forms import UserRegistration
from sqlalchemy.exc import IntegrityError
from modules_5 import db
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ffd5bb3def8e06bec8eaae7a930ceb863bb882a1245af7c1755336ffbd44a865'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('database has been created')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = UserRegistration()

    if request.method == 'POST' \
            and form.validate() \
            and form.consent_processing_personal_data.data:

        username = form.username.data
        date = form.date.data
        email = form.email.data
        password = form.password.data

        try:
            add_user_in_database(email=email,
                                 username=username,
                                 password=password,
                                 user_date_birth=date)

            flash(f'Пользователь {username} успешно зарегистрирован !')

            return redirect(url_for('successful_registration_user'))

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

    return render_template('user_registration.html',
                           **context,
                           form=form)


@app.route('/successful_registration_user/')
def successful_registration_user():
    context = {
        'title_pag': 'Поздравление с успешной регистрацией'
    }
    return render_template('successful_registration_user.html', **context)


if __name__ == '__main__':
    app.run()
