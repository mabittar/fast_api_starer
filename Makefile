SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
PROJECT=FastAPI_starer
OS = $(shell uname -s)

# Print usage of main targets when user types "make" or "make help"
.PHONY: help
help:
	echo "Please choose one of the following targets:"\
	      "    setup: Setup your development environment and install dependencies\n"\
	      "    run: Run app"\
		  "	   reload: Run app using reload mode"
		  "	   lint: Lint file"\
	      "    compose: Activate docker compose"\
	      "    compose-up: Docker-up"\
	      "    compose-build: Docker build App Image"\
	      ""\
	      "View the Makefile for more documentation about all of the available commands"
	@exit 2

.PHONY: setup
setup: venv requirements-dev.txt
	(\
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Start LOCAL environment"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
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
run:
	( \
		source venv/bin/activate; \
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Runinng APP"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		. app/app.sh; \
	)

.PHONY: reload
reload:
	( \
		source venv/bin/activate; \
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Runinng APP"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		. app/app_reload.sh --reload; \
	)

.PHONY: lint
lint:
	( \
		source venv/bin/activate; \
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Linting APP"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		black --check .; \
		isort --recursive  --force-single-line-imports --line-width 88 --apply .; \
	)

.PHONY: compose
compose: compose-build
	clear; \
	echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	echo " Starting containerized environment"; \
	echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	docker -compose -f ./container/local.docker-compose.yml up; \

.PHONY: compose-up
compose-up: compose-build
	docker -compose -f container/local.docker-compose.yml up

.PHONY: compose-down
compose-down:
	docker -compose -f container/local.docker-compose.yml down

.PHONY: build
build:
	( \
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Building containers... "; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		docker -compose -f container/local.docker-compose.yml \
		build --parallel \
		--build-arg; \
	)

