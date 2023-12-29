from datetime import date
from modules_5 import db, Users
from werkzeug.security import generate_password_hash


def add_user_in_database(email: str, username: str, user_date_birth: date, password: str) -> None:

    new_user = Users(email=email,
                     username=username,
                     date_birth=user_date_birth,
                     password_hash=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    print('add new user')