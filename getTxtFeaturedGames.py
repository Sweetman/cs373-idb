from getFeaturedGames import add_games
import json, os
from time import sleep

if __name__ == '__main__':
	path = "%s/FeaturedGamesScraper" % (os.getcwd())
	os.chdir(path)
	jsonResponse = ""
	for i in os.listdir(os.getcwd()):
		if i.endswith(".txt"):
			f = open(i, "r")
			jsonResponse = json.load(f)
			add_games(jsonResponse)
			print("added games from %s" %(i))
		sleep(7)