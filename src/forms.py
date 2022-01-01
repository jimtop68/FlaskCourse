from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo





class SignupForm(FlaskForm):
    username=StringField(label="username")
    email=StringField(label="email")
    password=StringField(label="password")
    password2=StringField(label="Επιβεβαίωση password")
    submit=SubmitField(label="Εγγραφή")