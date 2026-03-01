# Lab 6: Introduction to Django and Flask Web Frameworks

## Student Name

Yamini Parvathaneni

## Course

Software Architecture and Design – Fall 2025


# Overview

This lab demonstrates basic web application development using two Python web frameworks:

* Flask (lightweight framework)
* Django (full-featured framework)

The lab includes routing, templates, dynamic URLs, form handling, models, and admin panel usage.


# Part 1: Flask Application

## Features Implemented

* Home route (`/`) displaying "Welcome to Flask!"
* Dynamic route (`/hello/<name>`) displaying personalized greeting
* HTML template using Jinja2 (`hello.html`)
* Form page (`/form`) to enter user name
* Form submission handled using POST method
* Redirect to greeting page after form submission


## Flask Project Structure

```
flask_app/
│
├── venv/
├── app.py
└── templates/
    ├── hello.html
    └── form.html
```


## How to Run Flask Application

Open terminal and run:

```
cd flask_app
venv\Scripts\activate
python app.py
```

Open browser:

```
http://127.0.0.1:5000/
```

Test routes:

```
http://127.0.0.1:5000/
http://127.0.0.1:5000/form
http://127.0.0.1:5000/hello/Yamini
```

# Part 2: Django Application

## Features Implemented

* Homepage (`/`) displaying "Hello from Django!"
* Dynamic greeting route (`/greet/<name>/`)
* Templates using Django template system
* Message model with text field
* Admin panel for managing Message objects
* View to display all messages (`/messages/`)

## Django Project Structure

```
django_app/
│
├── venv/
└── myproject/
    │
    ├── manage.py
    │
    ├── myproject/
    │   ├── settings.py
    │   ├── urls.py
    │
    └── myapp/
        ├── models.py
        ├── views.py
        ├── admin.py
        ├── urls.py
        └── templates/
            ├── home.html
            ├── greet.html
            └── messages.html
```

## How to Run Django Application

Open terminal and run:

```
cd django_app\myproject
venv\Scripts\activate
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

Test routes:

```
http://127.0.0.1:8000/
http://127.0.0.1:8000/greet/Yamini/
http://127.0.0.1:8000/messages/
http://127.0.0.1:8000/admin/
```

## Admin Panel

Steps:

1. Open:

```
http://127.0.0.1:8000/admin/
```

2. Login using superuser credentials

3. Add Message objects

4. View messages at:

```
http://127.0.0.1:8000/messages/
```

# Summary of Implementation

Flask:

* Created routes using Flask decorators
* Used Jinja2 templates
* Implemented form handling
* Displayed dynamic greeting

Django:

* Created project (myproject) and app (myapp)
* Implemented views and URL routing
* Created Message model
* Used Django admin panel
* Displayed database content using templates

# Screenshots Included (submitted on Blackboard)

* Flask home page
* Flask form and greeting page
* Django homepage
* Django admin panel
* Django message list page

# GitHub Repository

Repository contains:

* flask_app folder
* django_app folder
* README.md