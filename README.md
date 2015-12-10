# Digital Football

## Local development
### Install Postgres

    brew install postgres
    
Then start it with:
 
    pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start

Then add DB:

    psql -d template1
    template1=# CREATE USER digifoot WITH PASSWORD 'digifoot';
    template1=# CREATE DATABASE digifoot;
    template1=# GRANT ALL PRIVILEGES ON DATABASE digifoot to digifoot;
    template1=# ALTER USER digifoot CREATEDB;
    
### Bootstrap 

    virtualenv ve -p /usr/bin/python
    ve/bin/pip install -r requirements.txt
    ve/bin/python manage.py migrate
    
    
### Run Django

    ve/bin/python manage.py runserver
    
    
## HEROKU

### Deploy deploy
    
    heroku create

### Deploy

    git push heroku master
    
### Run database migrations

    heroku run python manage.py migrate
    
    
## Troubleshooting 
    
### Fix kernel memory errors when running postgres

    sudo sysctl -w kern.sysv.shmmin=1
    sudo sysctl -w kern.sysv.shmall=1079204
    sudo sysctl -w kern.sysv.shmmax=4420419584
    
    
    
    
# CREDITS

Project developed by [Hern.as](https://hern.as) and [Hackevents.co](http://hackevents.co).

People involved in project:
 
- Bartosz Hernas
- Christian Strobl
- Marc Seitz
- Michał Hernas