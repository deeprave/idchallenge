# .id Challenge

https://github.com/dotidconsulting/coding-challenge-location-decisions

## Setup

1. create a .env - see following section
2. `cd ./backend && ./manage.py migrate`
3. `./manage.py createsuperuser --username admin --email admin@example.com`


### .env configuration

This is a 12-factor app, configured using a .env file.

A minimal version is as follows:
```dotenv
# django
DJANGO_DEBUG=true

# database
SA_DATABASE_URL=${DBTYPE}://${SAUSER}:${SAPASS}@${DBHOST}/${SANAME}
DATABASE_URL=${DBTYPE}://${DBUSER}:${DBPASS}@${DBHOST}/${DBNAME}
```
Substitue values in the above lines with literals or prefix these lines with (e.g.):
```dotenv
DBTYPE=postgresql
DBHOST=localhost:5432

SANAME=postgres
SAUSER=postgres
SAPASS=<postgres password>

DBNAME=idchallenge
DBROLE=idchallenge
DBUSER=challenge
DBPASS=<challenge password>
```
Note that the database needs to exist prior running up the application.
