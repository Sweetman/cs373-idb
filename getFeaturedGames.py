from urllib.request import urlopen
from sqlalchemy import create_engine
import json
from app import db
from models import FeaturedGame, Summoner, Champion

def add_games(jsonResponse):
	db_featured_games = []
	db_summoner_champs = {}

	for jsonFG in jsonResponse['gameList']:
		if FeaturedGame.query.filter_by(gameId=jsonFG['gameId']).first() is not None:
			print("game %d is already in the database" % (jsonFG['gameId']))
		else:
			featured_game = {}
			featured_game['gameId'] = jsonFG['gameId']
			featured_game['gameLength'] = jsonFG['gameLength']
			featured_game['gameMode'] = jsonFG['gameMode']
			featured_game['gameStartTime'] = jsonFG['gameStartTime']
			featured_game['gameType'] = jsonFG['gameType']
			featured_game['mapId'] = jsonFG['mapId']

			db_fg = FeaturedGame(featured_game['gameId'], featured_game['gameLength'],\
				featured_game['gameMode'],featured_game['gameStartTime'],featured_game['gameType'],\
				featured_game['mapId'])
			db_featured_games.append(db_fg)
			participants = jsonFG['participants']
			jsonSummonerInfo = {}
			summonerInfoUrl = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/'
			# makes the url for all the summoners in the game
			for participant in participants:
				curParticipantName = participant['summonerName']
				print("curPartipantName: %s" % (curParticipantName))
				summonerInfoUrl += curParticipantName.replace(' ', '%20') + ','
				champ = Champion.query.filter_by(championId=participant['championId']).first()
				db_fg.champions.append(champ)
				db_summoner_champs[curParticipantName] = champ

			summonerInfoUrl += '?api_key=b5cf54ec-e9cf-4c5f-8009-74785a540ce4'
			summonerInfoUrl = str(summonerInfoUrl.encode('ascii', 'ignore'))[2:-1]
			apiResponse = urlopen(summonerInfoUrl)
			apiResponseInfo = apiResponse.info()
			apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
			jsonSummonerInfo.update(json.loads(apiResponseRaw))

			for participant in participants:
				summoner = participant['summonerName'].lower().replace(' ', '')
				if Summoner.query.filter_by(name=summoner).first() is not None:
					db_fg.summoners.append(Summoner.query.filter_by(name=summoner).first())
				else:
					# hard coded false value because there probably shouldn't be a bot in a featured game
					summoner = Summoner(jsonSummonerInfo[summoner]['id'], participant['summonerName'], jsonSummonerInfo[summoner]['profileIconId'], jsonSummonerInfo[summoner]['summonerLevel'], False)
					print(summoner.name)
					db_fg.summoners.append(summoner)
			db.session.commit()

if __name__ == '__main__':	
	apiResponse = urlopen('https://na.api.pvp.net/observer-mode/rest/featured?api_key=b5cf54ec-e9cf-4c5f-8009-74785a540ce4')
	apiResponseInfo = apiResponse.info()
	apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
	jsonResponse = json.loads(apiResponseRaw)
	add_games(jsonResponse)