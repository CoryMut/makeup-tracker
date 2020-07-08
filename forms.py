from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, Email, ValidationError
from models import User

class UserForm(FlaskForm):
    
    email = StringField("Email", validators=[
                        InputRequired(), Length(max=50), Email()])

    password = PasswordField("Password", validators=[InputRequired()])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email is already associated with an account!")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[
                           InputRequired()])

    password = PasswordField("Password", validators=[InputRequired()])

    def validate_email(self, field):
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError("Email is not associated with an account!")

class ResetForm(FlaskForm):
    email = StringField("Email", validators=[
                        InputRequired(), Length(max=50)])


class PasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[InputRequired()])

    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired()])


