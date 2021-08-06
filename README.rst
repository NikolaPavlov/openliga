TODO:
-----

* better search for team  (Elastic Search)
* caching  api requests
* pagination in the index.html
* minify static (django-compressor)
* move django settings to .env file (separate production and dev settings)
* deploy to Vagran Target with Ansible
* add tests

Stack
-----
* poetry         (for virtualenv)
* django
* requests       (for hitting the API)
* docker_compose (for building in containers)

How to run
----------

master branch
=============

* ``poetry install --no-dev``         -->     install the dependancies
* ``poetry shell``                    -->     activating the env
* ``python manage.py runserver``      -->     run dev server localhost:8000

* to change the season from the default (2021) --> ``website.settings.SEASON``

docker_compose branch
=====================

* switch to docker_compose branch and read README

* My knowledge of Ansible+Vagrant currently is pretty rusty so I decide to show up somethin with docker_compose
* ``gunicorn`` --> ( for Server )
* ``nginx``    --> (reverse proxy, serving the static files)

