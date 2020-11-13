from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.fields.core import DateTimeField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError
from application.models import Users
from application import bcrypt
from flask_login import current_user
from string import punctuation


class RegistrationForm(FlaskForm):
    user_name = StringField('Username',
                            validators=[
                                DataRequired(),
                                Length(min=3, max=15)
                            ]
                            )

    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()
                                    ]
                        )
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=7, max=15)
                                         ]
                             )

    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(),
                                     EqualTo('password')
                                     ]
                                     )
    submit = SubmitField('Sign Up')

    def validate_user_name(self, user_name):
        user = Users.query.filter_by(user_name=user_name.data).first()
        idk = user_name.data
        if user:
            raise ValidationError('Username Taken')

        for letter in idk:
            if letter in list(set(punctuation)):
                raise ValidationError(
                    "Username can't contain " + str(list(set(punctuation)))[1:-1])

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired()
                                       ]
                           )
    password = PasswordField('Password',
                             validators=[DataRequired()])
    submit = SubmitField('Log In')

    def validate_username(self, username):
        user = Users.query.filter_by(user_name=username.data.lower()).first()
        if not user:
            raise ValidationError("User doesn't exist")


class UpdateAccountForm(FlaskForm):
    user_name = StringField('Username',
                            validators=[
                                DataRequired(),
                                Length(min=3, max=15)
                            ]
                            )

    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()
                                    ])
    submit = SubmitField('Edit Account')


class EventForm(FlaskForm):
    title = StringField('Event Name', validators=[DataRequired()])
    description = StringField('Event Description')
    date = DateTimeField('Date of Event', format='%d/%m/%Y')
    submit = SubmitField('Create Event')


class EditEventForm(FlaskForm):
    title = StringField('Event Name', validators=[DataRequired()])
    description = StringField('Event Description')
    date = DateTimeField('Date of Event', format='%d/%m/%Y')
    submit = SubmitField('Edit Event')


class AddUserForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Add User')

    def validate_user_name(self, user_name):
        user = Users.query.filter_by(user_name=user_name.data.lower()).first()
        if not user:
            raise ValidationError("User doesn't exist")
