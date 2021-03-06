from flask.ext.sqlalchemy import SQLAlchemy
from app import db
import json
from sqlalchemy_searchable import make_searchable
from sqlalchemy_utils.types import TSVectorType

make_searchable()

def get_dict_from_obj(obj):
	fields = {}
	for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
		if(field is not "search_vector"):
			data = obj.__getattribute__(field)
			try:
				json.dumps(data)
				fields[field] = data
			except TypeError:
				pass
	return fields

summoners_champions = db.Table('summoners_champions',
	db.Column('summoner_id', db.Integer, db.ForeignKey('summoner.id')),
	db.Column('champion_id', db.Integer, db.ForeignKey('champion.championId'))
)

featuredgames_champions = db.Table('featuredgames_champions',
	db.Column('featuredgame_id', db.Integer, db.ForeignKey('featured_game.id')),
	db.Column('champion_id', db.Integer, db.ForeignKey('champion.championId'))
)

featuredgames_summoners = db.Table('featuredgames_summoners',
	db.Column('featuredgame_id', db.Integer, db.ForeignKey('featured_game.id')),
	db.Column('summoner_id', db.Integer, db.ForeignKey('summoner.id'))
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
	youtube = db.Column(db.String, nullable=True)
	abilities = db.relationship('ChampionAbility', backref="champion", cascade="all, delete-orphan")
	search_vector = db.Column(TSVectorType('name', 'lore', 'partype', 'title', 'passive_description', 'passive_name'))

	def __init__(self, name, championId, imageFileName, lore, partype, title, attack, defense, magic,\
		difficulty, passiveDescription, passiveImageFileName, passiveName, armor, armorperlevel,\
		attackdamage, attackdamageperlevel, attackrange, attackspeedoffset, attackspeedperlevel,\
		crit, hp, hpperlevel, hpregen, hpregenperlevel, movespeed, mp, mpperlevel, mpregen,\
		mpregenperlevel, spellblock, spellblockperlevel, numberofskins):
		self.name = name
		self.championId = championId
		self.image_file_name = imageFileName
		self.lore = lore
		self.partype = partype
		self.title = title
		self.attack = attack
		self.defense = defense
		self.magic = magic
		self.difficulty = difficulty
		self.passive_description = passiveDescription
		self.passive_image_file_name = passiveImageFileName
		self.passive_name = passiveName
		self.stat_armor = armor
		self.stat_armorperlevel = armorperlevel
		self.stat_attackdamage = attackdamage
		self.stat_attackdamageperlevel = attackdamageperlevel
		self.stat_attackrange = attackrange
		self.stat_attackspeedoffset = attackspeedoffset
		self.stat_attackspeedperlevel = attackspeedperlevel
		self.stat_crit = crit
		self.stat_hp = hp
		self.stat_hpperlevel = hpperlevel
		self.stat_hpregen = hpregen
		self.stat_hpregenperlevel = hpregenperlevel
		self.stat_movespeed = movespeed
		self.stat_mp = mp
		self.stat_mpperlevel = mpperlevel
		self.stat_mpregen = mpregen
		self.stat_mpregenperlevel = mpregenperlevel
		self.stat_spellblock = spellblock
		self.stat_spellblockperlevel = spellblockperlevel
		self.number_of_skins = numberofskins

	def serialize(self):
		fields = get_dict_from_obj(self)
		fields['abilities'] = self.serialize_abilities()
		fields['featured_games'] = self.serialize_featured_games()
		fields['summoners'] = self.serialize_summoners()
		return fields

	def serialize_abilities(self):
		abilities = {}
		for ability in self.abilities:
			ability_data = get_dict_from_obj(ability)
			abilities[ability.name] = ability_data
		return abilities

	def serialize_featured_games(self):
		featured_games = {}
		for featured_game in self.featured_games:
			featured_game_data = get_dict_from_obj(featured_game)
			featured_games[featured_game.id] = featured_game_data
		return featured_games

	def serialize_summoners(self):
		summoners = {}
		for summoner in self.summoners:
			summoner_data = get_dict_from_obj(summoner)
			summoners[summoner.name] = summoner_data
		return summoners

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
	tooltip = db.Column(db.String)
	championId = db.Column(db.Integer, db.ForeignKey('champion.championId'))
	search_vector = db.Column(TSVectorType('name', 'description', 'spell_name', 'tooltip'))
	def __init__(self, name, description, costType, image, maxrank, spell_name, tooltip):
		self.name = name
		self.description = description
		self.costType = costType
		self.image = self.image
		self.maxrank = maxrank
		self.spell_name = spell_name
		self.tooltip = tooltip

	def serialize(self):
		return get_dict_from_obj(self)

class Summoner(db.Model):
	__tablename__ = 'summoner'
	id = db.Column(db.Integer, primary_key=True)
	summoner_id = db.Column(db.Integer)
	name = db.Column(db.String)
	profileIconId = db.Column(db.Integer)
	summonerLevel = db.Column(db.Integer)
	bot = db.Column(db.Boolean)
	champions = db.relationship('Champion', secondary=summoners_champions, backref=db.backref('summoners'))
	search_vector = db.Column(TSVectorType('name'))
	def __init__(self, summoner_id, name, profileIconId, summonerLevel, bot):
		self.summoner_id = summoner_id
		self.name = name
		self.profileIconId = profileIconId
		self.summonerLevel = summonerLevel
		self.bot = bot

	def serialize(self):
		fields = get_dict_from_obj(self)
		fields['champions'] = self.serialize_champions()
		fields['featured_games'] = self.serialize_featured_games()
		return fields

	def serialize_champions(self):
		champions = {}
		for champion in self.champions:
			champion_data = get_dict_from_obj(champion)
			champions[champion.name] = champion_data
		return champions

	def serialize_featured_games(self):
		featured_games = {}
		for featured_game in self.featured_games:
			featured_game_data = get_dict_from_obj(featured_game)
			featured_games[featured_game.id] = featured_game_data
		return featured_games

class FeaturedGame(db.Model):
	__tablename__ = 'featured_game'
	id = db.Column(db.Integer, primary_key=True)
	gameId = db.Column(db.Numeric)
	gameLength = db.Column(db.Integer)
	game_mode = db.Column(db.String)
	gameStartTime = db.Column(db.Numeric)
	game_type = db.Column(db.String)
	mapId = db.Column(db.Integer)
	champions = db.relationship('Champion', secondary=featuredgames_champions, backref=db.backref('featured_games'))
	summoners = db.relationship('Summoner', secondary=featuredgames_summoners, backref=db.backref('featured_games'))
	search_vector = db.Column(TSVectorType('game_mode', 'game_type'))
	def __init__(self, gameId, gameLength, gameMode, gameStartTime, gameType, mapId):
		self.gameId = gameId
		self.gameLength = gameLength
		self.game_mode = gameMode
		self.gameStartTime = gameStartTime
		self.game_type = gameType
		self.mapId = mapId

	def serialize(self):
		fields = get_dict_from_obj(self)
		fields['champions'] = self.serialize_champions()
		fields['summoners'] = self.serialize_summoners()
		return fields

	def serialize_champions(self):
		champions = {}
		for champion in self.champions:
			champion_data = get_dict_from_obj(champion)
			champions[champion.name] = champion_data
		return champions

	def serialize_summoners(self):
		summoners = {}
		for summoner in self.summoners:
			summoner_data = get_dict_from_obj(summoner)
			summoners[summoner.name] = summoner_data
		return summoners