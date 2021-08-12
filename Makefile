SHELL := /bin/bash
PROJECT=FastAPI_starer
OS = $(shell uname -s)

# Print usage of main targets when user types "make" or "make help"
.PHONY: help
help:
	echo "Please choose one of the following targets: \n"\
	      "    setup: Setup your development environment and install dependencies\n"\
	      "    run: Run app\n"\
	      "    compose: Activate docker compose\n"\
	      "    compose-up: Docker-up\n"\
	      "    compose-build: Docker build App Image\n"\
	      "\n"\
	      "View the Makefile for more documentation about all of the available commands"
	@exit 2

.PHONY: setup
setup: venv requirements-dev.txt
	(\
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Start DEV environment"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Update pyenv and set local python version"; \
		pyenv update; \
		pyenv install -s 3.9.2; \
		pyenv local 3.9.2; \
		echo " Check if virtual environment exists or initiate"; \
		if [ -d ./venv ]; \
		then \
		echo "virtual environment already exists skip initiation"; \
		else \
		@echo "virtual environment does not exist start creation" \
		python -m venv venv; \
		fi; \
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Start virtual environment"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		source venv/bin/activate; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Install requirements"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		pip install -r requirements-dev.txt; \
	)

.PHONY: run
run: venv requirements.txt
	( \
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Runinng APP"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		. venv/bin/activate; \
		clear ;\
		. app/app.sh --reload; \
	)

.PHONY: compose
compose: compose-build
	clear; \
	echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	echo " Starting containerized environment"; \
	echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	docker-compose -f container/local.docker-compose.yml up

.PHONY: compose-up
compose-up: compose-build
	docker-compose -f container/local.docker-compose.yml up

.PHONY: compose-down
compose-down:
	docker-compose -f container/local.docker-compose.yml down

.PHONY: compose-build
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
