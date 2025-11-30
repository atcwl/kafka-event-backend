.PHONY: run build worker

run:
	docker compose -f docker-compose.yml up --build

worker:
	python workers/run_worker.py

build:
	docker compose -f docker-compose.yml build