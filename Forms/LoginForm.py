from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators


class LoginForm(FlaskForm):
    people_email = StringField("Email: ", [
        validators.Length(3, 20, "Name should be from 3 to 20 symbols"),
        validators.Email("Wrong email format")
    ])
    people_password = PasswordField("Password: ", [
        validators.DataRequired("Please enter your password."),
    ])

    submit = SubmitField("Sing In")