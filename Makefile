run:
	uvicorn app.main:app --reload

worker:
	python -m app.workers.run_worker

docker-up:
	docker compose up --build

docker-down:
	docker compose down
