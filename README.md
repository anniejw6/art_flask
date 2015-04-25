# Flask App 

Building a flask application with static images and interactive data I/O.

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
pip install -r requirements.txt
```
# Heroku
Install Heroku toolbelt
```
heroku login
heroku create APP_NAME
git remote add REMOTE_NAME git@heroku.com:APP_NAME.git
git push REMOTE_NAME master
```
If authentication error, https://devcenter.heroku.com/articles/keys
Make sure you're not on a network that blocks certain ports

# Postgres
See here: http://blog.sahildiwan.com/posts/flask-and-postgresql-app-deployed-on-heroku/

Download http://postgresapp.com/
Add to bash_profile http://postgresapp.com/documentation/cli-tools.html
```
createdb appdb
```

# Databases
``` python db_create.py```

# Templates


# Misc.

```
pip install --upgrade setuptools
brew install postgresql
```

psycog2
http://stackoverflow.com/questions/11538249/python-pip-install-psycopg2-install-error
```
sudo cp /Library/PostgreSQL/9.2/lib/libssl.1.0.0.dylib /usr/lib
sudo cp /Library/PostgreSQL/9.2/lib/libcrypto.1.0.0.dylib /usr/lib
sudo ln -fs /usr/lib/libssl.1.0.0.dylib /usr/lib/libssl.dylib
sudo ln -fs /usr/lib/libcrypto.1.0.0.dylib /usr/lib/libcrypto.dylib
```

