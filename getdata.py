from urllib.request import urlopen
from sqlalchemy import create_engine
import json


"""
Champions and Abilities
"""

apiResponse = urlopen('https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=allytips,enemytips,image,info,lore,partype,passive,skins,spells,stats&api_key=b5cf54ec-e9cf-4c5f-8009-74785a540ce4')
apiResponseInfo = apiResponse.info()
apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
jsonResponse = json.loads(apiResponseRaw)

champions = {}
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

	champions[champion['name']] = champion

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

		abilities.append(ability)


"""
Featured games and Summoners
"""

apiResponse = urlopen('https://na.api.pvp.net/observer-mode/rest/featured?api_key=b5cf54ec-e9cf-4c5f-8009-74785a540ce4')
apiResponseInfo = apiResponse.info()
apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
jsonResponse = json.loads(apiResponseRaw)

featured_games = {}
summoners = {}
summonerInfoUrls = []
summonerInfoNum = 0
for jsonFG in jsonResponse['gameList']:
	# fgData = jsonResponse['gameList'][jsonFG]
	if jsonFG['gameId'] not in featured_games:
		featured_game = {}
		featured_game['gameId'] = jsonFG['gameId']
		featured_game['gameLength'] = jsonFG['gameLength']
		featured_game['gameMode'] = jsonFG['gameMode']
		featured_game['gameStartTime'] = jsonFG['gameStartTime']
		featured_game['gameType'] = jsonFG['gameType']
		featured_game['mapId'] = jsonFG['mapId']

		featured_games[featured_game['gameId']] = featured_game

	participants = jsonFG['participants']
	for participant in participants:
		curParticipantName = participant['summonerName']
		if curParticipantName not in summoners:
			summoner = {}
			if not summonerInfoNum % 10:
				summonerInfoUrls.append('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/')
			summonerInfoUrls[-1] += curParticipantName.replace(' ', '%20') + ','
			summonerInfoNum += 1
			summoner['name'] = participant['summonerName']
			summoner['profileIconId'] = participant['profileIconId']
			summoner['bot'] = participant['bot']
			summoner['championId'] = {participant['championId']}
			summoner['teamId'] = {participant['teamId']}
			summoner['gameId'] = {jsonFG['gameId']}

			summoners[curParticipantName] = summoner
		else:
			summoners[curParticipantName]['championId'].add(participant['championId'])
			summoners[curParticipantName]['teamId'].add(participant['teamId'])
			summoners[curParticipantName]['gameId'].add(participant['gameId'])

# to avoid too many requests causing an error, get all this stuff after the fact
jsonSummonerInfo = {}
for i in range(len(summonerInfoUrls)):
	summonerInfoUrls[i] += '?api_key=b5cf54ec-e9cf-4c5f-8009-74785a540ce4'
	summonerInfoUrls[i] = str(summonerInfoUrls[i].encode('ascii', 'ignore'))[2:-1]
	print(summonerInfoUrls)
	apiResponse = urlopen(summonerInfoUrls[i])
	apiResponseInfo = apiResponse.info()
	apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
	jsonSummonerInfo.update(json.loads(apiResponseRaw))
print(summonerInfoUrls)

print("\n\n\n\n" + str(jsonSummonerInfo))

for summonerName in summoners:
	jsonSummonerName = summonerName.lower().replace(' ', '')
	summoners[summonerName]['summonerId'] = jsonSummonerInfo[jsonSummonerName]['id']
	summoners[summonerName]['summonerLevel'] = jsonSummonerInfo[jsonSummonerName]['summonerLevel']







print(summoners)


