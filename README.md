# django
pip install django
pip install pymysql

trong file setting:

import pymysql
pymysql.install_as_MySQLdb()


# install project
 django-admin startproject demo

# start project: cd toi root project
python manage.py migrate 
python manage.py runserver 8888

# create new app
django-admin startapp home

# install mysql on win
pip install mysql

# install mysqlclient
pip install mysqlclient

# Tao tk admin
window:
winpty python manage.py createsuperuser

python manage.py createsuperuser

# thay doi file trong setting
python manage.py makemigrations
python manage.py migrate

