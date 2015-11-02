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
	championId = db.Column(db.Integer, primary_key=True)
	image_file_name = db.Column(db.String)
	lore = db.Column(db.String)
	partype = db.Column(db.String)
	title = db.Column(db.String)
	attack = db.Column(db.Integer)
	defense = db.Column(db.Integer)
	magic = db.Column(db.Integer)
	difficulty = db.Column(db.Integer)
	passive_description = db.Column(db.String)
	passive_image_file_name = db.Column(db.String)
	passive_name = db.Column(db.String)
	stat_armor = db.Column(db.Float)
	stat_armorperlevel = db.Column(db.Float)
	stat_attackdamage = db.Column(db.Float)
	stat_attackdamageperlevel = db.Column(db.Float)
	stat_attackrange = db.Column(db.Float)
	stat_attackspeedoffset = db.Column(db.Float)
	stat_attackspeedperlevel = db.Column(db.Float)
	stat_crit = db.Column(db.Float)
	stat_hp = db.Column(db.Float)
	stat_hpperlevel = db.Column(db.Float)
	stat_hpregen = db.Column(db.Float)
	stat_hpregenperlevel = db.Column(db.Float)
	stat_movespeed = db.Column(db.Float)
	stat_mp = db.Column(db.Float)
	stat_mpperlevel = db.Column(db.Float)
	stat_mpregen = db.Column(db.Float)
	stat_mpregenperlevel = db.Column(db.Float)
	stat_spellblock = db.Column(db.Float)
	stat_spellblockperlevel = db.Column(db.Float)
	number_of_skins = db.Column(db.Integer)
	abilities = db.relationship('ChampionAbility', backref='champion',
                                lazy='dynamic')

class ChampionAbility(db.Model):
	"""
	A Champion's abilities are a unique characteristic of each champion that separates them apart from other champions. 
	Every champion has at least five unique abilities, four of which are learned throughout the course of the battle 
	and requires leveling the champion to acquire/spending ability points. There's a 1:M relationship between 
	Champion:Ability, as each champion possesses multiple abilities.
	"""
	__tablename__ = 'champion_ability'
	description = db.Column(db.String)
	costType = db.Column(db.String)
	id = db.Column(db.String, primary_key=True)
	image = db.Column(db.String)
	maxrank = db.Column(db.Integer)
	spell_name = db.Column(db.String)
	championId = db.Column(db.Integer, db.ForeignKey('champion.championId'))

class Summoner(db.Model):
	__tablename__ = 'summoner'
	summoner_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	profileIconId = db.Column(db.Integer)
	summonerLevel = db.Column(db.Integer)
	bot = db.Column(db.Boolean)
	championId = db.Column(db.Integer)
	teamId = db.Column(db.Integer)
	champions = db.relationship('Champion', secondary=summoners_champions, backref=db.backref('summoners', lazy='dynamic'), lazy='dynamic')

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
