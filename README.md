# Baby Tools World

This repository contains the source code of the 'Baby Tools World' which is a simple full stack shop application written in Python using Django 6.
The project was developed for educational purposes only and therefore has no claim to feature completeness, or only minimal claims regarding application security, user experience, or design.

> [!NOTE]
> This project assumes you already know the python programming language

## Table of contents

* [Baby Tools World](#baby-tools-world)
  * [Prerequisites](#prerequisites)
  * [Quickstart](#quickstart)
  * [Project structure](#project-structure)
  * [Apps Overview](#apps-overview)
  * [Usage](#usage)
    * [Configuration](#configuration)
    * [Running the linting tools](#running-the-linting-tools)
    * [When to run this](#when-to-run-this)
    * [Testing](#testing)
    * [Running tests](#running-tests)
    * [Running with a WSGI Server](#running-with-a-wsgi-server)
    * [Seeding the application with data](#seeding-the-application-with-data)
  * [Containerization](#containerization)
    * [Build an image](#build-an-image)
    * [Run a container](#run-a-container)
    * [Commands in the Docker container](#commands-in-the-docker-container)

### Prerequisites

In order to seamlessly interact with the repository and the software it contains you need to following tools preinstalled:

* Python Interpreter
* OCI-Compliant Container Engine (e.g. podman, docker, etc.)
* Editor/IDE of your choice (VSC, PyCharm, etc.)

### Quickstart

In order to quickly get started with the project follow these steps:

* clone the repository
* nagivate to the repository
* (optional) create a virtual environment with `python -m venv my-venv`
  * activate the virtual environment:
    * on Windows run: `my-venv/Scripts/activate`
    * on MacOS/Linux run: `source my-venv/bin/activate`
* install the project dependencies with `pip install -r requirements.txt`
* configure required application environment variables
  * `cp example.env .env`
* go to the `src` directory via `cd src`
* prepare the database (create and apply migrations)
  * `python manage.py makemigrations`
  * `python manage.py migrate`
* start the application with `python manage.py runserver`
* verify the application is running by visiting `localhost:8000`
* (optional) create a superuser by running: `python manage.py createsuperuser`

### Project Structure

* `.gitlab`: GitLab specific project files
* `.github`: GitHub specific project files
* `src`: application source code, containing the django project, apps, and other files
* `requirements.txt`: the project dependencies

### Apps Overview

The project is modularized into several apps:

* `products`: Manages product listings and categories
* `users`: Handles user authentication and registration.

Each app has its own `models.py`, `views.py`, `urls.py`, and `admin.py` files to encapsulate its functionality.

### Usage

In this section you can read about the project a bit more in detail.

#### Configuration

To configure the project, follow these steps:

* Copy the example environment file to the `src` directory: `cp example.env src/.env`.
  * the file needs to be stored next to the manage.py file in order to function properly.
    Other locations might also work but there is no guarantuee, and in last consequence you will need to update to project correspondingly.
* Open your `src/.env` and set the required environment variables:
  * `ALLOWED_HOSTS`: provide a list of comma-separated values for the allowed host configuration => Defaults to `'localhost, 127.0.0.1, 0.0.0.0'`
  * `DEBUG`: Set to `True` for development or `False` for production. Defaults to `True`

#### Running the linting tools

> [!tip]
> In order to run the routines below the required packages must be installed (done after running `pip install -r requirements.txt`).
>
> If you are using a virtual environment this also needs to be activated.

To run code-quality checks that check the code-style and formatting you can run the following commands in your terminal:

```bash
# to format the python code
black .
# to apply correct sorting for imports
isort .
```

#### When to run this

You should check the code-style before pushing the commits to the remote repository.
In case you forgot it and somehow violated a rule, the CI workflow will fail -> run linting, add changes, commit, push -> see if pipeline passes

> [!note]
> If a CI workflow fails, you should check the logs to find out where the workflow failed and what was the reason for this failure.

#### Testing

This project contains tests for the corresponding apps in the respective packages.
Tests in Django can either be located in a `tests.py` file within a django-app, or you could also have a module named `tests` (essentially a folder with an `__init__.py` file).

> [!TIP]
> The django testrunner will by default discover tests by finding all python files that contain the word `test` in their name, e.g. `test.py`, `test_model.py`, or similar.

Example Structure:

```console
baby-tool-world/src/products
├───management
├───migrations
├───templates
└───tests <-- this is the module
      ├───__init__.py
      ├───test_category_model.py <-- this is a test file
      └───test_category_model.py <-- this is a test file too
```

#### Running tests

To run the tests with the `django testrunner` you can use the following command:

* `python manage.py test`, you need to run this in the folder where `manage.py` lives -> `src`

For more information about testing, refer to the testing documentation in this repository, see [testing documentation](./docs/testing.md)

#### Running with a WSGI Server

**WSGI** (Web Server Gateway Interface) is a specification that defines a standard interface between web servers and Python web applications or frameworks.
It acts as a bridge, allowing web servers to communicate with Python applications in a consistent manner.

In Django deployments, WSGI is used to serve the application in a production environment.
It enables the web server (e.g., Gunicorn, uWSGI, or Apache with mod_wsgi) to forward
requests to the Django application and return responses to the client. This ensures that
the application can handle HTTP requests efficiently and reliably in a scalable setup.

> `gunicorn` and `waitress` are similar tools and can be used for the same purpose,
> but sometimes running `gunicorn` on windows results in problems that can be circumvented by using `waitress` instead.
>
> See the following [quote](https://docs.gunicorn.org/en/stable/index.html) from the official gunicorn website:
>> Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX.

For more information about WSGI and its configuration, see the [wsgi documentation](./docs/wsgi.md).

#### Seeding the application with data

This section will guide you through the process of providing an initial seed to the application.

To initially seed the application you can run the management command `seed_db` to fill the database with some categories and testing products.

In order to run that comand go the the directory, where your `manage.py` file is stored and run the following command:

```bash
python manage.py seed_db
```

### Containerization

This section should give a brief overview about the containerization of the django app.

> [!NOTE]
> This guide assumes you are using the docker engine, docker desktop, or anything similar.
> For other tools that are compliant with the OCI spec the commands will be slightly different, but more or less the same.

#### Build an image

You can build the container image by running the following command in your terminal:

```bash
# use -t to provide a tag together with the image name
# -> baby-tools-world is the image name, 'local' is the tag
docker build -t baby-tools-world:local .
```

#### Run a container

> [!TIP]
> If you're using Windows, you'll probably have a problem with the file extension.
> Windows-based text editors put special characters at the end of lines to denote a line return or newline. Normally harmless,
> some applications on a Linux server can not understand these characters and can cause the service to not respond correctly.
>
> See this blog `https://blog.programster.org/fixing-docker-volume-windows-line-endings-on-bash-scripts`
> `https://docs.github.com/en/get-started/git-basics/configuring-git-to-handle-line-endings`

To start a container based on the image, use the following command in your terminal:

```bash
docker run --rm -it -p 8000:8000 baby-tools-world:local
```

In order to overwrite predefined environment configuration in the app, you can specify an `.env` file by adding the option to the command like below:

```bash
docker run --rm -it -p 8000:8000 --env-file .env baby-tools-world:local
```

> [!TIP]
> If you start your container on the VM with the -it flags, the container may shut down when you close your terminal.
> It will also be deleted once the container stops (this is what the --rm flag does). This is fine for testing.
> If the container needs to be permanently available, start it exclusively with the -d flag.
> Then the container will definitely stay online as long as no errors occur.
> Example: `docker run -d --name your-container-name -p 8000:8000 local`

#### Commands in the Docker container

1. open another terminal
2. List all open containers and copy the desired CONTAINER_ID `docker ps`
3. Opening up the bash shell to run a command inside an already running container `docker exec -t [container-id] bash`
4. Now you can run all commands within this running container
