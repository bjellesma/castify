# What is Castify

Castify is a backend API to help producers create movies by casting actors to movie. Authenticated producers will simply call endpoints to create movies and assign actors. It's. That. Simple. Read more about our [backend API](backend/readme.md) 

# Contributing

## Notes

* For any contributions to the API, please include in your pull request an update to [the api documentation section of the backend readme](backend/readme.md)

1. Ensure that your system has all of the dependencies for Castify development by checking the below [prerequisites section](#prerequisites).

2. Fork this repository and clone it to your machine.

3. Use the [environment setup instructions below](#setup) to set up a local development server
    1. Use the api documentation for more information on how to make requests to the endpoints.

4. Once you've made any modifications using the Code Style Guide listed in the next section, run the code through unit tests using `npm run test-full`.
    1. If you've written any new endpoints, please also write a new unit test for the endpoint.
    2. Please also pay attention to the code coverage as output and ensure that coverage is at least 80%
5. When your code is passing the unit tests, please submit a pull request

## Prerequisites

1. Download and install [Python](https://www.python.org/downloads/) if it is not already available on your system
2. `pipenv` is used as the virtual environment for this application and you can install it using `pip install pipenv`
3. Install [NodeJS](https://nodejs.org/en/download/) in order to run the development scripts
2. Create a database from your database installation for use in the app
    1. In Postgresql, for example, you can install a local database with `createdb agency` and test database with `createdb agency_test`

## Environment Setup Instructions

0. Clone this project to your machine.

1. From the command line, navigate to the backend directory, `casting-agency/backend`.

2. Edit `.env-template` and fill in the information to connect to the database of your choice
    1. Rename the file as `.env` so that it will be recognized by the app
    
    *Note*: This app has only been tested using postgres

The following is the schema as well as the expected data for the `.env` file
```
DATABASE_TYPE=The type of database that the user has created. This app has only been tested with postgresql
DATABASE_HOST=LEAVE THIS VALUE AS localhost!
DATABASE_PORT=port number that the database runs on
DATABASE_USER=username of user that has access to the database created by the user
DATABASE_PASSWORD=password for the database. Leave lank if no password is set
DATABASE_DATABASE=LEAVE THIS VALUE AS trivia!
TEST_DATABASE=LEAVE THIS VALUE AS trivia_test!
DEBUG=Boolean. If true, the app will run in debug so that it can host reload
```
The following is an example of a complete `.env` file:
```
DATABASE_TYPE=postgresql
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USER=user
DATABASE_PASSWORD=password
DATABASE_DATABASE=trivia
TEST_DATABASE=agency
DEBUG=True
```

3. Run `pipenv install` to install the virtual environment
    1. This command will also install the backend packages located inside of `pipfile`

5. Run `npm run server` to start the development server.

6. Open a webbrowser and ensure that you can connect to [http://localhost:5000](http://localhost:5000)
    1. You should be greeted with a welcome message saying "Hello API"

## Code Style Guide

This code abides by [PEP8](https://www.python.org/dev/peps/pep-0008/) with the exception of using tabs over any spaces. Please use this as a guide when making pull requests to this project.

# Credits

* Bill Jellesma
* Udacity - Udacity created the idea for the course as a teaching project
