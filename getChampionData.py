from urllib.request import urlopen
from sqlalchemy import create_engine
import json
from app import db
from models import Champion, ChampionAbility


"""
Champions and Abilities
"""

apiResponse = urlopen('https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=allytips,enemytips,image,info,lore,partype,passive,skins,spells,stats&api_key=b5cf54ec-e9cf-4c5f-8009-74785a540ce4')
apiResponseInfo = apiResponse.info()
apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
jsonResponse = json.loads(apiResponseRaw)

champion_list = []
abilities = []
for jsonChamp in jsonResponse['data']:
	champData = jsonResponse['data'][jsonChamp]
	champion = {}
	champion['name'] = champData['name']
	champion['allytips'] = champData['allytips']
	champion['enemytips'] = champData['enemytips']
	champion['championId'] = champData['id']
	champion['imageFileName'] = champData['image']['full']
	champion['lore'] = champData['lore']
	champion['partype'] = champData['partype']
	champion['title'] = champData['title']
	champion['attack'] = champData['info']['attack']
	champion['defense'] = champData['info']['defense']
	champion['magic'] = champData['info']['magic']
	champion['difficulty'] = champData['info']['difficulty']
	champion['passiveDescription'] = champData['passive']['description']
	champion['passiveImageFileName'] = champData['passive']['image']['full']
	champion['passiveName'] = champData['passive']['name']
	champion['armor'] = champData['stats']['armor']
	champion['armorperlevel'] = champData['stats']['armorperlevel']
	champion['attackdamage'] = champData['stats']['attackdamage']
	champion['attackdamageperlevel'] = champData['stats']['attackdamageperlevel']
	champion['attackrange'] = champData['stats']['attackrange']
	champion['attackspeedoffset'] = champData['stats']['attackspeedoffset']
	champion['attackspeedperlevel'] = champData['stats']['attackspeedperlevel']
	champion['crit'] = champData['stats']['crit']
	champion['critperlevel'] = champData['stats']['critperlevel']
	champion['hp'] = champData['stats']['hp']
	champion['hpperlevel'] = champData['stats']['hpperlevel']
	champion['hpregen'] = champData['stats']['hpregen']
	champion['hpregenperlevel'] = champData['stats']['hpregenperlevel']
	champion['movespeed'] = champData['stats']['movespeed']
	champion['mp'] = champData['stats']['mp']
	champion['mpperlevel'] = champData['stats']['mpperlevel']
	champion['mpregen'] = champData['stats']['mpregen']
	champion['mpregenperlevel'] = champData['stats']['mpregenperlevel']
	champion['spellblock'] = champData['stats']['spellblock']
	champion['spellblockperlevel'] = champData['stats']['spellblockperlevel']
	champion['numberOfSkins'] = len(champData['skins'])
	champ = Champion.query.filter_by(name=champion['name']).first()

	if champ is None:
		champ = Champion(champion['name'],champion['championId'],champion['imageFileName'],champion['lore'],\
			champion['partype'],champion['title'],champion['attack'],champion['defense'], champion['magic'],\
			champion['difficulty'],champion['passiveDescription'],champion['passiveImageFileName'],\
			champion['passiveName'], champion['armor'], champion['armorperlevel'],champion['attackdamage'],
			champion['attackdamageperlevel'], champion['attackrange'], champion['attackspeedoffset'],\
			champion['attackspeedperlevel'], champion['crit'], champion['hp'], champion['hpperlevel'],\
			champion['hpregen'],champion['hpregenperlevel'],champion['movespeed'],champion['mp'],\
			champion['mpperlevel'],champion['mpregen'],champion['mpregenperlevel'], champion['spellblock'],\
			champion['spellblockperlevel'], champion['numberOfSkins'])
		print("%s created" %(champ.name))
		spells = champData['spells']
		for spell in spells:
			ability = {}
			ability['description'] = spell['description']
			ability['costType'] = spell['costType']
			# note -- ability does not have ID provided by Riot
			ability['imageFileName'] = spell['image']['full']
			ability['maxrank'] = spell['maxrank']
			ability['name'] = spell['name']
			ability['tooltip'] = spell['tooltip']
			ability['championId'] = champData['id']
			ability = ChampionAbility(ability['name'], ability['description'], ability['costType'], ability['imageFileName'],\
				ability['maxrank'], ability['name'], ability['tooltip'])
			print("%s created" % (ability.name))
			champ.abilities.append(ability)
		champion_list.append(champ)
	else:
		print("%s is already in the db" %(champion['name']))
if champion_list:
	db.session.add_all(champion_list)
	db.session.commit()
	print("%d champions added" %(len(champion_list)))
else:
	print("no champions added")