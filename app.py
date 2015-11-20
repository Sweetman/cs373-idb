from flask 				  import Flask, render_template, jsonify
from flask.ext.cors import CORS, cross_origin
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta
import coverage

import os, json, subprocess

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)
CORS(app)

import models
from models import *
from tests import TestModels
from sqlalchemy_searchable import search

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index():
	return render_template('index.html')

@app.route('/partials/<path:path>')
def serve_partial():
	return render_template('/partials/{}'.format(path))

@app.route('/tests/runTests/')
def tests():
    p = subprocess.Popen(["make", "test"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
    out, err = p.communicate()
    return render_template('tests.html', output=err+out)


# ------------
# API requests
# ------------

@app.route('/api/')
@cross_origin()
def api_root():
	data = {
				'urls': {
							'champions_url': '/champions',
                     		'abilities_url': '/abilities',
                	 		'summoners_url': '/summoners',
                	 		'featured-games_url': '/featured-games',
                	 		'search_url': '/search'
                		}
           }
	return jsonify(data)

def get_dict_from_obj(obj):
	fields = {}
	for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
		data = obj.__getattribute__(field)
		try:
			json.dumps(data)
			fields[field] = data
		except TypeError:
			pass
	return fields


# Champions

@app.route('/api/champions/')
@cross_origin()
def api_champions_all():
	jsonData = {}
	for data in Champion.query:
		jsonData[data.name] = data.serialize()
	return jsonify(jsonData)

@app.route('/api/champions/<queried_id>')
def api_champions_id(queried_id):
	data = Champion.query.get(queried_id)
	return jsonify(data.serialize())


# Abilities

@app.route('/api/abilities/')
@cross_origin()
def api_abilities_all():
	jsonData = {}
	for data in ChampionAbility.query:
		jsonData[data.name] = data.serialize()
	return jsonify(jsonData)

@app.route('/api/abilities/<queried_id>')
def api_abilities_id(queried_id):
	data = ChampionAbility.query.get(queried_id)
	return jsonify(data.serialize())


# Summoners

@app.route('/api/summoners/')
@cross_origin()
def api_summoners_all():
	jsonData = {}
	for data in Summoner.query:
		jsonData[data.name] = data.serialize()
	return jsonify(jsonData)

@app.route('/api/summoners/<queried_id>')
@cross_origin()
def api_summoners_id(queried_id):
	data = Summoner.query.get(queried_id)
	return jsonify(data.serialize())


# Featured Games

@app.route('/api/featured-games/')
@cross_origin()
def api_featuredgames_all():
	jsonData = {}
	for data in FeaturedGame.query:
		jsonData[data.id] = data.serialize()
	return jsonify(jsonData)

@app.route('/api/featured-games/<queried_id>')
@cross_origin()
def api_featuredgames_id(queried_id):
	data = FeaturedGame.query.get(queried_id)
	return jsonify(data.serialize())


# Search

@app.route('/api/search/<query_string>')
@cross_origin()
def api_search(query_string):
	champ_query = db.session.query(Champion)
	ability_query = db.session.query(ChampionAbility)
	summoners_query = db.session.query(Summoner)
	game_query = db.session.query(FeaturedGame)
	result = {}
	result['champions'] = search(champ_query, query_string).all()
	result['abilities'] = search(ability_query, query_string).all()
	result['summoners'] = search(summoners_query, query_string).all()
	result['featured-games'] = search(game_query, query_string).all()
	jsonData = {}
	i = 0
	for model, data in result.items():
		jsonData[model] = {}
		for result_item in data:
			jsonData[model][i] = result_item.serialize()
			i+=1
	return jsonify(jsonData)


# -------
# Default
# -------

@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>')
def catch_all(path):
	return render_template('index.html')

if __name__ == '__main__':
	app.run()
