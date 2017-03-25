
[![Coverage Status](https://coveralls.io/repos/github/sdoro/django-migration/badge.svg?branch=master)](https://coveralls.io/github/sdoro/django-migration?branch=master)

# testing makemigrations and migrate

### 01. create & setup virtualenv

    echo "*.py[cod]" > .gitignore
    sudo pip install virtualenv
    echo "Django==1.10.6" > requirements.txt
    virtualenv $HOME/10.6
    source $HOME/10.6/bin/activate
    pip install -r requirements.txt

### 02. make project and app

    django-admin startproject liveactiondb
    cd liveactiondb
    ./manage.py startapp shows

### 03. using Travis CI to run an elementary test

    # edit shows/tests.py
    > ../.travis.yml
    # edit ../.travis.yml

### 04. makemigrations

    # edit liveactiondb/settings.py
    # edit shows/models.py (add Show)
    ./manage.py makemigrations
    ./manage.py migrate shows
    # edit shows/models.py (add Episode)
    ./manage.py makemigrations
    ./manage.py migrate shows

### 05. add db testing

    # edit shows/tests.py
    ./manage.py test shows
