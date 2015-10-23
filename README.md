# The Best Startup Alive

## Setup for local dev

Note: Everyone on the team has OS X, so these instructions will be for that environment until we host on a linux server

Required: [Python3](https://www.python.org/downloads/)

### Set up the virtual environment
Install virtualenv
```
pip install virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
mkdir -p $WORKON_HOME
which virtualenvwrapper.sh
source /path/outputted/by/which/command
```

Create a virtualenv for the project with python3
```
mkvirtualenv -p /path/to/python3 idb
```
You will know it worked when your shell prompt has (idb) appended to the beginning.

To start and deactivate your virtualenv run the following (tab completion included)
```
workon idb
deactivate idb
```

Edit the postactivate script for the virtualenv and add these commands
```
cd ~/path/to/project
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://admin@localhost/idb"
```

Change directories into the project's root directory and install the required python and front-end packages
Omit workon idb if you haven't set up the postactivate script with the cd command
```
workon idb
pip install -r requirements.txt
bower update
```


### Create the psql database
Install with homebrew or download the [Postgresql.app](http://postgresapp.com/)
Start your psql through the app or type the command
```
postgres -D /usr/local/pgsql/data
```

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
cd idb
python manage.py db upgrade
```

Start server
```
python manage.py runserver
```
