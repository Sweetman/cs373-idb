from app import app, db
import sqlalchemy as sa

db.drop_all()
# uncomment this line if you're db is completely from scratch (ie you just dropped the DATABSE and just created it)
sa.orm.configure_mappers()
db.create_all()