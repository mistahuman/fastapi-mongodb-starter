.PHONY: help install dev test build run clean mongo mongo-stop

VENV     := .venv
PYTHON   := $(VENV)/bin/python
PIP      := $(VENV)/bin/pip
UVICORN  := $(VENV)/bin/uvicorn
PYTEST   := $(VENV)/bin/pytest
APP_NAME        := fastapi-mongodb-starter
PORT            := 8000
MONGO_CONTAINER := mongo-dev
MONGO_PORT      := 27017

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

install: ## Create virtualenv and install dependencies
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

dev: ## Run development server with auto-reload
	$(UVICORN) app.main:app --reload --host 0.0.0.0 --port $(PORT)

test: ## Run integration tests (requires running server)
	$(PYTEST) tests/

build: ## Build Docker image
	docker build -t $(APP_NAME) .

run: ## Run app via Docker
	docker run --env-file .env -p $(PORT):$(PORT) $(APP_NAME)

mongo: ## Start a local MongoDB container
	docker run -d --name $(MONGO_CONTAINER) -p $(MONGO_PORT):27017 mongo:8 \
		|| docker start $(MONGO_CONTAINER)

mongo-stop: ## Stop the local MongoDB container
	docker stop $(MONGO_CONTAINER)

clean: ## Remove virtualenv
	rm -rf $(VENV)
