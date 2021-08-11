SHELL := /bin/bash
PROJECT=FastAPI_starer

startenv: venv requirements-dev.txt
(\
	clear; \
	@echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	@echo " Start DEV environment"; \
	@echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	@echo " Check if virtual environment exists or initiate"; \
	if [-d "venv"]; then \
		@echo "virtual environment already exists skip initiation"; \
	else; \
		. python -m venv venv; \
	fi 
	clear; \
	@echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	@echo " Start virtual environment"; \
	@echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	. venv/bin/activate; \
	@echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	@echo " Install requirements"; \
	@echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	pip install -r requirements-test.txt; \
)

compose: compose-build
	clear; \
	@echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	@echo " Starting containerized environment"; \
	@echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	docker-compose -f container/local.docker-compose.yml up


compose-up: compose-build
	docker-compose -f container/local.docker-compose.yml up
''
compose-down:
	docker-compose -f container/local.docker-compose.yml down

compose-build:
	( \
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Building containers... "; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		docker-compose -f container/local.docker-compose.yml \
		build --parallel \
		--build-arg  COMMIT=$$(git rev-parse HEAD) \
	)

run: venv requirements.txt
	( \
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Runinng APP"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		. venv/bin/activate; \
		pip install -r requirements.txt; \
		clear ;\
		.app.sh; \