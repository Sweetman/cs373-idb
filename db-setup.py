from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float

engine = create_engine('postgresql://admin@localhost/idb')
Base = declarative_base()

class Champion(Base):
	__tablename__ = 'champion'
	champ_name = Column(String, primary_key=True)
	# commenting the Blob's out because we need to discuss this
	# allytips = Column(Blob)
	# enemytips = Column(Blob)
	blurb = Column(String)
	id = Column(String)
	image = Column(String)
	attack = Column(Integer)
	defense = Column(Integer)
	magic = Column(Integer)
	key = Column(Integer)
	lore = Column(String)
	partype = Column(String)
	title = Column(String)
	# backref creates bidirectional relationship
	champion_skins = relationship("champion_skin", backref="champion")
	# uselist=False makes it 1:1 relationship
	champion_passive = relationship("champion_passive", uselist=False, backref="champion")
	abilities = relationship("ability", backref="champion")
	champion_info = relationship("champion_info", uselist=False, backref="champion")
	champion_tags = relationship("champion_tag", backref="champion")
	champion_stat = relationship("champion_stat", uselist=False, backref="champion")
	items = relationship("items", backref="champion")

class Champion_Skin(Base):
	__tablename__ = 'champion_skin'
	chromas = Column(Boolean)
	id = Column(String)
	skin_name = Column(String, primary_key=True)
	num = Column(Integer)
	champ_name = Column(String, ForeignKey('champion.champ_name'))


class Champion_Passive(Base):
	__tablename__ = 'champion_passive'
	description = Column(String)
	image = Column(String)
	passive_name = Column(String)
	champ_name = Column(String, ForeignKey('champion.champ_name'))

class Ability(Base):
	__tablename__ = 'ability'
	description = Column(String)
	costType = Column(String)
	id = Column(String)
	image = Column(String)
	maxrank = Column(Integer)
	spell_name = Column(String)
	champ_name = Column(String, ForeignKey('champion.champ_name'))

class Champion_Info(Base):
	__tablename__ = 'champion_info'
	attack = Column(Integer)
	defense = Column(Integer)
	difficulty = Column(Integer)
	magic = Column(Integer)
	champ_name = Column(String, ForeignKey('champion.champ_name'))

class Champion_Tag(Base):
	__tablename__ = 'champion_tag'
	tag_name = Column(String)
	champ_name = Column(String, ForeignKey('champion.champ_name'))

class Champion_Stat(Base):
	__tablename__ = 'champion_stat'
	armor = Column(Float)
	armorperlevel = Column(Float)
	attacklevel = Column(Float)
	attackdamageperlevel = Column(Float)
	attackrange = Column(Float)
	attackspeedoffset = Column(Float)
	attackspeedperlevel = Column(Float)
	crit = Column(Float)
	critperlevel = Column(Float)
	hp = Column(Float)
	hpperlevel = Column(Float)
	hpregen = Column(Float)
	hpregenperlevel = Column(Float)
	movespeed = Column(Float)
	mp = Column(Float)
	mpperlevel = Column(Float)
	mpregen = Column(Float)
	mpregenlevel = Column(Float)
	spellblock = Column(Float)
	spellblockperlevel = Column(Float)
	champ_name = Column(String, ForeignKey('champion.champ_name'))

class Item(Base):
	__tablename__ = 'item'
	item_name = Column(String)
	group = Column(String)
	description = Column(String)
	plaintext = Column(String)
	image = Column(String)
	champ_name = Column(String, ForeignKey('champion.champ_name'))
	item_stat = relationship("item_stat", uselist=False, backref="item")
	item_gold = relationship("item_gold", uselist=False, backref="item")
	items_tag = relationship("items_tag", backref="item")

class Item_Stat(Base):
	__tablename__ = 'item_stat'
	type = Column(String)
	stat_bonus = Column(Integer)
	item_name = Column(String, ForeignKey('item.item_name'))

class Item_Gold(Base):
	__tablename__ = 'item_gold'
	base = Column(Integer)
	purchaseable = Column(Boolean)
	total = Column(Integer)
	sell = Column(Integer)
	item_name = Column(String, ForeignKey('item.item_name'))

class Item_Tag(Base):
	__tablename__ = 'item_tag'
	tag_name = Column(String)
	id = Column(Integer, primary_key=True)
	item_name = Column(String, ForeignKey('item.item_name'))


Base.metadata.create_all(engine) 