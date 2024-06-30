build:
	docker build -t flask-bootstrap:local .

up: build
	docker-compose up --force-recreate

bash:
	docker-compose exec -it app bash

psql:
	docker-compose exec -it db psql -U example -d example