from app import db

class Art(db.Model):
	__tablename__ = 'art'
	id = db.Column(db.Integer, primary_key=True)
	image_path = db.Column(db.String(300), unique=True)
	title = db.Column(db.String(500))

	responses = db.relationship('Response', backref = db.backref('art'))

	def __init__(self, image_path, title):
		self.image_path = image_path
		self.title = title

	def __repr__(self):
		return '<ID: {0} Path: {1}>'.format(self.id, self.image_path)

class Response(db.Model):
	__tablename__ = 'response'
	response_id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer)
	response_form = db.Column(db.Integer)
	response_content = db.Column(db.Integer)

	art_id = db.Column(db.Integer, db.ForeignKey('art.id'))
	# user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

	def __init__(self, user_id, response_form, response_content, art_id):
		self.user_id = user_id
		self.art_id = art_id
		self.response_form = response_form
		self.response_content = response_content

	def __repr__(self):
		return '<ID: %r>' % self.response_id


# class User(db.Model):
#     user_id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True)

#     def __init__(self, email):
#         self.email = email

#     def __repr__(self):
#         return '<ID  %r>' % self.user_id
