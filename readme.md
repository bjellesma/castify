# What is Castify

Executive Producers need a way to see all of the movies as well as the actors assigned to them. Enter Castify. Castify is a backend API to help producers create movies by casting actors to movie. Authenticated producers will simply call endpoints to create movies and assign actors. It's. That. Simple. Read more about our [backend API](backend/readme.md) 

The live version of this API is hosted at [https://castifyio.herokuapp.com/](https://castifyio.herokuapp.com/).

# Roles

Castify is based on users that have access to different API endpoints.

| Permission | Casting Assistant | Casting Director | Executive Producer |
|---|---|---|---|
| View Actors | Yes | Yes | Yes |
| View Genres | Yes | Yes | Yes |
| View Movies | Yes | Yes | Yes |
| Add Actors | No | Yes | Yes |
| Add Genres | No | Yes | Yes |
| Add Movies | No | No | Yes |
| Modify Actors | No | Yes | Yes |
| Modify Genres | No | Yes | Yes |
| Modify Movies | No | Yes | Yes |
| Remove Actors | No | Yes | Yes |
| Remove Genres | No | Yes | Yes |
| Remove Movies | No | No | Yes |

For Example, the only permissions that an executive producer has over a casting director are to create and remove movies. On API references of the [backend documentation](backend/readme.md), each endpoint will also contain an "Authentication Required" section which has the minimum level of authorization needed.

# Contributing

First and foremost, this is a project for the [Full Stack Web Developer nanodegree program at Udacity](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044). This being said, Castify always welcomes contributions. For the best chances of your pull requests being accepted, please read and follow all of the guidelines below. 

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
`DATABASE_TYPE=`The type of database that the user has created. This app has only been tested with postgresql
`DATABASE_HOST=`The host of your database. Use "localhost" if you're setting up a local database.
`DATABASE_PORT=`port number that the database runs on.
`DATABASE_USER=`username of user that has access to the database created by the user.
`DATABASE_PASSWORD=`password for the database. Leave lank if no password is set.
`DATABASE_DATABASE=`LEAVE THIS VALUE unless you know what you're doing! This is the database housing all actors, models, and genres.
`DATABASE_URL=`This value is used to connect to a database if `DEPLOY` is set to True. This value is typically used with a cloud database on Heroku.
`TEST_DATABASE=`LEAVE THIS VALUE unless you know what you're doing! This is the database to be used for unit tests.
`AUTH0_DOMAIN=`LEAVE THIS VALUE unless you know what you're doing! The authentication domain used by Auth0 to authenticate.
`ALGORITHM=`LEAVE THIS VALUE unless you know what you're doing! The algorithm that will be used by Auth0 to make web tokens.
`API_AUDIENCE=`LEAVE THIS VALUE unless you know what you're doing! The audience that Auth0 will use to authenticate you.
`DEBUG=`If true, the app will run in debug so that it can host reload.
`DEPLOY=`If true, the app will act as if it is deployed to Heroku 
`CASTING_ASSISTANT_JWT=`JSON web token for casting assistants. This value is only used in unit testing and if `DEPLOY` is set to False.
`CASTING_DIRECTOR_JWT=`JSON web token for casting assistants. This value is only used in unit testing and if `DEPLOY` is set to False.
`EXECUTIVE_PRODUCER_JWT=`JSON web token for casting assistants. This value is only used in unit testing and if `DEPLOY` is set to False.

The following is an example of a complete `.env` file:
```
DATABASE_TYPE=postgresql
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USER=user
DATABASE_PASSWORD=password
DATABASE_DATABASE=agency
DATABASE_URL=
TEST_DATABASE=agency_test
AUTH0_DOMAIN=dev-cpb64ukj.us.auth0.com
ALGORITHM=RS256
API_AUDIENCE=https://127.0.0.1:5000
DEBUG=True
DEPLOY=False
CASTING_ASSISTANT_JWT=<secret>
CASTING_DIRECTOR_JWT=<secret>
EXECUTIVE_PRODUCER_JWT=<secret>
```

3. Run `pipenv install` to install the virtual environment
    1. This command will also install the backend packages located inside of `pipfile`

5. Run `npm run server` to start the development server.

6. Open a webbrowser and ensure that you can connect to [http://localhost:5000](http://localhost:5000)
    1. You should be greeted with a welcome message saying "Hello API"

## Code Style Guide

This code abides by [PEP8](https://www.python.org/dev/peps/pep-0008/) with the exception of using tabs over any spaces. Please use this as a guide when making pull requests to this project.

# Deployment

Currently, this API is hosted at heroku at [https://castifyio.herokuapp.com/](https://castifyio.herokuapp.com/). All of the above environmental variables will need to be setup on heroku as [configuration variables](https://devcenter.heroku.com/articles/config-vars) when deploying.

# Credits

* Bill Jellesma
* Udacity - Udacity created the idea for the course as a teaching project

Below is a copy of the backend documentation:

This Page contains all of the general documentation for the Castify API.

* [General](#general)
    * [Key Dependencies](#key-dependencies)
    * [Generation JSON Web Tokens](#generate-jwt)
    * [API Error](#api-errors)
* [API Reference](#api-reference)
    * [Actors](#actors)
        * [Get all Actors](#get-all-actors)
        * [Get Single Actor](#get-single-actor)
        * [Create Actor](#create-actor)
        * [Update Actor](#update-actor)
        * [Delete Actor](#delete-actor)
    * [Genres](#genres)
        * [Get all Genres](#get-all-genres)
        * [Get Single Genre](#get-single-genre)
        * [Create Genre](#create-genre)
        * [Update Genre](#update-genre)
        * [Delete Genre](#delete-genre)
    * [Movies](#movies)
        * [Get all Movies](#get-all-movies)
        * [Get Single Movie](#get-single-movie)
        * [Create Movie](#create-movie)
        * [Update Movie](#update-movie)
        * [Delete Movie](#delete-movie)
* [Creating Database Migrations](#migration)

# <a name="general">General Information</a>

## <a name="key-dependencies">Key Dependencies</a>

The backend is built heavily upon the following technologies.

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we"ll use handle the lightweight sqlite database. You"ll primarily work in app.py and can reference models.py. 

## <a name="generate-jwt">Generating JSON Web Tokens</a>

Most routes in Castify are non public and are only available to authenticated casting assistants, casting directors, and executive producers through the use of JSON Web Tokens (JWT). Because of this, unit tests will need valid JWTs to authenticate. JWTs also expire after a certain amount of time and will need to be refreshed. Specifically, JWTs for unit tests will be read from these fields as part of the `.env` file.

```
CASTING_ASSISTANT_JWT=
CASTING_DIRECTOR_JWT=
EXECUTIVE_PRODUCER_JWT=
```

You can generate new JWTs by using the following steps:

**NOTE** If a token expiration message is encountered. The following link will also be in the "message" key of the JSON response.

1. In a web browser, go to `https://dev-cpb64ukj.us.auth0.com/authorize?audience=https://127.0.0.1:5000&response_type=token&client_id=caolVXfgEL9z2t67IMOhcl10alFoRDQs&redirect_uri=https://127.0.0.1:5000/login-results`
  * You may need to clear the cache in your browser if you"ve previously logged in. 
2. Login with an auth0 user. The table below shows the relationship between roles and the JWT that it will generate

| Role | JWT |
|---|---|
| Casting Assistant | CASTING_ASSISTANT_JWT |
| Casting Directory | CASTING_DIRECTOR_JWT |
| Executive Producer | EXECUTIVE_PRODUCER_JWT |

3. The URL you are redirected to will be something like `https://127.0.0.1:5000/login-results#access_token=<jwt>&expires_in=86400&token_type=Bearer`. The usable JWT will be `<jwt>`

4. Define the string for `<jwt>` in your `.env` file for the role.
  * For Example, if you login with an account with the Casting Assistant role, it will generate an access token that you can assign to `CASTING_ASSISTANT_JWT` in your `.env` file 

Once all JWT definitions are made in your `.env` file, the tests should all be passing once again (or at least not failing with an unauthorized message).

## <a name="api-errors">API Errors</a>

All errors for the Castify API will throw JSON as errors. The following table lists some of the error codes that you may receive. The response may also include an `additional_information` string to provide additional information that may be helpful to the user. For example, If no movies are found for the GET request to `/api/movies`, The response will be 

```json
{
  "additional_information": "No movies have been found!", 
  "error": 404, 
  "message": "Not Found", 
  "success": false
}
```

| Status Code | Response | Example JSON | Additional Notes
|---|---|---|---|
| 400 | Bad Request | `{"success": False, "error": 400,"message": "Bad Request"}` | The request was not formatted according to what the server can parse. Check your syntax. |
| 404 | Not Found | `{"success": False, "error": 404,"message": "Not Found"}` | The resource requested was not found on the server. This can be an invalid URL or accessing a book that"s not in the database. |
| 405 | Method Not allowed | `{"success": False, "error": 405,"message": "Method Not Allowed"}` | The HTTP method was not allowed for the endpoint. Check your HTTP Method against the documentation for the endpoint and ensure that it"s accepted
| 422 | Unprocessable | `{"success": False, "error": 422,"message": "Cannot process"}` | The server cannot process the data that it was given. Check the documentation to make sure that your request has the correct data types. |
| 500 | Internal Server Error | `{"success": False, "error": 500,"message": Internal Server Error"}` | The server is unable to process the request due to a bug on our end. Send a bug report support@localhost.com complete with the exact steps to replicate the bug. |

# <a name="api-reference">API Reference</a>

This section is a breakdown of all the endpoints used, grouped by the particular resource

* [Actors](#actors)
    * [Get all Actors](#get-all-actors)
    * [Get Single Actor](#get-single-actor)
    * [Create Actor](#create-actor)
    * [Update Actor](#update-actor)
    * [Delete Actor](#delete-actor)
* [Genres](#genres)
    * [Get all Genres](#get-all-genres)
    * [Get Single Genre](#get-single-genre)
    * [Create Genre](#create-genre)
    * [Update Genre](#update-genre)
    * [Delete Genre](#delete-genre)
* [Movies](#movies)
    * [Get all Movies](#get-all-movies)
    * [Get Single Movie](#get-single-movie)
    * [Create Movie](#create-movie)
    * [Update Movie](#update-movie)
    * [Delete Movie](#delete-movie)

* The base URL for all requests is `http://localhost:5000/api`
* Many endpoints for the Castify API will require a valid JSON web token (jwt) to authenticate. 
    * An "Authentication Required" subsection is included in each endpoint documentation specifying the minimum role level that user needs. Roles are hierarchical and the hierarchy is defined in the following table.
    * Tokens can be generated using the instructions in [Generating JSON Web Tokens](#generate-jwt) above.
    * The example curl request section will include an authorization header for the applicable request.

| Role | Includes permissions of |
|---|---|
| Executive Producer | Casting Director |
| Casting Director | Casting Assistant |
| Casting Assistant | None |

For Example, the executive producer role has all of the permissions of casting director (who also has all of the permissions of casting assistant).

## <a name="actors">Actors</a>

### <a name="get-all-actors">Get All Actors</a>

#### Purpose

Get all actors in Castify, regardless of being linked to a movie

**Relative URL**: `/actors`

**Full URL**: `http://localhost:5000/api/actors`

**HTTP Method**: GET

#### Authentication Required

Casting Assistant

#### Request Format

No Request Body is sent.

#### Response Format

```js
{
    "actors": [
        {
            "age": int,
            "gender": str,
            "id": int,
            "name": str
        }
    ],
    "success": true
}
```

#### Request Example

No Request Body is sent.

#### Response Example

```js
{
    "actors": [
        {
            "age": 25,
            "gender": "Gender.male",
            "id": 1,
            "name": "test-update-2"
        }
    ],
    "success": true
}
```

#### Example CUrl request

```bash
curl -X GET http://localhost:5000/api/actors -H "Authorization <casting assistant JWT>"  
```

### <a name="get-single-actor">Get Single Actor</a>

#### Purpose

Get details on one actor in castify, reguardless of being linked to a movie

**Relative URL**: `/actors/<actor_id>`

**Full URL**: `http://localhost:5000/api/actors/<actor_id>` where `<actor_id>` is the id of the actor

**HTTP Method**: GET

#### Authentication Required

Casting Assistant

#### Request Format

No Request Body is sent.

#### Response Format

```js
{
    "actor": [
        {
            "age": int,
            "gender": str,
            "id": int,
            "name": str
        }
    ],
    "success": boolean
}
```

#### Request Example

No Request Body is sent.

#### Response Example

```js
{
    "actor": [
        {
            "age": 25,
            "gender": "Gender.male",
            "id": 1,
            "name": "test-update-2"
        }
    ],
    "success": true
}
```

#### Example CUrl request

```bash
curl -X GET http://localhost:5000/api/actors/1 -H "Authorization <casting assistant JWT>"  
```

### <a name="create-actor">Create Actor</a>

#### Purpose

Add new actor to the Castify application.

**Relative URL**: `/api/actors`

**Full URL**: `http://localhost:5000/api/actors

**HTTP Method**: POST

#### Optional HTTP Parameters

N/A

#### Authentication needed

Casting Director

#### Request Format

```js
{
    "name": str,
    "age": int,
    "gender": str
}
```

#### Response Format

```js
{
    "actor_id": int,
    "success": boolean
}
```

#### Request Example

```js
{
    "name": "Marshal Mathers",
    "age": 27,
    "gender": "male"
}
```

#### Response Example

```js
{
    "actor_id": 2,
    "success": true
}
```

#### Example CUrl request

```bash
curl -X POST -d '{"name": "Marshal Mathers","age": 27,"gender": "male"}' -H "Content-Type: application/json" -H "Authorization <casting director JWT>"  http://localhost:5000/api/actors
```

### <a name="update-actor">Update Actor</a>

#### Purpose

Update an actor in the Castify application.

**Relative URL**: `/actors/<actor_id>` where `<actor_id>` is the id of the actor

**Full URL**: `http://localhost:5000/api/actors/<actor_id>`

**HTTP Method**: Patch

#### Optional HTTP Parameters

N/A

#### Authentication needed

Casting Director

#### Request Format

You can update one or more attributes with the following JSON

```js
{
    "name": str,
    "age": int,
    "gender": str
}
```

#### Response Format

```js
{
    "actor": {
        "age": int,
        "gender": str,
        "id": int,
        "name": str
    },
    "success": bool
}
```

#### Request Example

```js
{
    "name": "Marshal Mathers",
    "age": 27,
    "gender": "male"
}
```

#### Response Example

```js
{
    "actor": {
        "age": 27,
        "gender": "Gender.male",
        "id": 1,
        "name": "Marshal Mathers"
    },
    "success": true
}
```

#### Example CUrl request

```bash
curl -X PATCH -d '{"name": "Marshal Mathers","age": 27,"gender": "male"}' -H "Content-Type: application/json" -H "Authorization <casting director JWT>"  http://localhost:5000/api/actors
```

### <a name="delete-actor">Delete Actor</a>

#### Purpose

Delete an actor in the Castify application.

**Relative URL**: `/actors/<actor_id>` where `<actor_id>` is the id of the actor

**Full URL**: `http://localhost:5000/api/actors/<actor_id>`

**HTTP Method**: Delete

#### Optional HTTP Parameters

N/A

#### Authentication needed

Casting Director

#### Request Format

No Request Body is sent.

#### Response Format

```js
{
    "actor_id": int,
    "success": bool
}
```

#### Request Example

No Request Body is sent.

#### Response Example

```js
{
    "actor_id": 2,
    "success": true
}
```

#### Example CUrl request

```bash
curl -X Delete -H "Authorization <casting director JWT>"  http://localhost:5000/api/actors/2
```

## <a name="genres">Genres</a>

### <a name="get-all-genres">Get All Genres</a>

#### Purpose

Get all genres in Castify.

**Relative URL**: `/genres`

**Full URL**: `http://localhost:5000/api/genres`

**HTTP Method**: GET

#### Authentication Required

Casting Assistant

#### Request Format

No Request Body is sent.

#### Response Format

```js
{
    "genres": [
        {
            "name": str
        }
    ],
    "success": boolean
}
```

#### Request Example

No Request Body is sent.

#### Response Example

```js
{
    "genres": [
        {
            "name": "test-genre"
        }
    ],
    "success": true
}
```

#### Example CUrl request

```bash
curl -X GET http://localhost:5000/api/genres -H "Authorization <casting assistant JWT>"  
```

### <a name="get-single-genre">Get Single Genre</a>

#### Purpose

Get details on one genre in castify

**Relative URL**: `/genres/<genre_id>`

**Full URL**: `http://localhost:5000/api/genres/<genre_id>` where `<genre_id>` is the id of the genre

**HTTP Method**: GET

#### Authentication Required

Casting Assistant

#### Request Format

No Request Body is sent.

#### Response Format

```js
{
    "genre": [
        {
            "name": int
        }
    ],
    "success": boolean
}
```

#### Request Example

No Request Body is sent.

#### Response Example

```js
{
    "genre": [
        {
            "age": "test-genre"
        }
    ],
    "success": true
}
```

#### Example CUrl request

```bash
curl -X GET http://localhost:5000/api/genres/1 -H "Authorization <casting assistant JWT>"  
```

### <a name="create-genre">Create Genre</a>

#### Purpose

Add new genre to the Castify application.

**Relative URL**: `/api/genres`

**Full URL**: `http://localhost:5000/api/genres

**HTTP Method**: POST

#### Optional HTTP Parameters

N/A

#### Authentication needed

Casting Director

#### Request Format

```js
{
    "name": str
}
```

#### Response Format

```js
{
    "genre_id": int,
    "success": boolean
}
```

#### Request Example

```js
{
    "name": "test-update-2"
}
```

#### Response Example

```js
{
    "genre_id": 2,
    "success": true
}
```

#### Example CUrl request

```bash
curl -X POST -d '{"name": "test-update-2"}' -H "Content-Type: application/json" -H "Authorization <casting director JWT>"  http://localhost:5000/api/genres
```

### <a name="update-genre">Update Genre</a>

#### Purpose

Update a genre in the Castify application.

**Relative URL**: `/genres/<genre_id>` where `<genre_id>` is the id of the genre

**Full URL**: `http://localhost:5000/api/genres/<genre_id>`

**HTTP Method**: Patch

#### Optional HTTP Parameters

N/A

#### Authentication needed

Casting Director

#### Request Format

You can update one or more attributes with the following JSON

```js
{
    "name": str
}
```

#### Response Format

```js
{
    "genre": {
        "name": str
    },
    "success": bool
}
```

#### Request Example

```js
{
    "name": "test-update-3"
}
```

#### Response Example

```js
{
    "genre": {
        "name": "test-update-3"
    },
    "success": true
}
```

#### Example CUrl request

```bash
curl -X PATCH -d '{"name": "test-update-3"}' -H "Content-Type: application/json" -H "Authorization <casting director JWT>"  http://localhost:5000/api/genres/2
```

### <a name="delete-genre">Delete Genre</a>

#### Purpose

Remove a genre from the Castify application.

**Relative URL**: `/genres/<genre_id>` where `<genre_id>` is the id of the genre

**Full URL**: `http://localhost:5000/api/genres/<genre_id>`

**HTTP Method**: Delete

#### Optional HTTP Parameters

N/A

#### Authentication needed

Casting Director

#### Request Format

No Request Body is sent.

#### Response Format

```js
{
    "genre_id": int,
    "success": bool
}
```

#### Request Example

No Request Body is sent.

#### Response Example

```js
{
    "genre_id": 2,
    "success": true
}
```

#### Example CUrl request

```bash
curl -X Delete -H "Authorization <casting director JWT>"  http://localhost:5000/api/genres/2
```

## <a name="movies">Movies</a>

### <a name="get-all-movies">Get All Movies</a>

#### Purpose

Get all movies in Castify, regardless of being linked to actors

**Relative URL**: `/movies`

**Full URL**: `http://localhost:5000/api/movies`

**HTTP Method**: GET

#### Authentication Required

Casting Assistant

#### Request Format

No Request Body is sent.

#### Response Format

```js
{
    "movies": [
        {
            "id": int,
            "title": str
        }
    ],
    "success": boolean
}
```

#### Request Example

No Request Body is sent.

#### Response Example

```js
{
    "movies": [
        {
            "id": 9,
            "title": "test"
        },
        {
            "id": 10,
            "title": "test"
        }
    ],
    "success": true
}
```

#### Example CUrl request

```bash
curl -X GET http://localhost:5000/api/movies -H "Authorization <casting assistant JWT>"  
```

### <a name="get-single-movie">Get Single Movie</a>

#### Purpose

Get details on one movie in castify, regardless of being linked to actors

**Relative URL**: `/movies/<movie_id>`

**Full URL**: `http://localhost:5000/api/movies/<movie_id>` where `<movie_id>` is the id of the movie

**HTTP Method**: GET

#### Authentication Required

Casting Assistant

#### Request Format

No Request Body is sent.

#### Response Format

```js
{
    "movies": [
        {
            "id": int,
            "title": str
        }
    ],
    "success": boolean
}
```

#### Request Example

No Request Body is sent.

#### Response Example

```js
{
    "movie": {
        "id": 10,
        "title": "test"
    },
    "success": true
}
```

#### Example CUrl request

```bash
curl -X GET http://localhost:5000/api/movies/10 -H "Authorization <casting assistant JWT>"  
```

### <a name="create-movie">Create Movie</a>

#### Purpose

Add new movie to the Castify application.

**Relative URL**: `/api/movies`

**Full URL**: `http://localhost:5000/api/movies

**HTTP Method**: POST

#### Optional HTTP Parameters

N/A

#### Authentication needed

Executive Producer

#### Request Format

```js
{
    "title":str,
    "release_date":str
}
```

#### Response Format

```js
{
    "movie_id": int,
    "success": boolean
}
```

#### Request Example

```js
{
    "title":"test2",
    "release_date":"2020-09-05 17:07:43"
}
```

#### Response Example

```js
{
    "movie_id": 11,
    "success": true
}
```

#### Example CUrl request

```bash
curl -X POST -d '{"title":"test2","release_date":"2020-09-05 17:07:43"}' -H "Content-Type: application/json" -H "Authorization <executive producer JWT>"  http://localhost:5000/api/movies
```

### <a name="update-movie">Update Movie</a>

#### Purpose

Update an movie in the Castify application.

**Relative URL**: `/movies/<movie_id>` where `<movie_id>` is the id of the movie

**Full URL**: `http://localhost:5000/api/movies/<movie_id>`

**HTTP Method**: Patch

#### Optional HTTP Parameters

N/A

#### Authentication needed

Casting Director

#### Request Format

You can update one or more attributes with the following JSON

```js
{
    "title": str,
    "release_date": str
}
```

#### Response Format

```js
{
    "movie": {
        "id": int,
        "title": str
    },
    "success": boolean
}
```

#### Request Example

Notice that release date is not being updated in this example

```js
{
    "name": "test3"
}
```

#### Response Example

```js
{
    "movie": {
        "id": 10,
        "title": "test3"
    },
    "success": true
}
```

#### Example CUrl request

```bash
curl -X PATCH -d '{"name": "test3"}' -H "Content-Type: application/json" -H "Authorization <casting director JWT>"  http://localhost:5000/api/movies/10
```

### <a name="delete-movie">Delete Movie</a>

#### Purpose

From a movie from the Castify application.

**Relative URL**: `/movies/<movie_id>` where `<movie_id>` is the id of the movie

**Full URL**: `http://localhost:5000/api/movies/<movie_id>`

**HTTP Method**: Delete

#### Optional HTTP Parameters

N/A

#### Authentication needed

Executive Producer

#### Request Format

No Request Body is sent.

#### Response Format

```js
{
    "movie_id": int,
    "success": bool
}
```

#### Request Example

No Request Body is sent.

#### Response Example

```js
{
    "movie_id": 11,
    "success": true
}
```

#### Example CUrl request

```bash
curl -X Delete -H "Authorization <executive producer JWT>"  http://localhost:5000/api/movies/11
```



# <a name="migration">Creating Database Migrations</a>

Database Migrations are used with Castify to make it easier to manage database versions. Any change to the database schema should use the following steps

1. If no db migrations have been performed, if there is no `/backend/migrations` folder, run `npm run db-init` to create the migrations folder.
2. Make a change to the database schema by editing one of the files in `/models`. For example, in the following code, we've added release date as a column to the movie database.

```py
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
```

3. Run `npm run db-migrate` to create a migration script in `/backend/migrations/alembic/versions`. Your output from the command will read as the following:

```
INFO  [alembic.autogenerate.compare] Detected added column 'movie.release_date'
```

Notice that running this command alone will not change the schema of the database yet. You can verify this by using a command line tool on your database.

4. Run `npm run db-upgrade` to upgrade the database to the newest version.

You can verify that the column was added by using a command line tool on your database.

5. If the database changes were not as you expected, you can downgrade the database by run `npm run db-downgrade`

