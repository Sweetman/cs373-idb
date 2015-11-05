from flask.ext.sqlalchemy import SQLAlchemy
from app import db

summoners_champions = db.Table('summoners_champions',
    db.Column('summoner_id', db.Integer, db.ForeignKey('summoner.summoner_id')),
    db.Column('champion_id', db.Integer, db.ForeignKey('champion.championId'))
)

featuredgames_champions = db.Table('featuredgames_champions',
    db.Column('featuredgame_id', db.Integer, db.ForeignKey('featured_game.gameId')),
    db.Column('champion_id', db.Integer, db.ForeignKey('champion.championId'))
)

featuredgames_summoners = db.Table('featuredgames_summoners',
    db.Column('featuredgame_id', db.Integer, db.ForeignKey('featured_game.gameId')),
    db.Column('summoner_id', db.Integer, db.ForeignKey('summoner.summoner_id'))
)

class Champion(db.Model):
	"""
	A champion is a person or being that has been summoned to wage battle in the League of Legends on the Fields of Justice. 
	They are the player-controlled characters in League of Legends, all of them bringing their own unique set of abilities, 
	traits and characteristics. Their fighting styles and attributes dictate their use and role in the Fields of Justice.
	A champion has a number of different relationships and sub-relationship entities.
	"""
	__tablename__ = 'champion'
	name = db.Column(db.String)
	# commenting the Blob's out because we need to discuss this
	# allytips = db.Column(Blob)
	# enemytips = db.Column(Blob)
	id = db.Column(db.Integer, primary_key=True)
	imageFileName = db.Column(db.String)
	lore = db.Column(db.String)
	partype = db.Column(db.String)
	title = db.Column(db.String)
	attack = db.Column(db.Integer)
	defense = db.Column(db.Integer)
	magic = db.Column(db.Integer)
	difficulty = db.Column(db.Integer)
	passive_description = db.Column(db.String)
	passive_image_file_name = db.Column(db.String)
	passiveName = db.Column(db.String)
	armor = db.Column(db.Float)
	armorperlevel = db.Column(db.Float)
	attackdamage = db.Column(db.Float)
	attackdamageperlevel = db.Column(db.Float)
	attackrange = db.Column(db.Float)
	attackspeedoffset = db.Column(db.Float)
	attackspeedperlevel = db.Column(db.Float)
	crit = db.Column(db.Float)
	hp = db.Column(db.Float)
	hpperlevel = db.Column(db.Float)
	hpregen = db.Column(db.Float)
	hpregenperlevel = db.Column(db.Float)
	movespeed = db.Column(db.Float)
	mp = db.Column(db.Float)
	mpperlevel = db.Column(db.Float)
	mpregen = db.Column(db.Float)
	mpregenperlevel = db.Column(db.Float)
	spellblock = db.Column(db.Float)
	spellblockperlevel = db.Column(db.Float)
	numberOfSkins = db.Column(db.Integer)
	abilities = db.relationship('ChampionAbility', backref="champion", cascade="all, delete-orphan" , lazy='dynamic')

	def __init__(self, name, id, imageFileName, lore, partype, title, attack, defense, magic,\
		difficulty, passiveDescription, passiveImageFileName, passiveName, armor, armorperlevel,\
		attackdamage, attackdamageperlevel, attackrange, attackspeedoffset, attackspeedperlevel,\
		crit, hp, hpperlevel, hpregen, hpregenperlevel, movespeed, mp, mpperlevel, mpregen,\
		mpregenperlevel, spellblock, spellblockperlevel, numberofskins):
		self.name = name
		self.id = id
		self.imageFileName = imageFileName
		self.lore = lore
		self.partype = partype
		self.title = title
		self.attack = attack
		self.defense = defense
		self.magic = magic
		self.difficulty = difficulty
		self.passive_description = passiveDescription
		self.passive_image_file_name = passiveImageFileName
		self.passiveName = passiveName
		self.armor = armor
		self.armorperlevel = armorperlevel
		self.attackdamage = attackdamage
		self.attackdamageperlevel = attackdamageperlevel
		self.attackrange = attackrange
		self.attackspeedoffset = attackspeedoffset
		self.attackspeedperlevel = attackspeedperlevel
		self.crit = crit
		self.hp = hp
		self.hpperlevel = hpperlevel
		self.hpregen = hpregen
		self.hpregenperlevel = hpregenperlevel
		self.movespeed = movespeed
		self.mp = mp
		self.mpperlevel = mpperlevel
		self.mpregen = mpregen
		self.mpregenperlevel = mpregenperlevel
		self.spellblock = spellblock
		self.spellblockperlevel = spellblockperlevel
		self.numberOfSkins = numberofskins

class ChampionAbility(db.Model):
	"""
	A Champion's abilities are a unique characteristic of each champion that separates them apart from other champions. 
	Every champion has at least five unique abilities, four of which are learned throughout the course of the battle 
	and requires leveling the champion to acquire/spending ability points. There's a 1:M relationship between 
	Champion:Ability, as each champion possesses multiple abilities.
	"""
	__tablename__ = 'champion_ability'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	description = db.Column(db.String)
	costType = db.Column(db.String)
	image = db.Column(db.String)
	maxrank = db.Column(db.Integer)
	spell_name = db.Column(db.String)
	championId = db.Column(db.Integer, db.ForeignKey('champion.championId'))
	def __init__(self, name, description, costType, image, maxrank, spell_name):
		self.name = name
		self.description = description
		self.costType = costType
		self.image = self.image
		self.maxrank = maxrank
		self.spell_name = spell_name

class Summoner(db.Model):
	__tablename__ = 'summoner'
	summoner_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	profileIconId = db.Column(db.Integer)
	summonerLevel = db.Column(db.Integer)
	bot = db.Column(db.Boolean)
	championId = db.Column(db.Integer)
	teamId = db.Column(db.Integer)
	championId = db.Column(db.Integer, db.ForeignKey('champion.championId'))
	champions = db.relationship('Champion', secondary=summoners_champions, backref=db.backref('summoners', lazy='dynamic'), lazy='dynamic')
	def __init__(self, summoner_id, name, profileIconId, summonerLevel, bot):
		self.summoner_id = summoner_id
		self.name = name
		self.profileIconId = profileIconId
		self.summonerLevel = summonerLevel
		self.bot = bot

class FeaturedGame(db.Model):
	__tablename__ = 'featured_game'
	gameId = db.Column(db.Integer, primary_key=True)
	gameLength = db.Column(db.Integer)
	gameMode = db.Column(db.String)
	gameStartTime = db.Column(db.Integer)
	gameType = db.Column(db.String)
	mapId = db.Column(db.Integer)
	champions = db.relationship('Champion', secondary=featuredgames_champions, backref=db.backref('featured_games', lazy='dynamic'))
	summoners = db.relationship('Summoner', secondary=featuredgames_summoners, backref=db.backref('featured_games'))
	def __init__(self, gameId, gameLength, gameMode, gameStartTime, gameType, mapId):
		self.gameId = gameId
		self.gameLength = gameLength
		self.gameMode = gameMode
		self.gameStartTime = gameStartTime
		self.gameType = gameType
		self.mapId = mapId