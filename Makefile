build:
	docker build -t flask-bootstrap:local .

up: build
	docker-compose up --force-recreate

bash: up
	docker-compose exec -it app bash

psql: up
	docker-compose exec -it db psql -U example -d example

migrate:
	docker-compose exec -it app alembic upgrade head

new-migration:
	docker-compose exec -it app alembic revision -m $(shell bash -c 'read -p "Enter migration name: " name; echo $$name')

tests-e2e: up
	docker-compose exec -it app bash bin/test_e2e.sh