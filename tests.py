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

import json, psycopg2

# ----------
# TestModels
# ----------

class TestModels (TestCase):

	# ---------
	# Champions
	# ---------

	def test_model_champions_1(self):
		mockResponse = {"Aatrox": {"champ_name": "Aatrox", "title": "the Darkin Blade"},
						"Thresh": {"champ_name": "Thresh", "partype": "Mana"} }
		self.assertEqual(mockResponse['Aatrox']['champ_name'], "Aatrox") 
		self.assertEqual(mockResponse['Aatrox']['title'], "the Darkin Blade") 
		self.assertEqual(mockResponse['Thresh']['champ_name'], "Thresh") 
		self.assertEqual(mockResponse['Thresh']['partype'], "Mana") 

	def test_model_champions_2(self):
		try:
			conn = psycopg2.connect("dbname='hardcarry' user='admin' password='password'")
		except:
			print ("Unable to connect to the database.")
		cur = conn.cursor()
		try:
			cur.execute("""SELECT * FROM champion""")
		except:
			print ("Query failed.")
		dbResponse = cur.fetchall()
		self.assertEqual(dbResponse[0][0], "Aatrox") 
		self.assertEqual(dbResponse[0][9], "the Darkin Blade") 
		self.assertEqual(dbResponse[1][0], "Thresh") 
		self.assertEqual(dbResponse[1][8], "Mana") 

	def test_model_champions_3(self):
		apiResponse = urlopen('http://hardcarry.me/api/champions/Aatrox')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertEqual(jsonResponse['name'], "Aatrox") 
		self.assertEqual(jsonResponse['title'], "the Darkin Blade") 

	# ------
	# Abilities
	# ------

	def test_model_abilities_1(self):
		mockResponse = {"0": {"spell_name": "Dark Flight", "maxrank": 5},
						"1": {"spell_name": "Blades of Torment", "costType": "pofcurrentHealth"} }
		self.assertEqual(mockResponse["0"]['spell_name'], "Dark Flight") 
		self.assertEqual(mockResponse["0"]['maxrank'], 5) 
		self.assertEqual(mockResponse["1"]['spell_name'], "Blades of Torment") 
		self.assertEqual(mockResponse["1"]['costType'], "pofcurrentHealth") 

	def test_model_abilities_2(self):
		try:
			conn = psycopg2.connect("dbname='hardcarry' user='admin' password='password'")
		except:
			print ("Unable to connect to the database.")
		cur = conn.cursor()
		try:
			cur.execute("""SELECT * FROM ability""")
		except:
			print ("Query failed.")
		dbResponse = cur.fetchall()
		self.assertEqual(dbResponse[0][5], "Dark Flight") 
		self.assertEqual(dbResponse[0][4], 5) 
		self.assertEqual(dbResponse[1][5], "Blades of Torment") 
		self.assertEqual(dbResponse[1][1], "pofcurrentHealth") 

	def test_model_abilities_3(self):
		apiResponse = urlopen('http://hardcarry.me/api/abilities/0')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertEqual(jsonResponse["0"]['spell_name'], "Dark Flight") 
		self.assertEqual(jsonResponse["0"]['maxrank'], 5) 

	# -----
	# Items
	# -----

	def test_model_items_1(self):
		mockResponse = {"Enchantment: Cinderhulk": {"group": "JungleItems", "image": "3725.png"},
						"Enchantment: Runeglaive": {"group": "JungleItems", "image": "3724.png"} }
		self.assertEqual(mockResponse['Enchantment: Cinderhulk']['group'], "JungleItems") 
		self.assertEqual(mockResponse['Enchantment: Cinderhulk']['image'], "3725.png") 
		self.assertEqual(mockResponse['Enchantment: Runeglaive']['group'], "JungleItems") 
		self.assertEqual(mockResponse['Enchantment: Runeglaive']['image'], "3724.png") 

	def test_model_items_2(self):
		try:
			conn = psycopg2.connect("dbname='hardcarry' user='admin' password='password'")
		except:
			print ("Unable to connect to the database.")
		cur = conn.cursor()
		try:
			cur.execute("""SELECT * FROM item""")
		except:
			print ("Query failed.")
		dbResponse = cur.fetchall()
		self.assertEqual(dbResponse[0][1], "JungleItems") 
		self.assertEqual(dbResponse[0][4], "3725.png") 
		self.assertEqual(dbResponse[1][1], "JungleItems") 
		self.assertEqual(dbResponse[1][4], "3724.png") 

	def test_model_items_3(self):
		apiResponse = urlopen('http://hardcarry.me/api/champions/Aatrox')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertEqual(jsonResponse['Enchantment: Cinderhulk']['group'], "JungleItems") 
		self.assertEqual(jsonResponse['Enchantment: Cinderhulk']['image'], "3725.png") 

# ----
# Main
# ----

if __name__ == "__main__" :
	main()


# .Unable to connect to the database.
# EE.Unable to connect to the database.
# EE.Unable to connect to the database.
# EE
# ======================================================================
# ERROR: test_model_abilities_2 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 78, in test_model_abilities_2
#     cur = conn.cursor()
# UnboundLocalError: local variable 'conn' referenced before assignment

# ======================================================================
# ERROR: test_model_abilities_3 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 93, in test_model_abilities_3
#     jsonResponse = json.loads(apiResponseRaw)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/__init__.py", line 318, in loads
#     return _default_decoder.decode(s)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/decoder.py", line 343, in decode
#     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/decoder.py", line 361, in raw_decode
#     raise ValueError(errmsg("Expecting value", s, err.value)) from None
# ValueError: Expecting value: line 1 column 1 (char 0)

# ======================================================================
# ERROR: test_model_champions_2 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 42, in test_model_champions_2
#     cur = conn.cursor()
# UnboundLocalError: local variable 'conn' referenced before assignment

# ======================================================================
# ERROR: test_model_champions_3 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 57, in test_model_champions_3
#     jsonResponse = json.loads(apiResponseRaw)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/__init__.py", line 318, in loads
#     return _default_decoder.decode(s)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/decoder.py", line 343, in decode
#     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/decoder.py", line 361, in raw_decode
#     raise ValueError(errmsg("Expecting value", s, err.value)) from None
# ValueError: Expecting value: line 1 column 1 (char 0)

# ======================================================================
# ERROR: test_model_items_2 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 114, in test_model_items_2
#     cur = conn.cursor()
# UnboundLocalError: local variable 'conn' referenced before assignment

# ======================================================================
# ERROR: test_model_items_3 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 129, in test_model_items_3
#     jsonResponse = json.loads(apiResponseRaw)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/__init__.py", line 318, in loads
#     return _default_decoder.decode(s)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/decoder.py", line 343, in decode
#     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/json/decoder.py", line 361, in raw_decode
#     raise ValueError(errmsg("Expecting value", s, err.value)) from None
# ValueError: Expecting value: line 1 column 1 (char 0)

# ----------------------------------------------------------------------
# Ran 9 tests in 0.371s

# FAILED (errors=6)

