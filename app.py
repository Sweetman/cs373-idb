from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from subprocess import call
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

# sanity check for app settings
# print(os.environ['APP_SETTINGS'])

from models import *

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/partials/<path:path>')
def serve_partial():
	return render_template('/partials/{}'.format(path))

@app.route('/runTests')
def run_tests():
	call('coverage3 run tests.py \ coverage3 html', shell=True)
	f = open('tests.out')
	result = f.read()
	return ('<pre>' + result + '</pre>')

@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()