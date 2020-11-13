from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.fields.core import DateTimeField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError
from application.models import Users
from application import bcrypt
from flask_login import current_user
from string import punctuation


class CheckIfUserExists:
    def __init__(self, message=None):
        self.users = Users.query.all()
        if not message:
            message = "User doesn't exist"
        self.message = message

    def __call__(self, form, field):
        raise ValidationError(self.message)


class CheckIfUsernameIsTaken:
    def __init__(self, message=None):
        self.users = Users.query.all()
        if not message:
            message = 'Username Taken'
        self.message = message

    def __call__(self, form, field):
        for user in self.users:
            if field.data.lower() == user.user_name.lower():
                raise ValidationError(self.message)


class CheckIfEmailIsTaken:
    def __init__(self, message=None):
        self.users = Users.query.all()
        if not message:
            message = 'Email Taken'
        self.message = message

    def __call__(self, form, field):
        for user in self.users:
            if field.data.lower() == user.email:
                raise ValidationError(self.message)


class CharacterCheckUsername:
    def __init__(self):
        self.characters = list(set(punctuation))
        message = "Username can't contain " + str(self.characters)[1:-1]
        self.message = message

    def __call__(self, form, field):
        for letter in field.data.lower():
            if letter in self.characters:
                raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    user_name = StringField('Username',
                            validators=[
                                DataRequired(),
                                CheckIfUsernameIsTaken(),
                                Length(min=3, max=15),
                                CharacterCheckUsername()
                            ]
                            )

    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email(),
                                    CheckIfEmailIsTaken()
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


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       CheckIfUserExists(),
                                       ]
                           )
    password = PasswordField('Password',
                             validators=[DataRequired()])
    submit = SubmitField('Log In')


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
    user_name = StringField('Username', validators=[DataRequired(),
                                                    CheckIfUserExists()])
    submit = SubmitField('Add User')
