build:
	docker build -t flask-bootstrap:local .

up: build
	docker-compose up --force-recreate