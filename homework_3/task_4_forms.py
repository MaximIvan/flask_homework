from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm


class UserRegistration(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])