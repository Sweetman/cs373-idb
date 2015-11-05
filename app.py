from flask 				  import Flask, render_template, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta
from subprocess 		  import call

import os, json

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import *

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/partials/<path:path>')
def serve_partial():
	return render_template('/partials/{}'.format(path))

@app.route('/tests/runTests/')
def run_tests():
	call('coverage run tests.py > tests.out 2>&1', shell=True)
	f = open('tests.out')
	result = f.read()
	return ('<pre>' + result + '</pre>')

# ------------
# API requests
# ------------

def get_dict_from_obj(obj):
	fields = {}
	for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
		data = obj.__getattribute__(field)
		try:
			json.dumps(data)
			fields[field] = data
		except TypeError:
			fields[field] = None
	return fields

@app.route('/api/champions/')
def api_champions_all():
	jsonData = {}
	for data in Champion.query:
		jsonData[data.name] = get_dict_from_obj(data)
	return jsonify(jsonData)

@app.route('/api/champions/<queried_id>')
def api_champions_id(queried_id):
	data = Champion.query.get(queried_id)
	return jsonify(get_dict_from_obj(data))

@app.route('/api/champions/<queried_id>/abilities')
def api_champions_id_abilities(queried_id):
	data = Champion.query.get(queried_id)
	return jsonify(get_dict_from_obj(data))

@app.route('/api/abilities/')
def api_abilities_all():
	jsonData = {}
	for data in ChampionAbility.query:
		jsonData[data.name] = get_dict_from_obj(data)
	return jsonify(jsonData)

@app.route('/api/abilities/<queried_id>')
def api_abilities_id(queried_id):
	data = ChampionAbility.query.get(queried_id)
	return jsonify(get_dict_from_obj(data))

@app.route('/api/summoners/')
def api_summoners_all():
	jsonData = {}
	for data in Summoner.query:
		jsonData[data.name] = get_dict_from_obj(data)
	return jsonify(jsonData)

@app.route('/api/summoners/<queried_id>')
def api_summoners_id(queried_id):
	data = Summoner.query.get(queried_id)
	return jsonify(get_dict_from_obj(data))

@app.route('/api/featured-games/')
def api_featuredgames_all():
	jsonData = {}
	for data in FeaturedGame.query:
		jsonData[data.id] = get_dict_from_obj(data)
	return jsonify(jsonData)

@app.route('/api/featured-games/<queried_id>')
def api_featuredgames_id(queried_id):
	data = FeaturedGame.query.get(queried_id)
	return jsonify(get_dict_from_obj(data))

# -------
# Default
# -------

@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>')
def catch_all(path):
	return render_template('index.html')

if __name__ == '__main__':
	app.run()
