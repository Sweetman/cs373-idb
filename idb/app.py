from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
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

@app.route('/champions', methods=['GET'])
def champions():
    return render_template('index.html')

@app.route('/abilities', methods=['GET'])
def abilities():
    return render_template('index.html')

@app.route('/items', methods=['GET'])
def items():
    return render_template('index.html')

@app.route('/partials/<path:path>')
def serve_partial():
	return render_template('/partials/{}'.format(path))

if __name__ == '__main__':
    app.run()