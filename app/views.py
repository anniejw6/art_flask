from flask import render_template
from app import app
from random import randint

def randImg():
	n = randint(1,3)
	return "image" + str(n) + ".jpg"
@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'Bobert'} 
	return render_template('index.html',
	image = randImg(), title = 'ArtFlask', user = user)
