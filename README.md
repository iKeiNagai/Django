Horticulture app - application that assists with the organization and execution of flower competitions

install:
- pip install django 
- pip install mysqlclient
- pip install django-filter
- pip install fuzzywuzzy

to run:
- cd dbproject
- python manage.py makemigrations
- python manage.py migrate (if managed on)
- python manage.py runserver 
- python manage.py inspectdb > models.py (create file for db tables)