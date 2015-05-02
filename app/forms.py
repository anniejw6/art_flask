from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired
 
class ContactForm(Form):
	response_form = TextField("Form")
	response_content = TextField("Content")
	submit = SubmitField("Send")

class Submission(Form):
	submit = SubmitField("Submit")

class LoginForm(Form):
    """Form class for user login."""
    email = TextField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
   # remember_me = BooleanField('Remember me', default = False)