from flask import (render_template, Flask, request,
	flash, session, redirect, url_for, g)
from app import app, forms, models, db, lm, bcrypt
from random import randint
from sqlalchemy import func
import pandas as pd
from flask.ext.login import (LoginManager, login_required, login_user,
	logout_user, current_user)
import json
from flask.ext.bcrypt import Bcrypt
import logging
import uuid
import sys

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@lm.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.
    :param unicode user_id: user_id (email) user to retrieve
    """
    #return models.User.query.filter_by(email = user_id).first()
    return models.User.query.get(user_id)

def randImg():

	base = 'http://media.vam.ac.uk/media/thira/collection_images/{0}/{1}_jpg_ds.jpg'

	# Grab list of IDs from database
	image_id = []
	for i in db.session.query(models.Art):
		image_id.append(i)
	image_id = [img.image_path for img in image_id]

	# Grab random one
	n = randint(0, (len(image_id) - 1))
	img = image_id[n]

	return {'url': base.format(img[0:6], img), 'num': n + 1}

# Before  request
@app.before_request
def before_request():
	if 'session_idd' not in session:
		session['session_idd'] = uuid.uuid4().hex

	if current_user.is_authenticated():
		session['user_idd'] = session['user_id']
	else:
		session['user_idd'] = session['session_idd'] 

# Home Page
@app.route('/')
@app.route('/index')
def index():
	session['r_img_num'] = randImg()
	#app.logger.info(session['user_idd'])
	#app.logger.info(session['session_idd'])

	return render_template('index.html',
			image_url = session['r_img_num']['url'])

# About
@app.route('/about/')
def about():
	return render_template('about.html')

# Easy way to query database stupidly
@app.route('/contact/', methods = ['GET', 'POST'])
#@login_required
def contact():
	#return str(len(models.User.query.all()))
	#app.logger.info(models.User.query.get('albatross'))
	
	#return str(current_user)
	return session['user_idd']

# Data for Output
@app.route("/gdata")
def gdata():
	"""
	Pulls data from database
	"""
	# query database
	r = models.Response
	q = db.session.query(r.art_id,
		func.count(r.response_id)).group_by(r.art_id).all()
	# Dump to JSON
	x = pd.DataFrame(q)
	x.columns = ['letter', 'frequency']
	return x.to_json(orient='records')
	# return json.dumps(dict(q))


# Check output
@app.route('/output/', methods = ['GET', 'POST'])
def output():
	#
	return render_template('output.html')


# Put things in database
@app.route('/signUpUser', methods=['POST'])
def signUpUser():
	response = models.Response(
		session_id = session['session_idd'], 
		user_id = session['user_idd'], 
		art_id = session['r_img_num']['num'],
		response_form = int(float(request.form['response_form']) * 100),
		response_content = int(float(request.form['response_content']) * 100))
	db.session.add(response)
	db.session.commit()

	return str(len(models.Response.query.all()))


# Log-In
@app.route("/login/", methods=["GET", "POST"])
def login():
	"""For GET requests, display the login form. For POSTS, login the current user
	by processing the form."""
	form = forms.LoginForm()
	#app.logger.info(session['user_id'])
	if form.validate_on_submit():
		user = models.User.query.filter_by(email = form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			user.authenticated = True
			db.session.add(user)
			db.session.commit()
			login_user(user, remember=True)
			#app.logger.info(current_user)
			#app.logger.info(session['user_id'])
			session['user_idd'] = session['user_id']
			flash("Logged in successfully.")
			return redirect(url_for("index"))
	return render_template("reg_login.html", form=form)


@app.route("/logout/", methods=["GET"])
@login_required
def logout():
	"""Logout the current user."""
	user = current_user
	user.authenticated = False
	db.session.add(user)
	db.session.commit()
	logout_user()
	session['user_idd'] = session['session_idd']
	#return render_template("logout.html")
	return 'logged out'

@app.route('/register/' , methods=['GET','POST'])
def register():
	form = forms.LoginForm()
	if request.method == 'GET':
		return render_template('reg_login.html', form = form)
	user = models.User(request.form['email'], 
		bcrypt.generate_password_hash(request.form['password']))
	db.session.add(user)
	db.session.commit()
	login_user(user, remember=True)
	session['user_idd'] = session['user_id']
	flash('User successfully registered')
	return redirect(url_for('index'))
 
# @app.route('/login/',methods=['GET','POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('reg_login.html')
#     return redirect(url_for('index'))
