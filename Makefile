##
# Local
#
# @file
# @version 0.1

# end
create-env:
	python3 -m venv .venv
	source ./venv/bin/activate
	pip install -r requirements.txt

make-migrate-run:
	python3 manage.py makemigrations
	python3 manage.py migrate
	sqlite3 db.sqlite3 < rooms.sql
	python3 manage.py runserver

delete-migrations:
	rm clients/migrations/0001_initial.py
	rm reserves/migrations/0001_initial.py
	rm rooms/migrations/0001_initial.py
	rm bill/migrations/000*
	rm db.sqlite3
