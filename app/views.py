from flask import render_template, Flask, request, flash, session
from app import app, forms, models, db
from random import randint
import json

def randImg():
	n = randint(1,3)
	return {'name': "image" + str(n) + ".jpg", 'num': n}



# 

@app.route('/',  methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
	session['r_img_num'] = randImg()
	user = {'nickname':'TayTay'} 

	if request.method == "POST":
		user =  request.form['username']
		password = request.form['password']
		#return json.dumps({'status':'OK','user':user,'pass':password});
		return 'test'

	elif request.method == "GET":

		return render_template('index.html', 
			image = session['r_img_num']['name'], 
			title = 'ArtFlask', user = user)

@app.route('/contact/', methods = ['GET', 'POST'])
def contact():
	form = forms.ContactForm()
	
	if request.method == "POST":
		response_form  = request.form['response_form']
		response_content = request.form['response_content']
		user_id = 1
		art_id = session['r_img_num']['num']
		response = models.Response(user_id, art_id, response_form, 
			response_content)
		db.session.add(response)
		db.session.commit()
		#return models.Art.query.all()
		return str(len(models.Response.query.all()))
	 
	elif request.method == "GET":
		return render_template('contact.html', form = form)

@app.route('/chart2/')
def chart2():
	return render_template('chart2.html')

@app.route('/chart/')
def chart():
	return render_template('chart.html')

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});
	# return request