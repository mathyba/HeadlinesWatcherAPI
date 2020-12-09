# Headlines Watcher API

Consumes an API providing news headlines and serves the headline details.

## Set-up

### Install dependencies

Be aware that dependencies installed this way may interfere with the ones already or to be installed on your system.
Using a virtual environment or docker is advised to avoid such conflicts.

```
pip install -r requirements.txt
```

### With docker

Full set-up is provided with Docker, docker-compose and Makefile.
If you don't have Docker and docker-compose, check out the official [Docker](https://docs.docker.com/get-docker/) and [Docker-Compose](https://docs.docker.com/compose/install/) doc and follow the guidelines for your distribution.

### With a virtual env

Example with pipenv

```
# Install dependencies
pipenv install

# Open a shell in the virtual env
pipenv shell
```

#### Possible issues

You may find that python is unable to import some packages installed.
If so, provide pipenv with a PYTHONPATH:

- find the location of the package:

```
# Inside the venv shell
pip show <package-raising-the-error>
```

- define the PYTHONPATH in the .env:

```
echo "PYTHONPATH='path-to-the-package' >> .env
```

## Usage

### In a shell

```
# Run client
python client.py
```

## With docker

```
# Launch api and client services
# Rebuilds if necessary
docker-compose up --build

# Restart api
docker-compose restart api

# Restart client
docker-compose client
```

Point your browser to `http://localhost:5000/ui` for more details on the API.

## For developers

Install dev packages

```
pip install -r requirements.txt requirements-dev.txt

# Or with a virtual env
pipenv install
```

You will also have access to pre-commit hooks:

```
# Run pre-commit checks without committing
pre-commit run

# Bypass pre-commit check
git commit "foo" --no-verify
```
