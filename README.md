# The Best Startup Alive

## Setup for local dev

Install the required python and front-end packages
```
pip install requirements.txt
bower update
```

Export the required settings
```
export APP_SETTINGS="config.DevelopmentConfig"
export DATABSE_URL="postgresql://<user_name>@localhost/<database_name>"
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