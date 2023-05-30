from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired,Email

class UserLoginForm(FlaskForm):
    # email, password, submit_button
    first_name = StringField('first_name', validators = [DataRequired()])
    last_name = StringField('last_name', validators = [DataRequired()])
    username = StringField('username', validators= [DataRequired()])
    date_created = DateField('date_created (YYYY-MM-DD)', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

class CarInfo(FlaskForm):
    model =StringField('model')
    make =StringField('make')
    year = StringField('Year (YYYY)')
    color = StringField('Color')
    image_url = StringField('Image URL')
    submit_button = SubmitField()
