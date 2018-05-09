# <center> Django 命令
###1、Creating a project
    $ django-admin startproject myproject
###2、The development server
    $ cd myproject
    $ python manage.py runserver 8080
###3、Creating the Polls app
    $ python manage.py startapp polls app
###4、create the tables in database
    $ python manage.py migrate
###5、create module   
    define a module on polls/models.py
    Edit the myproject/settins.py file and add that dotted paht to INSTALLED_APPS
    run the command to tell Django that you have get a new app or you have make some changes to you models and create migration for those changes.
    $ python manage.py makemigrations polls
    
    The sqlmigrate command takes migration names and returns their SQL:
    $ python manage.py sqlmigrate polls 0001
    
    run migrate again to create those model tables in database and  apply those changes to the database.
    $ python manage.py migrate
    