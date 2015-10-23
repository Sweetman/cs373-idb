from flask.ext.sqlalchemy import SQLAlchemy
from app import db

class Champion(db.Model):
	'''
	A champion is a person or being that has been summoned to wage battle in the League of Legends on the Fields of Justice. 
	They are the player-controlled characters in League of Legends, all of them bringing their own unique set of abilities, 
	traits and characteristics. Their fighting styles and attributes dictate their use and role in the Fields of Justice.
	A champion has a number of different relationships and sub-relationship entities.
	'''
	__tablename__ = 'champion'
	champ_name = db.Column(db.String, primary_key=True)
	# commenting the Blob's out because we need to discuss this
	# allytips = db.Column(Blob)
	# enemytips = db.Column(Blob)
	blurb = db.Column(db.String)
	id = db.Column(db.String)
	image = db.Column(db.String)
	attack = db.Column(db.Integer)
	defense = db.Column(db.Integer)
	magic = db.Column(db.Integer)
	key = db.Column(db.Integer)
	lore = db.Column(db.String)
	partype = db.Column(db.String)
	title = db.Column(db.String)
	# backref creates bidirectional db.relationship
	champion_skins = db.relationship("champion_skin", backref="champion")
	# uselist=False makes it 1:1 db.relationship
	champion_passive = db.relationship("champion_passive", uselist=False, backref="champion")
	abilities = db.relationship("ability", backref="champion")
	champion_info = db.relationship("champion_info", uselist=False, backref="champion")
	champion_tags = db.relationship("champion_tag", backref="champion")
	champion_stat = db.relationship("champion_stat", uselist=False, backref="champion")
	items = db.relationship("items", backref="champion")

class Champion_Skin(db.Model):
	'''
	Champions can be bought within the game and are used to decorate a champion. 
	A champion might have multiple skins.
	'''
	__tablename__ = 'champion_skin'
	chromas = db.Column(db.Boolean)
	id = db.Column(db.String)
	skin_name = db.Column(db.String, primary_key=True)
	num = db.Column(db.Integer)
	champ_name = db.Column(db.String, db.ForeignKey('champion.champ_name'))


class Champion_Passive(db.Model):
	'''
	Each champion has a single innate, passive ability.
	'''
	__tablename__ = 'champion_passive'
	description = db.Column(db.String)
	image = db.Column(db.String)
	passive_name = db.Column(db.String, primary_key=True)
	champ_name = db.Column(db.String, db.ForeignKey('champion.champ_name'))

class Ability(db.Model):
	'''
	A Champion's abilities are a unique characteristic of each champion that separates them apart from other champions. 
	Every champion has at least five unique abilities, four of which are learned throughout the course of the battle 
	and requires leveling the champion to acquire/spending ability points. There's a 1:M relationship between 
	Champion:Ability, as each champion possesses multiple abilities.
	'''
	__tablename__ = 'ability'
	description = db.Column(db.String)
	costType = db.Column(db.String)
	id = db.Column(db.String, primary_key=True)
	image = db.Column(db.String)
	maxrank = db.Column(db.Integer)
	spell_name = db.Column(db.String)
	champ_name = db.Column(db.String, db.ForeignKey('champion.champ_name'))

class Champion_Info(db.Model):
	'''
	Base stats of the champ.
	'''
	__tablename__ = 'champion_info'
	attack = db.Column(db.Integer)
	defense = db.Column(db.Integer)
	difficulty = db.Column(db.Integer)
	magic = db.Column(db.Integer)
	champ_name = db.Column(db.String, db.ForeignKey('champion.champ_name'), primary_key=True)

class Champion_Tag(db.Model):
	'''
	Tag refers to the category or the type of champ. A champion might be categorized as multiple types,
	such as a Tank, Support, Jungler, etc.
	'''
	__tablename__ = 'champion_tag'
	id = db.Column(db.Integer, primary_key=True)
	tag_name = db.Column(db.String)
	champ_name = db.Column(db.String, db.ForeignKey('champion.champ_name'))

class Champion_Stat(db.Model):
	'''
	These are the in-game stats that the champ will have depending on the level and items equipped.
	'''
	__tablename__ = 'champion_stat'
	armor = db.Column(db.Float)
	armorperlevel = db.Column(db.Float)
	attacklevel = db.Column(db.Float)
	attackdamageperlevel = db.Column(db.Float)
	attackrange = db.Column(db.Float)
	attackspeedoffset = db.Column(db.Float)
	attackspeedperlevel = db.Column(db.Float)
	crit = db.Column(db.Float)
	critperlevel = db.Column(db.Float)
	hp = db.Column(db.Float)
	hpperlevel = db.Column(db.Float)
	hpregen = db.Column(db.Float)
	hpregenperlevel = db.Column(db.Float)
	movespeed = db.Column(db.Float)
	mp = db.Column(db.Float)
	mpperlevel = db.Column(db.Float)
	mpregen = db.Column(db.Float)
	mpregenlevel = db.Column(db.Float)
	spellblock = db.Column(db.Float)
	spellblockperlevel = db.Column(db.Float)
	champ_name = db.Column(db.String, db.ForeignKey('champion.champ_name'), primary_key=True)

class Item(db.Model):
	'''
	As the game progresses, players acquire currency in the form of gold and can spend 
	it on powerful items to improve the champion's performance. Each item provides a 
	unique bonus such as faster movement, improved damage, increased durability, reduced ability 
	cooldowns, etc. There's a 1:M relationship between Champion:Item respecively, as each player 
	can purchase multiple items for their champion during the game.
	'''
	__tablename__ = 'item'
	item_name = db.Column(db.String, primary_key=True)
	group = db.Column(db.String)
	description = db.Column(db.String)
	plaintext = db.Column(db.String)
	image = db.Column(db.String)
	champ_name = db.Column(db.String, db.ForeignKey('champion.champ_name'))
	item_stat = db.relationship("item_stat", uselist=False, backref="item")
	item_gold = db.relationship("item_gold", uselist=False, backref="item")
	items_tag = db.relationship("items_tag", backref="item")

class Item_Stat(db.Model):
	'''
	The bonus that the item gives to the champ, raising a specific stat.
	'''
	__tablename__ = 'item_stat'
	type = db.Column(db.String)
	stat_bonus = db.Column(db.Integer)
	item_name = db.Column(db.String, db.ForeignKey('item.item_name'), primary_key=True)

class Item_Gold(db.Model):
	'''
	How much an item costs to buy and can be sold for.
	'''
	__tablename__ = 'item_gold'
	model = db.Column(db.Integer)
	purchaseable = db.Column(db.Boolean)
	total = db.Column(db.Integer)
	sell = db.Column(db.Integer)
	item_name = db.Column(db.String, db.ForeignKey('item.item_name'), primary_key=True)

class Item_Tag(db.Model):
	'''
	Category or type that the item belongs to.
	'''
	__tablename__ = 'item_tag'
	tag_name = db.Column(db.String)
	id = db.Column(db.Integer, primary_key=True)
	item_name = db.Column(db.String, db.ForeignKey('item.item_name'))