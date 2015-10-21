#!/usr/bin/env python3

# -------------------------------
# Copyright (C) 2015
# League IDB
# -------------------------------

# -------
# Imports
# -------

from io       import StringIO
from urllib.request import urlopen
from unittest import main, TestCase

import json

# ----------
# TestModels
# ----------

class TestModels (TestCase):

	# ---------
	# Champions
	# ---------

	def test_model_champions_1(self):
		mockResponse = {"Aatrox": {"name": "Aatrox", "title": "the Darkin Blade"},
					    "Thresh": {"name": "Thresh", "partype": "Mana"} }
		self.assertEqual(mockResponse['Aatrox']['name'], "Aatrox") 
		self.assertEqual(mockResponse['Aatrox']['title'], "the Darkin Blade") 
		self.assertEqual(mockResponse['Thresh']['name'], "Thresh") 
		self.assertEqual(mockResponse['Thresh']['partype'], "Mana") 

	def test_model_champions_2(self):
		response = open("app/database/champions")
		jsonResponse = json.load(data)
		response.close()
		self.assertEqual(jsonResponse['Aatrox']['name'], "Aatrox") 
		self.assertEqual(jsonResponse['Aatrox']['title'], "the Darkin Blade") 
		self.assertEqual(jsonResponse['Thresh']['name'], "Thresh") 
		self.assertEqual(jsonResponse['Thresh']['partype'], "Mana") 

	def test_model_champions_3(self):
		apiResponse = urlopen('http://localhost:8080/api/champions/Aatrox')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertEqual(jsonResponse['name'], "Aatrox") 
		self.assertEqual(jsonResponse['title'], "the Darkin Blade") 

	# ------
	# Spells
	# ------

	def test_model_spells_1(self):
		mockResponse = {"0": {"spell_name": "Dark Flight", "maxrank": 5},
					    "1": {"spell_name": "Blades of Torment", "costType": "pofcurrentHealth"} }
		self.assertEqual(mockResponse["0"]['spell_name'], "Dark Flight") 
		self.assertEqual(mockResponse["0"]['maxrank'], 5) 
		self.assertEqual(mockResponse["1"]['spell_name'], "Blades of Torment") 
		self.assertEqual(mockResponse["1"]['costType'], "pofcurrentHealth") 

	def test_model_spells_2(self):
		response = open("app/database/spells")
		jsonResponse = json.load(data)
		response.close()
		self.assertEqual(jsonResponse["0"]['spell_name'], "Dark Flight") 
		self.assertEqual(jsonResponse["0"]['maxrank'], 5) 
		self.assertEqual(jsonResponse["1"]['spell_name'], "Blades of Torment") 
		self.assertEqual(jsonResponse["1"]['costType'], "pofcurrentHealth") 

	def test_model_spells_3(self):
		apiResponse = urlopen('http://localhost:8080/api/spells/0')
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
		response = open("app/database/items")
		jsonResponse = json.load(data)
		response.close()
		self.assertEqual(jsonResponse['Enchantment: Cinderhulk']['group'], "JungleItems") 
		self.assertEqual(jsonResponse['Enchantment: Cinderhulk']['image'], "3725.png") 
		self.assertEqual(jsonResponse['Enchantment: Runeglaive']['group'], "JungleItems") 
		self.assertEqual(jsonResponse['Enchantment: Runeglaive']['image'], "3724.png") 

	def test_model_items_3(self):
		apiResponse = urlopen('http://localhost:8080/api/champions/Aatrox')
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


# .EE.EE.EE
# ======================================================================
# ERROR: test_model_champions_2 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 37, in test_model_champions_2
#     response = open("app/database/champions")
# FileNotFoundError: [Errno 2] No such file or directory: 'app/database/champions'

# ======================================================================
# ERROR: test_model_champions_3 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 46, in test_model_champions_3
#     apiResponse = urlopen('http://localhost:8080/api/champions/Aatrox')
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 153, in urlopen
#     return opener.open(url, data, timeout)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 461, in open
#     response = meth(req, response)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 571, in http_response
#     'http', request, response, code, msg, hdrs)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 499, in error
#     return self._call_chain(*args)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 433, in _call_chain
#     result = func(*args)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 579, in http_error_default
#     raise HTTPError(req.full_url, code, msg, hdrs, fp)
# urllib.error.HTTPError: HTTP Error 404: Not Found

# ======================================================================
# ERROR: test_model_items_2 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 95, in test_model_items_2
#     response = open("app/database/items")
# FileNotFoundError: [Errno 2] No such file or directory: 'app/database/items'

# ======================================================================
# ERROR: test_model_items_3 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 104, in test_model_items_3
#     apiResponse = urlopen('http://localhost:8080/api/champions/Aatrox')
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 153, in urlopen
#     return opener.open(url, data, timeout)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 461, in open
#     response = meth(req, response)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 571, in http_response
#     'http', request, response, code, msg, hdrs)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 499, in error
#     return self._call_chain(*args)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 433, in _call_chain
#     result = func(*args)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 579, in http_error_default
#     raise HTTPError(req.full_url, code, msg, hdrs, fp)
# urllib.error.HTTPError: HTTP Error 404: Not Found

# ======================================================================
# ERROR: test_model_spells_2 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 66, in test_model_spells_2
#     response = open("app/database/spells")
# FileNotFoundError: [Errno 2] No such file or directory: 'app/database/spells'

# ======================================================================
# ERROR: test_model_spells_3 (__main__.TestModels)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 75, in test_model_spells_3
#     apiResponse = urlopen('http://localhost:8080/api/spells/0')
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 153, in urlopen
#     return opener.open(url, data, timeout)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 461, in open
#     response = meth(req, response)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 571, in http_response
#     'http', request, response, code, msg, hdrs)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 499, in error
#     return self._call_chain(*args)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 433, in _call_chain
#     result = func(*args)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/urllib/request.py", line 579, in http_error_default
#     raise HTTPError(req.full_url, code, msg, hdrs, fp)
# urllib.error.HTTPError: HTTP Error 404: Not Found

# ----------------------------------------------------------------------
# Ran 9 tests in 0.043s

# FAILED (errors=6)

