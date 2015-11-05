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
		champ1 = Champion.query.get(266)
		champ2 = Champion.query.get(412)
		self.assertEqual(champ1.name, 'Aatrox') 
		self.assertEqual(champ1.title, 'the Darkin Blade') 
		self.assertEqual(champ2.name, 'Thresh') 
		self.assertEqual(champ2.partype, 'Mana') 

	def test_model_champions_3(self):
		apiResponse = urlopen('http://hardcarry.me/api/champions/266')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertEqual(jsonResponse['266']['name'], 'Aatrox') 
		self.assertEqual(jsonResponse['266']['title'], 'the Darkin Blade') 

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
		ability1 = Champion.query.get(0)
		ability2 = Champion.query.get(1)
		self.assertEqual(ability1.name, 'Dark Flight') 
		self.assertEqual(ability1.maxrank, 5) 
		self.assertEqual(ability2.name, 'Blades of Torment') 
		self.assertEqual(ability2.costType, 'pofcurrentHealth') 

	def test_model_abilities_3(self):
		apiResponse = urlopen('http://hardcarry.me/api/abilities/0')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertEqual(jsonResponse['0']['name'], 'Dark Flight') 
		self.assertEqual(jsonResponse['0']['maxrank'], 5) 

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
		game1 = Champion.query.get(0)
		game2 = Champion.query.get(1)
		self.assertEqual(game1.gameLength, 321) 
		self.assertEqual(game1.gameMode, 'CLASSIC') 
		self.assertEqual(game2.gameType, 'MATCHED_GAME') 
		self.assertEqual(game2.mapId, 11) 

	def test_model_featuredgames_3(self):
		apiResponse = urlopen('http://hardcarry.me/api/featured-games/0')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertEqual(mockResponse['0']['gameLength'], 321) 
		self.assertEqual(mockResponse['0']['gameMode'], 'CLASSIC') 

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
		summoner1 = Champion.query.get(0)
		summoner2 = Champion.query.get(1)
		self.assertEqual(summoner1.name, 'Riesig') 
		self.assertEqual(summoner1.profileIconId, 538) 
		self.assertEqual(summoner2.summonerLevel, 30) 
		self.assertEqual(summoner2.teamId, 100) 

	def test_model_summoners_3(self):
		apiResponse = urlopen('http://api.hardcarry.me/summoners/0')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertEqual(mockResponse['0']['name'], 'Riesig') 
		self.assertEqual(mockResponse['0']['profileIconId'], 538) 

# ----
# Main
# ----

if __name__ == '__main__' :
	main()


# .Unable to connect to the database.
# EE.Unable to connect to the database.
# EE.Unable to connect to the database.
# EE
# ======================================================================
# ERROR: test_model_abilities_2 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File 'tests.py', line 78, in test_model_abilities_2
#     cur = conn.cursor()
# UnboundLocalError: local variable 'conn' referenced before assignment

# ======================================================================
# ERROR: test_model_abilities_3 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File 'tests.py', line 93, in test_model_abilities_3
#     jsonResponse = json.loads(apiResponseRaw)
#   File '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/__init__.py', line 318, in loads
#     return _default_decoder.decode(s)
#   File '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/decoder.py', line 343, in decode
#     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
#   File '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/decoder.py', line 361, in raw_decode
#     raise ValueError(errmsg('Expecting value', s, err.value)) from None
# ValueError: Expecting value: line 1 column 1 (char 0)

# ======================================================================
# ERROR: test_model_champions_2 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File 'tests.py', line 42, in test_model_champions_2
#     cur = conn.cursor()
# UnboundLocalError: local variable 'conn' referenced before assignment

# ======================================================================
# ERROR: test_model_champions_3 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File 'tests.py', line 57, in test_model_champions_3
#     jsonResponse = json.loads(apiResponseRaw)
#   File '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/__init__.py', line 318, in loads
#     return _default_decoder.decode(s)
#   File '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/decoder.py', line 343, in decode
#     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
#   File '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/decoder.py', line 361, in raw_decode
#     raise ValueError(errmsg('Expecting value', s, err.value)) from None
# ValueError: Expecting value: line 1 column 1 (char 0)

# ======================================================================
# ERROR: test_model_items_2 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File 'tests.py', line 114, in test_model_items_2
#     cur = conn.cursor()
# UnboundLocalError: local variable 'conn' referenced before assignment

# ======================================================================
# ERROR: test_model_items_3 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File 'tests.py', line 129, in test_model_items_3
#     jsonResponse = json.loads(apiResponseRaw)
#   File '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/__init__.py', line 318, in loads
#     return _default_decoder.decode(s)
#   File '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/decoder.py', line 343, in decode
#     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
#   File '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/decoder.py', line 361, in raw_decode
#     raise ValueError(errmsg('Expecting value', s, err.value)) from None
# ValueError: Expecting value: line 1 column 1 (char 0)

# ----------------------------------------------------------------------
# Ran 9 tests in 0.371s

# FAILED (errors=6)

