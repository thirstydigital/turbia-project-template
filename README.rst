How to Use
==========

This is a turbia project template, for use with the `startproject` management
command. Create a new skeleton project like this:

1.  Create skeleton project::

        $ cd ~/projects
        $ django-admin.py startproject -e bat,development,ini,production,py,rst,staging -n Makefile \
        --template https://github.com/thirstydigital/turbia-project-template/archive/master.zip $PROJECT

2.  Update this ``README.rst`` file. Remove the ``How to Use`` section and
    update the ``Overview`` section.

3.  Create a private repository on BitBucket (use SourceTree) and push an
    initial commit.


Overview
========

Description of project.


Installation
------------

You will need Git, Python 2.6.5+ or 3.2+, ``pip``, ``virtualenv`` and
``virtualenvwrapper`` to install this project and its dependencies.

Clone project in your ``projects`` folder::

    $ cd ~/projects
    $ git clone git@bitbucket.org:thirstydigital/{{ project_name }}.git

Create ``virtualenv`` and install dependencies::

    $ cd {{ project_name }}
    $ mkvirtualenv --distribute --no-site-packages -a "$PWD" -r requirements.txt {{ project_name }}

If you are going to use PostgreSQL, install ``psycopg2``::

    $ pip install psycopg2

If you are going to use the interactive shell, install ``ipython``::

    $ pip install ipython

If you are going to use the python debugger, install ``ipdb``::

    $ pip install ipdb

Configure settings for the local environment::

    $ cp {{ project_name }}conf/settings.py.development {{ project_name }}settings.py
    $ vi {{ project_name }}settings.py

If you are deploying to a staging or production environment, copy the staging
or production settings instead.

Sync database and populate with initial data::

    $ ./manage.py syncdb --migrate
    $ ./manage.py turbia_initial_data

Update static files and flush cached static pages::

    $ ./manage.py collectstatic
    $ ./manage.py pages_flush


Working with your project
-------------------------

Activate ``virtualenv`` and change to project directory::

    $ workon {{ project_name }}

Run development server::

    $ ./manage.py runserver

Run interactive shell::

    $ ./manage.py shell

Deactivate ``virtualenv``::

    $ deactivate
