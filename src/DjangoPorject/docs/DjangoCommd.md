# <center> Django 命令
### 1、Creating a project
    $ django-admin startproject myproject
### 2、The development server
    $ cd myproject
    $ python manage.py runserver 8080
### 3、Creating the Polls app
    $ python manage.py startapp polls app
### 4、create the tables in database
    $ python manage.py migrate
### 5、create modle   
    define a module on polls/models.py
    Edit the myproject/settins.py file and add that dotted paht to INSTALLED_APPS
    run the command to tell Django that you have get a new app or you have make some changes to you models and create migration for those changes.
    $ python manage.py makemigrations polls
    
    The sqlmigrate command takes migration names and returns their SQL:
    $ python manage.py sqlmigrate polls 0001
    
    run migrate again to create those model tables in database and  apply those changes to the database.
    $ python manage.py migrate
### 6、create an admin user
    $ python manage.py createsuperuser
### 7、creating an admin user
    create a user
    $ python manage.py createsuperuser
    Enter the username and password, then you can vist admin and edit models.
### 8、template
    we can put the templates on app subdirectory,like this:
    /polls/templates/polls/index.html
    and we can loads the templates by use render from views.py.
### 9、Raising a 404 error
    from django.http import Http404
    raise Http404("Input you notes")
    we can use get_object_or_404 function  to take a Django models as its first argument and an arbitrary number of keyword which it passes to the get() function of the model's manager.
    from django.shorcuts import get_object_or_404
    get_object_or_404(Question, pk = question_id)

