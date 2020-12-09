# Headlines Watcher API

Consumes an API providing news headlines and serves the headline details.

## Set-up

### Install dependencies

Be aware that dependencies installed this way may interfere with the ones already or to be installed on your system.
Using a virtual environment or docker is advised to avoid such conflicts.

```
pip install -r requirements.txt
```

### with docker

Full set-up is provided with Docker, docker-compose.
You may need the official [Docker](https://docs.docker.com/get-docker/) and [Docker-Compose](https://docs.docker.com/compose/install/) doc for installation guidelines.

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

## Configuration

Generate your own API key:

```
https://newsapi.org/
```

Place it in the `.env_example` and rename it to `.env`.

There, you may also configure parameters to override their default values:

- refresh rate: time waited between headlines updates, in seconds
- debug: if True, the server will run in debug mode and log level will be set to DEBUG
- country: two-letter country code which news to target (ex: "CA", "FR"...)
- exp_time: time after which headlines expired and removed from the database, in seconds

## Usage

### In a shell

```
# Run the client
python client.py

# Run the api
python api.py

# Run both simultaneously:
python main.py
```

### With docker

```
# Launch api and client services
# Rebuilds if necessary
docker-compose up --build

# Restart api
docker-compose restart api

# Restart client
docker-compose restart client
```

Point your browser to `http://localhost:5000/ui` for more details on the API.

## API

### Endpoints

Once the api is running, you can access the doc by pointing the browser to to http://localhost:5000/ui/.

`/`: Get all stored headlines

```
# Example
curl http://localhost:5000/
```

`/{id}`: Get specific headline

```
# Example
curl http://localhost:5000/283856036047863831589562360520055251764
```

## For developers

Install dev packages

```
pip install -r requirements.txt -r requirements-dev.txt

# Or with a virtual env
pipenv install
```

You will also have access to pre-commit hooks for format and style checking:

```
# Run pre-commit checks without committing
pre-commit run

# Bypass pre-commit check
git commit "foo" --no-verify
```
