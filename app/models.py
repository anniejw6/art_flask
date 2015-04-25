from app import db

class Art(db.Model):
	art_id = db.Column(db.Integer, primary_key=True)
	art_image_path = db.Column(db.String(300))

	def __init__(self, art_id, art_image_path):
		self.art_id = art_id
		self.art_image_path = art_image_path

	def __repr__(self):
		return '<ID: {0} Path: {1}>'.format(self.art_id, self.art_image_path)

# class User(db.Model):
#     user_id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True)

#     def __init__(self, email):
#         self.email = email

#     def __repr__(self):
#         return '<ID  %r>' % self.user_id

class Response(db.Model):
	response_id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer)
	# art_id = db.Column(db.Integer)
	# user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
	art_id = db.Column(db.Integer, db.ForeignKey('art.art_id'))
	response_form = db.Column(db.Integer)
	response_content = db.Column(db.Integer)

	def __init__(self, user_id, art_id, response_form, response_content):
		self.user_id = user_id
		self.art_id = art_id
		self.response_form = response_form
		self.response_content = response_content

	def __repr__(self):
		return '<ID: %r>' % self.response_id
