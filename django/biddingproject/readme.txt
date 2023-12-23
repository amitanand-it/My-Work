python -m venv django-env
source django-env/bin/activate
pip install django
python -m django --version
django-admin startproject mysite

python manage.py runserver 0:8000
In ALLOWED_HOSTS enter '*' for all

python manage.py startapp polls
polls
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

pip install psycopg2
In settings use django.db.backends.postgresql_psycopg2
'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'tradein_clients',
    'USER': 'tradein_dev',
}

python manage.py dbshell
Adding model to INSTALLED_APPS of settings 
python manage.py makemigrations
python manage.py migrate
python manage.py sqlmigrate polls 0001 > polls_app.sql

createsuperuser
python manage.py createsuperuser

from .models import Question
admin.site.register(Question)

