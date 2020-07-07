from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length


class UserForm(FlaskForm):
    
    email = StringField("Email", validators=[
                        InputRequired(), Length(max=50)])

    password = PasswordField("Password", validators=[InputRequired()])


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[
                           InputRequired()])

    password = PasswordField("Password", validators=[InputRequired()])


class ResetForm(FlaskForm):
    email = StringField("Email", validators=[
                        InputRequired(), Length(max=50)])


class PasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[InputRequired()])

    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired()])


