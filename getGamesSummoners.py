from urllib.request import urlopen
from sqlalchemy import create_engine
import json
from app import db
from models import FeaturedGame, Summoner, Champion

apiResponse = urlopen('https://na.api.pvp.net/observer-mode/rest/featured?api_key=b5cf54ec-e9cf-4c5f-8009-74785a540ce4')
apiResponseInfo = apiResponse.info()
apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
jsonResponse = json.loads(apiResponseRaw)

db_featured_games = []
db_summoners = []
summoners = {}
summonerInfoUrls = []
summonerInfoNum = 0

for jsonFG in jsonResponse['gameList']:
	champions = []
	featured_game = {}
	featured_game['gameId'] = jsonFG['gameId']
	print(featured_game['gameId'])
	featured_game['gameLength'] = jsonFG['gameLength']
	print(featured_game['gameLength'])
	featured_game['gameMode'] = jsonFG['gameMode']
	print(featured_game['gameMode'])
	featured_game['gameStartTime'] = jsonFG['gameStartTime']
	print(featured_game['gameStartTime'])
	featured_game['gameType'] = jsonFG['gameType']
	print(featured_game['gameType'])
	featured_game['mapId'] = jsonFG['mapId']
	print(featured_game['mapId'])

	db_fg = FeaturedGame(featured_game['gameId'], featured_game['gameLength'],\
		featured_game['gameMode'],featured_game['gameStartTime'],featured_game['gameType'],\
		featured_game['mapId'])
	db_featured_games.append(db_fg)
	participants = jsonFG['participants']
	for participant in participants:
		curParticipantName = participant['summonerName']
		if curParticipantName not in summoners:
			summoner = {}

			# building requests to get more summoner info later
			if not summonerInfoNum % 10:
				summonerInfoUrls.append('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/')
			summonerInfoUrls[-1] += curParticipantName.replace(' ', '%20') + ','
			summonerInfoNum += 1
			
			summoner['name'] = participant['summonerName']
			summoner['profileIconId'] = participant['profileIconId']
			summoner['bot'] = participant['bot']
			summoner['championId'] = participant['championId']
			print(participant['championId'])
			print("start time: %s" %(jsonFG['gameStartTime']))
			champ = Champion.query.filter_by(championId=participant['championId']).first()
			db_fg.champions.append(champ)
			print("this game %d had summoner %s who was playing %s" %(db_fg.gameId, summoner['name'], champ.name))
			summoner['teamId'] = participant['teamId']
			summoner['gameId'] = jsonFG['gameId']

			summoners[curParticipantName] = summoner
		else:
			summoners[curParticipantName]['championId'].add(participant['championId'])
			summoners[curParticipantName]['teamId'].add(participant['teamId'])
			summoners[curParticipantName]['gameId'].add(participant['gameId'])
	# print(champions)
db.session.add_all(db_featured_games)
db.session.commit()
# to avoid too many requests causing an error, get all this stuff after the fact
# each summoner info url has 10 names. if you have too many in a request you get an error
jsonSummonerInfo = {}
for i in range(len(summonerInfoUrls)):
	summonerInfoUrls[i] += '?api_key=b5cf54ec-e9cf-4c5f-8009-74785a540ce4'
	summonerInfoUrls[i] = str(summonerInfoUrls[i].encode('ascii', 'ignore'))[2:-1]
	apiResponse = urlopen(summonerInfoUrls[i])
	apiResponseInfo = apiResponse.info()
	apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
	jsonSummonerInfo.update(json.loads(apiResponseRaw))

for summonerName in summoners:
	jsonSummonerName = summonerName.lower().replace(' ', '')
	summoners[summonerName]['summonerId'] = jsonSummonerInfo[jsonSummonerName]['id']
	summoners[summonerName]['summonerLevel'] = jsonSummonerInfo[jsonSummonerName]['summonerLevel']

	summoner = Summoner(summoners[summonerName]['summonerId'], summonerName, summoners[summonerName]['profileIconId'],\
		summoners[summonerName]['summonerLevel'], summoners[summonerName]['bot'])
	db_summoners.append(summoner)
	db_fg = FeaturedGame.query.filter_by(gameId=summoners[summonerName]['gameId']).first()
	db_fg.summoners.append(summoner)
	champ = Champion.query.filter_by(championId=summoners[summonerName]['championId']).first()
	summoner.champions.append(champ)
	db.session.commit()
db.session.commit()

