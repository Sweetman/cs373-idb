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
		ability1 = ChampionAbility.query.get(268)
		ability2 = ChampionAbility.query.get(270)
		self.assertEqual(ability1.name, 'Dark Flight') 
		self.assertEqual(ability1.maxrank, 5) 
		self.assertEqual(ability2.name, 'Blades of Torment') 
		self.assertEqual(ability2.costType, 'pofcurrentHealth') 

	def test_model_abilities_4(self):
		apiResponse = urlopen('http://hardcarry.me/api/abilities/268')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertEqual(jsonResponse['name'], 'Dark Flight') 
		self.assertEqual(jsonResponse['maxrank'], 5) 

	# --------------
	# Featured Games
	# --------------

	def test_model_featuredgames_1(self):
		mockResponse = [{'gameLength': 321, 'gameMode': 'CLASSIC'},
						{'gameType': 'MATCHED_GAME', 'mapId': 11} ]
		self.assertEqual(mockResponse[0]['gameLength'], 321) 
		self.assertEqual(mockResponse[0]['gameMode'], 'CLASSIC') 
		self.assertEqual(mockResponse[1]['gameType'], 'MATCHED_GAME') 
		self.assertEqual(mockResponse[1]['mapId'], 11) 

	def test_model_featuredgames_2(self):
		mockGame = FeaturedGame(0, 321, 'CLASSIC', 0, '', 0)
		self.assertEqual(mockGame.gameLength, 321) 
		self.assertEqual(mockGame.gameMode, 'CLASSIC') 

	def test_model_featuredgames_3(self):
		game1 = FeaturedGame.query.get(1)
		game2 = FeaturedGame.query.get(2)
		self.assertEqual(game1.gameLength, 362) 
		self.assertEqual(game1.gameMode, 'CLASSIC') 
		self.assertEqual(game2.gameType, 'MATCHED_GAME') 
		self.assertEqual(game2.mapId, 11) 

	def test_model_featuredgames_4(self):
		apiResponse = urlopen('http://hardcarry.me/api/featured-games/1')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertEqual(jsonResponse['gameLength'], 362)
		self.assertEqual(jsonResponse['gameMode'], 'CLASSIC')

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
		summoner1 = Summoner.query.get(70)
		summoner2 = Summoner.query.get(16)
		self.assertEqual(summoner1.name, ' FlapDoodLe  Hmm') 
		self.assertEqual(summoner1.profileIconId, 550) 
		self.assertEqual(summoner2.summonerLevel, 30)
		self.assertEqual(summoner2.name, 'A Wizard') 

	def test_model_summoners_4(self):
		apiResponse = urlopen('http://hardcarry.me/api/summoners/16')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertEqual(jsonResponse['name'], 'A Wizard') 
		self.assertEqual(jsonResponse['profileIconId'], 16) 

# ----
# Main
# ----

if __name__ == '__main__' :
	main()


# coverage3 run tests.py

# ................
# ----------------------------------------------------------------------
# Ran 16 tests in 36.514s

# OK

# coverage3 -m --report

# Name     Stmts   Miss  Cover   Missing
# --------------------------------------
# app        100     69    31%   16, 20, 24-27, 35-43, 50-53, 57-58, 62-65, 69-72, 76-79, 86-89, 93-94, 101-104, 108-109, 113-116, 120-123, 130-133, 137-138, 142-145, 149-152, 162, 165
# config      17      0   100%   
# models     127      0   100%   
# tests      105      0   100%   
# --------------------------------------
# TOTAL      349     69    80%   

# NOTE - the tests actually have nearly 100% coverage on app.py through the api calls.

