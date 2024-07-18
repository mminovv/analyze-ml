## Table of Contents

* [Setup](#setup)
* [Setup on a local machine with Docker and Docker Compose](#setup-on-a-local-machine-with-docker-and-docker-compose)
* [Installing on a local machine with venv](#installing-on-a-local-machine-with-venv)
* [App testing](#app-testing)
* [Linting & Formatting](#linting-and-formatting)

## Setup
Configuration is stored in `.env`, for examples see `.env.examples`

Create environment file `.env`:
```sh
cp .env.example .env
```
* This project requires python3.11 and postgres.
* Install [docker](https://www.docker.com/get-started) and [docker-compose](https://docs.docker.com/compose/)

## Setup on a local machine with Docker and Docker Compose

See all commands:
```sh
make help
```

Up project with `Docker`:
```sh
make up
```

See make configuration on Makefile


## Installing on a local machine with venv
* Create and activate your virtual environment
* Install requirements

Install requirements:

```sh
python3 -m venv venv
source venv/bin/activate # unix system
pip install -r requirements.txt
```

```sh
alembic upgrade head
```
Development servers:

```bash
# run dev server
uvicorn src.asgi:app --reload --host 0.0.0.0 --port 8000 --log-level debug --reload
```
### App testing

Add user with balance 100.00 to the database:
```bash
make create-user
```

Check documentation in [swagger](http://127.0.0.1:8000/docs)


## Linting and Formatting

Linting completed with flake8
```bash
flake8 --ignore=E501 --exclude=venv,docs .
```

Formatting completed with black
```bash
black exclude=venv,env,docs,migrations .
```
