from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.fields.core import DateTimeField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError
from application.models import Users
from flask_login import current_user


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
                             validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(),
                                     EqualTo('password')
                                     ]
                                     )
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    user_name = StringField('Username',
                            validators=[DataRequired(),
                                        ]
                            )
    password = PasswordField('Password',
                             validators=[DataRequired()])
    stay_logged_in = BooleanField('Stay Logged In')
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
    submit = SubmitField('Create Event')
