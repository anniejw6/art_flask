from flask import render_template, Flask, request, flash, session
from app import app, forms, models, db
from random import randint
import json

def randImg():

	base = 'http://media.vam.ac.uk/media/thira/collection_images/{0}/{1}_jpg_ds.jpg'
	image_id = ['2007BL4483', '2006BF0305', '2006AF0219', '2011FC6706', '2013GK1429', '2006AV6276', '2006BH6911']
	n = randint(0, (len(image_id) - 1))
	img = image_id[n]
	return {'url' : base.format(img[0:6], img), 'num': n}


@app.route('/')
@app.route('/index')
def index():

	session['r_img_num'] = randImg()
	user = {'nickname':'TayTay'} 

	return render_template('index.html', 
		image_url = session['r_img_num']['url'], 
		title = 'ArtFlask', user = user)

@app.route('/contact/', methods = ['GET', 'POST'])
def contact():
	return str(len(models.Response.query.all()))
# 	form = forms.ContactForm()
	
# 	if request.method == "POST":
# 		response_form  = request.form['response_form']
# 		response_content = request.form['response_content']
# 		user_id = 1
# 		art_id = session['r_img_num']['num']
# 		response = models.Response(user_id, art_id, response_form, 
# 			response_content)
# 		db.session.add(response)
# 		db.session.commit()
# 		#return models.Art.query.all()
# 		return str(len(models.Response.query.all()))
	 
# 	elif request.method == "GET":
# 		return render_template('contact.html', form = form)

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

	response_form =  int(float(request.form['response_form']) * 100)
	response_content = int(float(request.form['response_content']) * 100)
	user_id = 1
	art_id = session['r_img_num']['num']
	response = models.Response(user_id, art_id, response_form, response_content)
	db.session.add(response)
	db.session.commit()
	return str(len(models.Response.query.all()))
	# return request