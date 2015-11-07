from models import Champion
from app import db

f = open("champion_yt.txt", "r")
for line in f:
	line = line.split(",")
	print(line[0])
	champ = Champion.query.filter_by(name=line[0]).first()
	print(champ.name)
	champ.youtube = line[1]
	print("adding youtube video %s" %(champ.youtube))
	db.session.commit()