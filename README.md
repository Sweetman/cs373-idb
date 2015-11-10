# HardCarry

## Setup for local dev

Note: Everyone on the team has OS X, so these instructions will be for that environment until we host on a linux server

Required: [Python3](https://www.python.org/downloads/)

### Set up the virtual environment
```
pip install virtualenv
which python3 // outputs path to your python3, will be refered to as PYTHON3_PATH
virtualenv -p PYTHON3_PATH env
source env/bin/activate
```

You will know it worked when your shell prompt has (env) appended to the beginning.

To start and deactivate your virtualenv run the following (tab completion included)
```
source env/bin/activate
deactivate env
```

Edit the activate script for the virtualenv and add these commands to the bottom of the file
```
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://admin@localhost/idb"
```

Now install the requirements for the project
```
pip install -r requirements.txt
bower update
```


### Create the psql database
Install with homebrew or download the [Postgresql.app](http://postgresapp.com/)

Create a postgres server, user, and database.
```
psql
create database idb;
create user admin;
grant all privileges on database idb to admin;
```

### Set up database and run the server
Change directories into the idb app and upgrade the database to latest migrations
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

Populate the database with the scraping scripts. IT IS IMPORTANT THAT YOU RUN getChampionData.py FIRST.
```
python getChampionData.py
python getChampYoutube.py
python getFeaturedGames.py
python getTxtFeaturedGames.py
```

Start server
```
python manage.py runserver
```
