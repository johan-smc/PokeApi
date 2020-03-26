# PokeApi

A Pokemon is a mystical creature that belongs to a fictional world, designed
and managed by the Japanese companies Nintendo, Game Freak and
Creatures. The Pokemon world is available on manga, anime adaptions, games,
retail stores and many more places.
The depth of this virtual world allows to have mountains of data only to describe
completely a Pokemon and its relations around the universe. This information is
available on the [Poke api](https://pokeapi.co/docs/v2.html).

## Table of contents

- [Contributors](#contributors)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Django](#Running-the-Django)
- [Tasks](#tasks)


## Contributors
| Name                       | GitHub                                | 
| -------------------------- | ------------------------------------- | 
| Johan Sebastian Murillo | [johan-smc](https://github.com/johan-smc) | 

## Prerequisites

We recommend work on Linux or on a Unix system.
In this project all examples will be in mac os.

### Python

You must have `python 3` on your computer.

### Pyenv

You must have `pyenv` on your computer, for python environment configuration.

### Direnv

You must have `direnv` on your computer, for environment var for django configuration.

## Installation
### Clone the repository

```shell
$ git clone https://github.com/johan-smc/PokeApi
$ cd PokeApi
```

### Install the requirements

Install the requirements in `requirements/development.txt`

```shell
$ pip install -r requirements/development.txt
```

### Create environment file 

Create in folder root `.envrc` and add all the database information needed.
After the add the file run the next command to export the vars.

```shell
$ direnv allow
```

## Running the Django

```shell
$ cd poke_api
$ python manage.py migrate --settings=poke_api.settings.development
$ python manage.py runserver --settings=poke_api.settings.development
```


## Tasks

### Evolution Chains

For fetch all the information for an evolution chain you need to run the next command whit an `id` param:

```shell
$ python manage.py fetch_evolution_chain --settings=poke_api.settings.development {$id}
```

### Get a pokemon

You need to run django with `runserver` and the url for the request is `/api/pokemon/{name}`

### Running the Django test

All function in services files has tests cases for run them the command is:

```shell
$ python manage.py test --settings=poke_api.settings.development
``` 