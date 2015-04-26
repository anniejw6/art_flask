from flask import render_template, Flask, request, flash, session
from app import app, forms, models, db
from random import randint
from sqlalchemy import func
import pandas as pd
import json

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

@app.route("/gdata")
@app.route("/gdata/<float:mux>/<float:muy>")
def gdata(ndata=100,mux=.5,muy=0.5):
    """
    Pulls data from database
    """
    # query database
    r =  models.Response
    q = db.session.query(r.art_id, 
    	func.count(r.response_id)).group_by(r.art_id).all()
    # Dump to JSON
    x = pd.DataFrame(q)
    x.columns = ['letter', 'frequency']
    return x.to_json(orient='records')
    #return json.dumps(dict(q))

@app.route('/output/', methods = ['GET', 'POST'])
def output():
	
	return render_template('output.html')


@app.route('/signUpUser', methods=['POST'])
def signUpUser():

	response_form =  int(float(request.form['response_form']) * 100)
	response_content = int(float(request.form['response_content']) * 100)
	user_id = 1
	art_id = session['r_img_num']['num']
	response = models.Response(user_id, response_form, response_content, art_id)
	db.session.add(response)
	db.session.commit()
	return str(len(models.Response.query.all()))