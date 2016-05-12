PROJECT_NAME = "wall-server"
DB_NAME = "wall"
TEST_DB_NAME_1C = "test_sl1c"

APPS = "_auth" "blog" "common" "shop"

default: _requirements _settings dropdb createdb syncdb migrate loaddata collect_static end

_settings:
	@echo "Emitting local development settings module"
	@cp settings/local.py.example settings/local.py

_requirements:
	@echo "Installing requirements"
	@pip install --exists-action=s -r requirements/dev.txt

req: _requirements

db: dropdb createdb syncdb migrate loaddata

createdb:
	@echo "Creating MySQL database $(DB_NAME)"
	@mysql -uroot -e "create database if not exists $(DB_NAME) character set utf8 collate utf8_general_ci;"

dropdb:
	@echo "Destroying MySQL database $(DB_NAME)"
	@mysql -uroot -e "drop database if exists $(DB_NAME);"

migrate:
	@echo "Running migrations"
	@python manage.py migrate -v 0

syncdb:
	@echo "Syncing database and loading initial fixtures"
	@python manage.py syncdb --database=default --noinput -v 0

loaddata:
	@echo "Loading additional data fixtures"
	@python manage.py filldb

run:
	@python run.py

runpub:
	@python run.py --host=0.0.0.0

test:
	@python manage.py test $(APPS)

shell:
	@python manage.py shell

end:
	@echo "You can now run development server using 'make run' command"

clean:
	@echo "Cleaning *.pyc files"
	@find . -name "*.pyc" -exec rm -f {} \;

flush:
	@echo "Flushing redis"
	@redis-cli FLUSHALL

collect_static:
	python manage.py collectstatic -l --noinput

compilemessages:
	python manage.py compilemessages

makemessages:
	python manage.py makemessages -a

#this activation works but (env) prefix not added. Not working in a simple way because
#When you source, you're loading the activate script into your active shell.

#When you do it in a script, you load it into that shell which exits when your script
#finishes and you're back to your original, unactivated shell.
#http://stackoverflow.com/questions/13122137/how-to-source-virtualenv-activate-in-a-bash-script
activate:
	./activate.sh

# daemonized version
# celery multi start worker2 -A apps.common -Q low
celery_low_start:
	celery -A apps.common worker -l info -Q low

celery_start:
	celery -A apps.common worker -l info

celeryd_start:
	celery -A apps.common worker -l info -Q default

flower:
	flower -A apps.common --port=5555

cache_update:
	@python manage.py cache_update