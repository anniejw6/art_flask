from flask import render_template, Flask, request, flash
from app import app, forms
from random import randint


def randImg():
	n = randint(1,3)
	return "image" + str(n) + ".jpg"



@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'TayTay'} 
	return render_template('index.html',
	image = randImg(), title = 'ArtFlask', user = user)

@app.route('/contact/')
def contact():
	form = forms.ContactForm()
	return render_template('contact.html', form = form)
