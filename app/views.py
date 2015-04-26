from flask import render_template, Flask, request, flash, session
from app import app, forms, models, db
from random import randint


def randImg():
	n = randint(1,3)
	return {'name': "image" + str(n) + ".jpg", 'num': n}



# 

@app.route('/')
@app.route('/index')
def index():
	session['r_img_num'] = randImg()
	user = {'nickname':'TayTay'} 

	# # Some fucked up shit we should get rid of later ###
	# art1 = models.Art(1, 'image1.jpg')
	# art2 = models.Art(2, 'image2.jpg')
	# art3 = models.Art(3, 'image3.jpg')
	# db.session.add(art1) 
	# db.session.add(art2)
	# db.session.add(art3)
	# db.session.commit()
	
	form = forms.ContactForm()

	return render_template('index.html',
		image = session['r_img_num']['name'], title = 'ArtFlask', user = user,
		form = form)

@app.route('/contact/', methods = ['GET', 'POST'])
def contact():
	form = forms.ContactForm()
	
	if request.method == "POST":
		response_form  = request.form['response_form']
		response_content = request.form['response_content']
		user_id = 1
		art_id = session['r_img_num']['num']
		response = models.Response(user_id, art_id, response_form, response_content)
		db.session.add(response)
		db.session.commit()
		#return models.Art.query.all()
		return str(len(models.Response.query.all()))
	 
	elif request.method == "GET":
		return render_template('contact.html', form = form)

@app.route('/chart/')
def chart():
	return render_template('chart.html')
