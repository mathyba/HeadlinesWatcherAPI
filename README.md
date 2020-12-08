# French Government Dataset Browser

Consumes the French Governement's datasets at regular interval and provides an id endpoint to fetch target information.

## Set-up

Install dependencies
```
pip install -r requirements.txt
```
Be aware that dependencies installed this way may interfere with the ones already or to be installed on your system.
Using a virtual environment is advised to avoid such conflicts.

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

# TODO
[] Dockerize development environment

## For developers

Install dev packages
```
pip install -r requirements.txt requirements-dev.txt

# Or with a virtual env
pipenv install
```
