# Flask App 

Building a flask application with static images and interactive data I/O.

Production: [art-flask-pro.herokuapp.com](http://art-flask-pro.herokuapp.com/) (In theory, this should always work.)

Staging: [art-flask-stage.herokuapp.com](http://art-flask-stage.herokuapp.com/) (Probably is broken.)

# Setup 
Create new virtual environment
``` 
python -m venv flask
```

Activate virtualenv
```
source flask/bin/activate
```

run `requirements.txt`
```
pip install --upgrade pip
pip install --upgrade setuptools
pip install -r requirements.txt 
#alternatively: `cat requirements.txt | xargs -n 1 pip install`
```
# Heroku
Install Heroku toolbelt
```
heroku login
heroku create APP_NAME
git remote add REMOTE_NAME git@heroku.com:APP_NAME.git
```
First time you push
```
git push REMOTE_NAME master
heroku addons:add heroku-postgresql:dev
heroku pg:promote HEROKU_POSTGRESQL_COLOR
heroku run python
from app import db
db.create_all()
quit()
heroku run python addTables.py
```
Subsequent times
```
git push REMOTE_NAME master
```
(What to do when your database structure changes is still an open question)
If authentication error, https://devcenter.heroku.com/articles/keys
Make sure you're not on a network that blocks certain ports

# Databases
## Migrating
```
# Initialize
python managedb.py db init
# AFTER EVERY DATABASE CHANGE
python managedb.py db migrate
python managedb.py db upgrade
```
See here: http://blog.sahildiwan.com/posts/flask-and-postgresql-app-deployed-on-heroku/

Download http://postgresapp.com/
Add to bash_profile: http://postgresapp.com/documentation/cli-tools.html
```
createdb appdb
python
from app import db
db.create_all()
quit()
```

Working with mapped postgres tables in python
```
from app import models, db
a = models.Art
r = models.Response

for q in db.session.query(a): ## example
  print(q)
  
result = []
for i in db.session.query(a, r):
  result.append(i)
x = res[1]
print(x)
print(x[0])
print(x[1].user_id)
```


# Templates

# Models (database)

Input
```
# /app python
from app import db, models
db.create_all()
user = models.User('jamie@gmail.com')
db.session.add(user)
db.sesssion.commit()
models.User.query.all() #auto generates ID!
```

Connecting via SQLAlchemy
```
from sqlachemy import create_engine
engine  = create_engine('postgresql://localhost/appdb')
connection = engine.connect()
result = connection.execute("select * from response")
for row in result:
  print(row['response_id'])
```

# Misc.

psycopg2
http://stackoverflow.com/questions/11538249/python-pip-install-psycopg2-install-error
```
sudo PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.4/bin pip install psycopg2
```
```
sudo cp /Library/PostgreSQL/9.2/lib/libssl.1.0.0.dylib /usr/lib
sudo cp /Library/PostgreSQL/9.2/lib/libcrypto.1.0.0.dylib /usr/lib
sudo ln -fs /usr/lib/libssl.1.0.0.dylib /usr/lib/libssl.dylib
sudo ln -fs /usr/lib/libcrypto.1.0.0.dylib /usr/lib/libcrypto.dylib
```

**Good links**

- [Long end-to-end post](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database);
- [Short Flask & Heroku](http://blog.sahildiwan.com/posts/flask-and-postgresql-app-deployed-on-heroku/);
- [Medium Flask & Heroku](https://realpython.com/blog/python/flask-by-example-part-1-project-setup/);
- [Short Flask, Heroku & PostgreSQL](http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku)
- [Flask & D3](https://github.com/cranmer/flask-d3-hello-world/blob/master/__init__.py)
