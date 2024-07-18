help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@grep '^[a-zA-Z]' ${MAKEFILE_LIST} | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

up: ## docker compose build and up
	docker-compose up --build -d

logs: ## app logs
	docker logs --follow --timestamps app

db_logs: ## db logs
	docker logs --follow --timestamps postgres

exec: ## exec to app container
	docker exec -it app bash

lint: ## lint the code with black
	black exclude=venv,env,docs,migrations . --check

update-requirements: ## update requirements.txt
	poetry export -f requirements.txt --output requirements.txt --without-hashes