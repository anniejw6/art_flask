from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
 
class ContactForm(Form):
	response_form = TextField("Form")
	response_content = TextField("Content")
	submit = SubmitField("Send")

class Submission(Form):
	submit = SubmitField("Submit")