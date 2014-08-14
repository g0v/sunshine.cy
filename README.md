cy 
================

[金錢報](http://sunshine.cy.g0v.tw/)        
[Hackpad 意見回饋](https://g0v.hackpad.com/--TrxSlBQ4MyI)

In Ubuntu 12.04 LTS
=================

## For Crawler (Scrapy 0.24.4)

[Scrapy offcial install doc](http://doc.scrapy.org/en/latest/intro/install.html)
```
apt-get install libxml2-dev libxslt1-dev python-dev libffi-dev
pip install lxml
pip install Scrapy
```


## For Website (Python/Django)

0.1 install basic tools
```
sudo apt-get update
sudo apt-get upgrade
sudo reboot
sudo apt-get install git python-pip python-dev python-setuptools postgresql libpq-dev
easy_install virtualenv
```

0.2 set a password in your database(If you already have one, just skip this step)        
(you can use `whoami` to check your username, notice **&lt;username&gt;**  below, please replace with your own)

```
sudo -u <username> psql -c "ALTER USER <username> with encrypted PASSWORD 'put_your_password_here';"
```

## Clone source code from GitHub to local
```
git clone git@github.com:thewayiam/cy.git       
cd cy/website/cy/
```

## Start virtualenv and install packages         
(if you don' mind packages installed into your local environment, just `pip install -r requirements.txt`)
```
virtualenv --no-site-packages venv      
source venv/bin/activate        
pip install -r requirements.txt     
```

## Restore data into database       
Please new a database(eg. cy), below will use cy for example
```
createdb -h localhost -U <username> cy
pg_restore --verbose --clean --no-acl --no-owner -h localhost -U <username> -d cy local_db.dump
```

## Django settings.py          
create and edit local_settings.py in cy/website/cy/cy/ to configing your database parameter(notice **USER**, **PASSWORD** below) and **SECRET_KEY**
See [Django tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/) or maybe use [online generator](http://www.miniwebtool.com/django-secret-key-generator/) to get SECRET_KEY for convenience				
```
SECRET_KEY = '' # put random string inside and don't share it with anybody.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cy', # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}
```
Because local_settings.py is list in .gitignore, so this file won't be appear in source control, for safety.

## runserver
```
python manage.py runserver
```

CC0 1.0 Universal
=================
CC0 1.0 Universal       
This work is published from Taiwan.     
