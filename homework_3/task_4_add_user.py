from modules_4 import db, Users
from werkzeug.security import generate_password_hash, check_password_hash


def add_user_in_database(email: str, username: str, password: str) -> None:

    new_user = Users(email=email,
                     username=username,
                     password_hash=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    print('add new user')