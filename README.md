# The Best Startup Alive

## Setup for local dev

Install python 3.5 via website download

Install pip

Install virtualenv

If you don't have postgreesql
```
brew install postgresql
```

initialize your virtual env by navigating to the project's root directory then
```
virtualenv venv
```

start your virtualenv by
```
source venv/bin/activate
```
ensure that your terminal prompt is in the virtualenv by noticing the (venv) on the left side of the prompt.


Install the required python and front-end packages
```
pip install -r requirements.txt
bower update
```

Create a postgres server, user, and database
```
pg_ctl -D /usr/local/var/postgres init
pg_ctl -D /usr/local/var/postgres start
createdb idb
```

Export the required settings
```
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://<user_name>@localhost/<database_name>"
```

Change directories into the idb app and migrate the databases
```
cd idb
python manage.py db upgrade
```

Start server with
```
python manage.py runserver
```
