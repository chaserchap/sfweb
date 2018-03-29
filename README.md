# sfweb

## Required Software
postgres
python 2.7

## Required Libraries
Django

## Setting up to run
Once you have a postgres instance installed ensure you have a database created named `sfweb`.
Restore the database provided in the repo to this database. This can be pretty easily done with pgadmin4.

## Running the Site
In the main repo folder (should be sfweb) run: `python manage.py runserver`.
Navigate to `localhost:8000` from any browser.
