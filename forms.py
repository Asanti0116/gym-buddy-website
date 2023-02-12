"""Forms for GymBuddy"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class SignUpForm(FlaskForm):
  """Form for adding users."""
  

  username = StringField('Username', validators=[
      DataRequired(), Length(min=6)], render_kw={"placeholder": "Username"})

  password = PasswordField('Password', validators=[Length(min=6)], render_kw={"placeholder": "Password"})

  password_confirm = PasswordField('Repeat Password', validators=[ DataRequired(), Length(min=6), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})

class LoginForm(FlaskForm):
  """Login form"""

  username = StringField('Username', validators=[DataRequired()], render_kw={
                           "placeholder": "Username"})
  password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6)], render_kw={"placeholder": "Password"})



