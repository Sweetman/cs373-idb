from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from models import *

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
# sanity check for app settings
print(os.environ['APP_SETTINGS'])

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()