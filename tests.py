#!/usr/bin/env python3

# -------------------------------
# Copyright (C) 2015
# League IDB
# -------------------------------

# -------
# Imports
# -------

from io             import StringIO
from urllib.request import urlopen
from unittest       import main, TestCase
from models 		import *
import json, postgresql

# ----------
# TestModels
# ----------

class TestModels (TestCase):

	# ---------
	# Champions
	# ---------

	def test_model_champions_1(self):
		mockResponse = {'Aatrox': {'name': 'Aatrox', 'title': 'the Darkin Blade'},
						'Thresh': {'name': 'Thresh', 'partype': 'Mana'} }
		self.assertEqual(mockResponse['Aatrox']['name'], 'Aatrox') 
		self.assertEqual(mockResponse['Aatrox']['title'], 'the Darkin Blade') 
		self.assertEqual(mockResponse['Thresh']['name'], 'Thresh') 
		self.assertEqual(mockResponse['Thresh']['partype'], 'Mana') 

	def test_model_champions_2(self):
		mockChampion = Champion('Aatrox', 266, '', '', '', 'the Darkin Blade', 8, 4, 3,\
			4, '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
		self.assertEqual(mockChampion.name, 'Aatrox') 
		self.assertEqual(mockChampion.championId, 266) 
		self.assertEqual(mockChampion.title, 'the Darkin Blade') 

	def test_model_champions_3(self):
		champ1 = Champion.query.get(266)
		champ2 = Champion.query.get(412)
		self.assertEqual(champ1.name, 'Aatrox') 
		self.assertEqual(champ1.title, 'the Darkin Blade') 
		self.assertEqual(champ2.name, 'Thresh') 
		self.assertEqual(champ2.partype, 'Mana') 

	def test_model_champions_4(self):
		apiResponse = urlopen('http://hardcarry.me/api/champions/266')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertEqual(jsonResponse['name'], 'Aatrox') 
		self.assertEqual(jsonResponse['title'], 'the Darkin Blade') 

	# ---------
	# Abilities
	# ---------

	def test_model_abilities_1(self):
		mockResponse = {'0': {'name': 'Dark Flight', 'maxrank': 5},
						'1': {'name': 'Blades of Torment', 'costType': 'pofcurrentHealth'} }
		self.assertEqual(mockResponse['0']['name'], 'Dark Flight') 
		self.assertEqual(mockResponse['0']['maxrank'], 5) 
		self.assertEqual(mockResponse['1']['name'], 'Blades of Torment') 
		self.assertEqual(mockResponse['1']['costType'], 'pofcurrentHealth')

	def test_model_abilities_2(self):
		mockAbility = ChampionAbility('Dark Flight', '', '', '', 5, '', '')
		self.assertEqual(mockAbility.name, 'Dark Flight') 
		self.assertEqual(mockAbility.maxrank, 5) 

	def test_model_abilities_3(self):
		ability1 = ChampionAbility.query.get(1)
		ability2 = ChampionAbility.query.get(2)
		self.assertTrue(ability1.name)
		self.assertTrue(ability1.maxrank)
		self.assertTrue(ability2.name)
		self.assertTrue(ability2.costType)

	def test_model_abilities_4(self):
		apiResponse = urlopen('http://hardcarry.me/api/abilities/1')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertTrue(jsonResponse['name'])
		self.assertTrue(jsonResponse['maxrank']) 

	# --------------
	# Featured Games
	# --------------

	def test_model_featuredgames_1(self):
		mockResponse = [{'gameLength': 321, 'game_mode': 'CLASSIC'},
						{'game_type': 'MATCHED_GAME', 'mapId': 11} ]
		self.assertEqual(mockResponse[0]['gameLength'], 321) 
		self.assertEqual(mockResponse[0]['game_mode'], 'CLASSIC') 
		self.assertEqual(mockResponse[1]['game_type'], 'MATCHED_GAME') 
		self.assertEqual(mockResponse[1]['mapId'], 11) 

	def test_model_featuredgames_2(self):
		mockGame = FeaturedGame(0, 321, 'CLASSIC', 0, '', 0)
		self.assertEqual(mockGame.gameLength, 321) 
		self.assertEqual(mockGame.game_mode, 'CLASSIC') 

	def test_model_featuredgames_3(self):
		game1 = FeaturedGame.query.get(1)
		game2 = FeaturedGame.query.get(2)
		self.assertTrue(game1.gameLength) 
		self.assertTrue(game1.champions) 
		self.assertTrue(game2.summoners)
		self.assertTrue(game2.mapId) 

	def test_model_featuredgames_4(self):
		apiResponse = urlopen('http://hardcarry.me/api/featured-games/1')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertTrue(jsonResponse['gameLength'])
		self.assertTrue(jsonResponse['champions'])

	# ---------
	# Summoners
	# ---------

	def test_model_summoners_1(self):
		mockResponse = {'Riesig': {'name': 'Riesig', 'profileIconId': 538},
						'GochuHunter': {'summonerLevel': 30, 'teamId': 100} }
		self.assertEqual(mockResponse['Riesig']['name'], 'Riesig') 
		self.assertEqual(mockResponse['Riesig']['profileIconId'], 538) 
		self.assertEqual(mockResponse['GochuHunter']['summonerLevel'], 30) 
		self.assertEqual(mockResponse['GochuHunter']['teamId'], 100) 

	def test_model_summoners_2(self):
		mockSummoner = Summoner(0, 'Riesig', 538, 30, False)
		self.assertEqual(mockSummoner.name, 'Riesig') 
		self.assertEqual(mockSummoner.profileIconId, 538) 

	def test_model_summoners_3(self):
		summoner1 = Summoner.query.get(1)
		summoner2 = Summoner.query.get(2)
		self.assertTrue(summoner1.name)
		self.assertTrue(summoner1.profileIconId) 
		self.assertTrue(summoner2.summonerLevel)
		self.assertTrue(summoner2.name)

	def test_model_summoners_4(self):
		apiResponse = urlopen('http://hardcarry.me/api/summoners/1')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertTrue(jsonResponse['name'])
		self.assertTrue(jsonResponse['profileIconId'])

	# ------
	# Search
	# ------

	def test_search_1(self):
		apiResponse = urlopen('http://hardcarry.me/api/search/aatrox')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertTrue(jsonResponse['0'])
		self.assertTrue(jsonResponse['0']['abilities'])
		self.assertTrue(jsonResponse['0']['abilities']['Dark Flight'])

	def test_search_2(self):
		apiResponse = urlopen('http://hardcarry.me/api/search/aatrox%20and%20thresh')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertTrue(not jsonResponse)

	def test_search_3(self):
		apiResponse = urlopen('http://hardcarry.me/api/search/aatrox%20or%20thresh')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertTrue(jsonResponse['0'])
		self.assertTrue(jsonResponse['0']['abilities'])
		self.assertTrue(jsonResponse['0']['abilities']['Savagery'])
		self.assertTrue(jsonResponse['1'])
		self.assertTrue(jsonResponse['1']['abilities'])
		self.assertTrue(jsonResponse['1']['abilities']['The Box'])

# ----
# Main
# ----

if __name__ == '__main__' :
	main()


# coverage3 run tests.py
# ...................
# ----------------------------------------------------------------------
# Ran 19 tests in 0.763s

# OK

# coverage3 report -m --include="models.py"
# Name        Stmts   Miss  Cover   Missing
# -----------------------------------------
# models.py     207     59    71%   10-19, 121-125, 128-132, 135-139, 142-146, 176, 196-199, 202-206, 209-213, 236-239, 242-246, 249-253

# NOTE - the tests actually have nearly 100% coverage on app.py through the api calls. The parts coverage says are missing are the 
#		 serialization done by the api calls.

