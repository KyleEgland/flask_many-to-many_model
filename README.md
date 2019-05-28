# Flask Many-to-Many Model
This repository exists for my own reference in future projects.  Please use it if you find it useful!

## Synopsis
There seems to always be some data structure that needs reference in or to another data structure.  This is a many-to-many relationship which is certainly achievable within the Flask web framework.  This repository demonstrates a simple many-to-many relationship using SQLAlchemy and Flask under the guise of users and channels (with users subscribing to channels and channels having subscribers).

## Virtualenv
This project was created using Python 3.x (3.7.3 at the time of writing) with the virtualenv module.  To run this project in your own virtual environment:

1) Install the virtualenv module

    `C:\Users\<username>\<repo>\flask_many-to-many_model> python -m pip install virtualenv`

2) Create a virtual environment in the project directory

    `C:\Users\<username>\<repo>\flask_many-to-many_model> python -m virtualenv .`

3) Activate the virtual environment

    * Windows:

    `C:\Users\<username>\<repo>\flask_many-to-many_model> .\Scripts\activate`

    * Linux

    `user@machine /<repo>/flask_many-to-many_model$ source bin/activate`

4) Install dependencies

    `(flask_many-to-many_model) C:\Users\<username>\<repo>\flask_many-to-many_model> python -m pip install -r requirements.txt`

## About Flask and Databases
The goal of this project is not to familiarize you (the consumer of it) with how data models and databases work with Flask, but rather how a specific relationship within that paradigm works.  Should you require a primer, please refer to the Flask Mega-Tutorial created by Miguel Grinberg (link in Credits section) in order to begin that journey.

Additionally, this project utilizes the Flask-Migrate module to manage the database and its structure.  There will be a migrations directory with at least one migration made. Simply apply the latest migrations:

    `(flask_many-to-many_model) C:\Users\<username>\<repo>\flask_many-to-many_model> flask db upgrade`

Create the database:

    `(flask_many-to-many_model) C:\Users\<username>\<repo>\flask_many-to-many_model> flask shell`

    `>>> db.create_all()`

Then the application may be run:

    `(flask_many-to-many_model) C:\Users\<username>\<repo>\flask_many-to-many_model> flask run`

## Environment File
This repository uses an environment file (.env) that must be created locally.  This file normally contains secrets, which is why it is not synced here.  Please find an example below:

```
FLASK_APP=flask_many_to_many.py
SECURITY_KEY=development
FLASK_ENV=development
# This is for linux
DATABASE_URL=sqlite:////home/<username>/<dir_to_repos>/flask_api_call_test/app.db
# This is for Windows
DATABASE_URL=sqlite:///C:/Users/<username>/<dir_to_repos>/flask_api_call_test/app.db
```

## Credits
Please reference the following resources to view the source(s) of this project.

* [Creating Many-To-Many Relationships in Flask-SQLAlchemy](https://youtu.be/OvhoYbjtiKc) YouTube video by [Pretty Printed](https://prettyprinted.com/)
* [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by [Miguel Grinberg](https://blog.miguelgrinberg.com/author/Miguel%20Grinberg)
* [Bootstrap](https://getbootstrap.com/)
