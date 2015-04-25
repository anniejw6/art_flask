from flask import render_template, Flask, request, flash
from app import app, forms, models, db
from random import randint


def randImg():
	n = randint(1,3)
	return "image" + str(n) + ".jpg"


#art = randImg()

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'TayTay'} 
	return render_template('index.html',
	image = randImg(), title = 'ArtFlask', user = user)

@app.route('/contact/', methods = ['GET', 'POST'])
def contact():
	form = forms.ContactForm()
	
	if request.method == "POST":
		response_form  = request.form['subject']
		response_content = request.form['message']
		user_id = 1
		art_id = 2
		response = models.Response(user_id, art_id, response_form, response_content)
		db.session.add(response)
		db.session.commit()
		return 'Hooray'
			
	 
	elif request.method == "GET":
		return render_template('contact.html', form = form)
