# polls

# Documentation
https://pollsapi351.docs.apiary.io/

# Installion Guide

### Initialize project
#### Open CMD/Terminal
* mkdir polls_project
* cd polls_project
* git clone https://github.com/Costigun/polls.git
### Create Virtual Environment
* python3 -m venv myvenv
### Install lib-s
#### For Windows
* myvenv\Scripts\activate
* pip install requirements.txt
#### For Linux/MacOS
* source myvenv/bin/activate
* pip install requirements.txt
### Work with PostgreSQL
* sudo -u postgres psql
* CREATE DATABASE polls;
* CREATE USER polls_user WITH PASSWORD 'deathless0419';
* GRANT ALL PRIVILEGES ON DATABASE polls TO polls_user;
* ALTER ROLE polls_user WITH SUPERUSER;
* \q
### Work on project
##### Open directory where "manage.py" file
###### Do migrations
* python3 manage.py makemigrations
* python3 manage.py migrate
###### Create superuser for admin panel
* python3 manage.py createsuperuser
###### Run project
* python3 manage.py runserver


