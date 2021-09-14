TASK
----

As an enduser I want to have a small website, which displays various data of Bundesliga games 
using the JSON/XML API http://www.openligadb.de/
(see https://bitbucket.org/anythingabout/openligadb-samples/overview/ ).
Provide the following Information:
* Next upcoming matches (following Gameday)
* All matches of the actual season
* Win/Loss Ratio of the actual season of each team
* Optimized for different resolutions through a type and layout of your choice
Bonus-Points:
* A search functionality for a specific team displaying all the information above
* Automated deployment script with fabric/ansible or the like. If you do so, deployment 
Target should be a local Vagrantbox.
* Minify used Scripts/CSS automatically
* etc. pp.

Please describe why you choose which technology (Framework, Language, SOAP/JSON), and 
provide a description of your Workflow to solve this problem.

A link to a repository with a small Readme.md for setup is needed.

You may use a persistence layer of your choice if you feel the need to (mongoDB, mySQL p.e)
The actual UI of the Site is totally up to you, functionality and proper design of the application 
should be your focus.

SOLUTION
--------
working time: ~14hours for 7days


TODO:
=====

* better search for team  (Elastic Search)
* caching  api requests
* pagination in the index.html
* minify static (django-compressor)
* move django settings to .env file (separate production and dev settings)
* deploy to Vagran Target with Ansible
* add tests

Stack
=====
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

