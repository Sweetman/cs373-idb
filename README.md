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

Make sure you have a user called admin already.
Now run the following:
```
make database
```

Start server
```
python manage.py runserver
```
