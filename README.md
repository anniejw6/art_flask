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

# Templates


# Misc.

```
pip install --upgrade setuptools
brew install postgresql

```
