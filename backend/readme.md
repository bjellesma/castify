This Page contains all of the general documentation for the Castify API.

* [General](  # general)
    * [Key Dependencies](  # key-dependencies)
    * [Generation JSON Web Tokens](  # generate-jwt)
    * [API Error](  # api-errors)
* [API Reference](  # api-reference)
    * [Actors](  # actors)
        * [Get all Actors](  # get-all-actors)
        * [Get Single Actor](  # get-single-actor)
        * [Create Actor](  # create-actor)
        * [Update Actor](  # update-actor)
        * [Delete Actor](  # delete-actor)
    * [Genres](  # genres)
        * [Get all Genres](  # get-all-genres)
        * [Get Single Genre](  # get-single-genre)
        * [Create Genre](  # create-genre)
        * [Update Genre](  # update-genre)
        * [Delete Genre](  # delete-genre)
    * [Movies](  # movies)
        * [Get all Movies](  # get-all-movies)
        * [Get Single Movie](  # get-single-movie)
        * [Create Movie](  # create-movie)
        * [Update Movie](  # update-movie)
        * [Delete Movie](  # delete-movie)
* [Creating Database Migrations](  # migration)

# <a name="general">General Information</a>

# <a name="key-dependencies">Key Dependencies</a>

The backend is built heavily upon the following technologies.

- [Flask](http: // flask.pocoo.org /) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https: // www.sqlalchemy.org /) is the Python SQL toolkit and ORM we"ll use handle the lightweight sqlite database. You"ll primarily work in app.py and can reference models.py.

# <a name="generate-jwt">Generating JSON Web Tokens</a>

Most routes in Castify are non public and are only available to authenticated casting assistants, casting directors, and executive producers through the use of JSON Web Tokens(JWT). Because of this, unit tests will need valid JWTs to authenticate. JWTs also expire after a certain amount of time and will need to be refreshed. Specifically, JWTs for unit tests will be read from these fields as part of the `.env` file.

```
CASTING_ASSISTANT_JWT=CASTING_DIRECTOR_JWT=EXECUTIVE_PRODUCER_JWT=```

You can generate new JWTs by using the following steps:

**NOTE ** If a token expiration message is encountered. The following link will also be in the "message" key of the JSON response.

1. In a web browser, go to `https: // dev - cpb64ukj.us.auth0.com / authorize?audience=https: // 127.0.0.1: 5000 & response_type=token & client_id=caolVXfgEL9z2t67IMOhcl10alFoRDQs & redirect_uri=https: // 127.0.0.1: 5000 / login - results`
  * You may need to clear the cache in your browser if you"ve previously logged in .
2. Login with an auth0 user. The table below shows the relationship between roles and the JWT that it will generate

| Role | JWT |
|--- | --- |
| Casting Assistant | CASTING_ASSISTANT_JWT |
| Casting Directory | CASTING_DIRECTOR_JWT |
| Executive Producer | EXECUTIVE_PRODUCER_JWT |

# access_token=<jwt>&expires_in=86400&token_type=Bearer`. The usable JWT
# will be `<jwt>`
3. The URL you are redirected to will be something like `https: // 127.0.0.1: 5000 / login - results

4. Define the string for `< jwt >` in your `.env` file for the role.
  * For Example, if you login with an account with the Casting Assistant role, it will generate an access token that you can assign to `CASTING_ASSISTANT_JWT` in your `.env` file

Once all JWT definitions are made in your `.env` file, the tests should all be passing once again (or at least not failing with an unauthorized message).

# <a name="api-errors">API Errors</a>

All errors for the Castify API will throw JSON as errors. The following table lists some of the error codes that you may receive. The response may also include an `additional_information` string to provide additional information that may be helpful to the user. For example, If no movies are found for the GET request to `/ api / movies`, The response will be

```json
{
  "additional_information": "No movies have been found!",
  "error": 404,
  "message": "Not Found",
  "success": false
}
```

| Status Code | Response | Example JSON | Additional Notes
| --- | --- | --- | --- |
| 400 | Bad Request | `{"success": False, "error": 400, "message": "Bad Request"}` | The request was not formatted according to what the server can parse. Check your syntax. |
| 404 | Not Found | `{"success": False, "error": 404, "message": "Not Found"}` | The resource requested was not found on the server. This can be an invalid URL or accessing a book that"s not in the database. |
| 405 | Method Not allowed | `{"success": False, "error": 405, "message": "Method Not Allowed"}` | The HTTP method was not allowed for the endpoint. Check your HTTP Method against the documentation for the endpoint and ensure that it"s accepted
| 422 | Unprocessable | `{"success": False, "error": 422, "message": "Cannot process"}` | The server cannot process the data that it was given. Check the documentation to make sure that your request has the correct data types. |
| 500 | Internal Server Error | `{"success": False, "error": 500, "message": Internal Server Error"}` | The server is unable to process the request due to a bug on our end. Send a bug report support @ localhost.com complete with the exact steps to replicate the bug. |

# <a name="api-reference">API Reference</a>

This section is a breakdown of all the endpoints used, grouped by the particular resource

* [Actors](  # actors)
    * [Get all Actors](  # get-all-actors)
    * [Get Single Actor](  # get-single-actor)
    * [Create Actor](  # create-actor)
    * [Update Actor](  # update-actor)
    * [Delete Actor](  # delete-actor)
* [Genres](  # genres)
    * [Get all Genres](  # get-all-genres)
    * [Get Single Genre](  # get-single-genre)
    * [Create Genre](  # create-genre)
    * [Update Genre](  # update-genre)
    * [Delete Genre](  # delete-genre)
* [Movies](  # movies)
    * [Get all Movies](  # get-all-movies)
    * [Get Single Movie](  # get-single-movie)
    * [Create Movie](  # create-movie)
    * [Update Movie](  # update-movie)
    * [Delete Movie](  # delete-movie)

* The base URL for all requests is `http: // localhost: 5000 / api`
* Many endpoints for the Castify API will require a valid JSON web token(jwt) to authenticate.
    * An "Authentication Required" subsection is included in each endpoint documentation specifying the minimum role level that user needs. Roles are hierarchical and the hierarchy is defined in the following table.
    * Tokens can be generated using the instructions in [Generating JSON Web Tokens](  # generate-jwt) above.
    * The example curl request section will include an authorization header for the applicable request.

| Role | Includes permissions of |
|--- | --- |
| Executive Producer | Casting Director |
| Casting Director | Casting Assistant |
| Casting Assistant | None |

For Example, the executive producer role has all of the permissions of casting director(who also has all of the permissions of casting assistant).

# <a name="actors">Actors</a>

# <a name="get-all-actors">Get All Actors</a>

# Purpose

Get all actors in Castify, regardless of being linked to a movie

** Relative URL**: `/ actors`

** Full URL**: `http: // localhost: 5000 / api / actors`

** HTTP Method**: GET

# Authentication Required

Casting Assistant

# Request Format

No Request Body is sent.

# Response Format

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

# Request Example

No Request Body is sent.

# Response Example

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

# Example CUrl request

```bash
curl - X GET http: // localhost: 5000 / api / actors - H "Authorization <casting assistant JWT>"
```

# <a name="get-single-actor">Get Single Actor</a>

# Purpose

Get details on one actor in castify, reguardless of being linked to a movie

** Relative URL**: `/ actors / <actor_id >`

**Full URL**: `http: // localhost: 5000 / api / actors / <actor_id >` where `< actor_id >` is the id of the actor

** HTTP Method**: GET

# Authentication Required

Casting Assistant

# Request Format

No Request Body is sent.

# Response Format

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

# Request Example

No Request Body is sent.

# Response Example

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

# Example CUrl request

```bash
curl - X GET http: // localhost: 5000 / api / actors / 1 - H "Authorization <casting assistant JWT>"
```

# <a name="create-actor">Create Actor</a>

# Purpose

Add new actor to the Castify application.

**Relative URL**: `/ api / actors`

** Full URL**: `http: // localhost: 5000 / api / actors

** HTTP Method**: POST

# Optional HTTP Parameters

N / A

# Authentication needed

Casting Director

# Request Format

```js
{
    "name": str,
    "age": int,
    "gender": str
}
```

# Response Format

```js
{
    "actor_id": int,
    "success": boolean
}
```

# Request Example

```js
{
    "name": "Marshal Mathers",
    "age": 27,
    "gender": "male"
}
```

# Response Example

```js
{
    "actor_id": 2,
    "success": true
}
```

# Example CUrl request

```bash
curl - X POST - d '{"name": "Marshal Mathers","age": 27,"gender": "male"}' - H "Content-Type: application/json" - H "Authorization <casting director JWT>"  http: // localhost: 5000 / api / actors
```

# <a name="update-actor">Update Actor</a>

# Purpose

Update an actor in the Castify application.

**Relative URL**: `/ actors / <actor_id >` where `< actor_id >` is the id of the actor

** Full URL**: `http: // localhost: 5000 / api / actors / <actor_id >`

**HTTP Method**: Patch

# Optional HTTP Parameters

N / A

# Authentication needed

Casting Director

# Request Format

You can update one or more attributes with the following JSON

```js
{
    "name": str,
    "age": int,
    "gender": str
}
```

# Response Format

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

# Request Example

```js
{
    "name": "Marshal Mathers",
    "age": 27,
    "gender": "male"
}
```

# Response Example

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

# Example CUrl request

```bash
curl - X PATCH - d '{"name": "Marshal Mathers","age": 27,"gender": "male"}' - H "Content-Type: application/json" - H "Authorization <casting director JWT>"  http: // localhost: 5000 / api / actors
```

# <a name="delete-actor">Delete Actor</a>

# Purpose

Delete an actor in the Castify application.

**Relative URL**: `/ actors / <actor_id >` where `< actor_id >` is the id of the actor

** Full URL**: `http: // localhost: 5000 / api / actors / <actor_id >`

**HTTP Method**: Delete

# Optional HTTP Parameters

N / A

# Authentication needed

Casting Director

# Request Format

No Request Body is sent.

# Response Format

```js
{
    "actor_id": int,
    "success": bool
}
```

# Request Example

No Request Body is sent.

# Response Example

```js
{
    "actor_id": 2,
    "success": true
}
```

# Example CUrl request

```bash
curl - X Delete - H "Authorization <casting director JWT>"  http: // localhost: 5000 / api / actors / 2
```

# <a name="genres">Genres</a>

# <a name="get-all-genres">Get All Genres</a>

# Purpose

Get all genres in Castify.

**Relative URL**: `/ genres`

** Full URL**: `http: // localhost: 5000 / api / genres`

** HTTP Method**: GET

# Authentication Required

Casting Assistant

# Request Format

No Request Body is sent.

# Response Format

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

# Request Example

No Request Body is sent.

# Response Example

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

# Example CUrl request

```bash
curl - X GET http: // localhost: 5000 / api / genres - H "Authorization <casting assistant JWT>"
```

# <a name="get-single-genre">Get Single Genre</a>

# Purpose

Get details on one genre in castify

** Relative URL**: `/ genres / <genre_id >`

**Full URL**: `http: // localhost: 5000 / api / genres / <genre_id >` where `< genre_id >` is the id of the genre

** HTTP Method**: GET

# Authentication Required

Casting Assistant

# Request Format

No Request Body is sent.

# Response Format

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

# Request Example

No Request Body is sent.

# Response Example

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

# Example CUrl request

```bash
curl - X GET http: // localhost: 5000 / api / genres / 1 - H "Authorization <casting assistant JWT>"
```

# <a name="create-genre">Create Genre</a>

# Purpose

Add new genre to the Castify application.

**Relative URL**: `/ api / genres`

** Full URL**: `http: // localhost: 5000 / api / genres

** HTTP Method**: POST

# Optional HTTP Parameters

N / A

# Authentication needed

Casting Director

# Request Format

```js
{
    "name": str
}
```

# Response Format

```js
{
    "genre_id": int,
    "success": boolean
}
```

# Request Example

```js
{
    "name": "test-update-2"
}
```

# Response Example

```js
{
    "genre_id": 2,
    "success": true
}
```

# Example CUrl request

```bash
curl - X POST - d '{"name": "test-update-2"}' - H "Content-Type: application/json" - H "Authorization <casting director JWT>"  http: // localhost: 5000 / api / genres
```

# <a name="update-genre">Update Genre</a>

# Purpose

Update a genre in the Castify application.

**Relative URL**: `/ genres / <genre_id >` where `< genre_id >` is the id of the genre

** Full URL**: `http: // localhost: 5000 / api / genres / <genre_id >`

**HTTP Method**: Patch

# Optional HTTP Parameters

N / A

# Authentication needed

Casting Director

# Request Format

You can update one or more attributes with the following JSON

```js
{
    "name": str
}
```

# Response Format

```js
{
    "genre": {
        "name": str
    },
    "success": bool
}
```

# Request Example

```js
{
    "name": "test-update-3"
}
```

# Response Example

```js
{
    "genre": {
        "name": "test-update-3"
    },
    "success": true
}
```

# Example CUrl request

```bash
curl - X PATCH - d '{"name": "test-update-3"}' - H "Content-Type: application/json" - H "Authorization <casting director JWT>"  http: // localhost: 5000 / api / genres / 2
```

# <a name="delete-genre">Delete Genre</a>

# Purpose

Remove a genre from the Castify application.

**Relative URL**: `/ genres / <genre_id >` where `< genre_id >` is the id of the genre

** Full URL**: `http: // localhost: 5000 / api / genres / <genre_id >`

**HTTP Method**: Delete

# Optional HTTP Parameters

N / A

# Authentication needed

Casting Director

# Request Format

No Request Body is sent.

# Response Format

```js
{
    "genre_id": int,
    "success": bool
}
```

# Request Example

No Request Body is sent.

# Response Example

```js
{
    "genre_id": 2,
    "success": true
}
```

# Example CUrl request

```bash
curl - X Delete - H "Authorization <casting director JWT>"  http: // localhost: 5000 / api / genres / 2
```

# <a name="movies">Movies</a>

# <a name="get-all-movies">Get All Movies</a>

# Purpose

Get all movies in Castify, regardless of being linked to actors

** Relative URL**: `/ movies`

** Full URL**: `http: // localhost: 5000 / api / movies`

** HTTP Method**: GET

# Authentication Required

Casting Assistant

# Request Format

No Request Body is sent.

# Response Format

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

# Request Example

No Request Body is sent.

# Response Example

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

# Example CUrl request

```bash
curl - X GET http: // localhost: 5000 / api / movies - H "Authorization <casting assistant JWT>"
```

# <a name="get-single-movie">Get Single Movie</a>

# Purpose

Get details on one movie in castify, regardless of being linked to actors

** Relative URL**: `/ movies / <movie_id >`

**Full URL**: `http: // localhost: 5000 / api / movies / <movie_id >` where `< movie_id >` is the id of the movie

** HTTP Method**: GET

# Authentication Required

Casting Assistant

# Request Format

No Request Body is sent.

# Response Format

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

# Request Example

No Request Body is sent.

# Response Example

```js
{
    "movie": {
        "id": 10,
        "title": "test"
    },
    "success": true
}
```

# Example CUrl request

```bash
curl - X GET http: // localhost: 5000 / api / movies / 10 - H "Authorization <casting assistant JWT>"
```

# <a name="create-movie">Create Movie</a>

# Purpose

Add new movie to the Castify application.

**Relative URL**: `/ api / movies`

** Full URL**: `http: // localhost: 5000 / api / movies

** HTTP Method**: POST

# Optional HTTP Parameters

N / A

# Authentication needed

Executive Producer

# Request Format

```js
{
    "title": str,
    "release_date": str
}
```

# Response Format

```js
{
    "movie_id": int,
    "success": boolean
}
```

# Request Example

```js
{
    "title": "test2",
    "release_date": "2020-09-05 17:07:43"
}
```

# Response Example

```js
{
    "movie_id": 11,
    "success": true
}
```

# Example CUrl request

```bash
curl - X POST - d '{"title":"test2","release_date":"2020-09-05 17:07:43"}' - H "Content-Type: application/json" - H "Authorization <executive producer JWT>"  http: // localhost: 5000 / api / movies
```

# <a name="update-movie">Update Movie</a>

# Purpose

Update an movie in the Castify application.

**Relative URL**: `/ movies / <movie_id >` where `< movie_id >` is the id of the movie

** Full URL**: `http: // localhost: 5000 / api / movies / <movie_id >`

**HTTP Method**: Patch

# Optional HTTP Parameters

N / A

# Authentication needed

Casting Director

# Request Format

You can update one or more attributes with the following JSON

```js
{
    "title": str,
    "release_date": str
}
```

# Response Format

```js
{
    "movie": {
        "id": int,
        "title": str
    },
    "success": boolean
}
```

# Request Example

Notice that release date is not being updated in this example

```js
{
    "name": "test3"
}
```

# Response Example

```js
{
    "movie": {
        "id": 10,
        "title": "test3"
    },
    "success": true
}
```

# Example CUrl request

```bash
curl - X PATCH - d '{"name": "test3"}' - H "Content-Type: application/json" - H "Authorization <casting director JWT>"  http: // localhost: 5000 / api / movies / 10
```

# <a name="delete-movie">Delete Movie</a>

# Purpose

From a movie from the Castify application.

**Relative URL**: `/ movies / <movie_id >` where `< movie_id >` is the id of the movie

** Full URL**: `http: // localhost: 5000 / api / movies / <movie_id >`

**HTTP Method**: Delete

# Optional HTTP Parameters

N / A

# Authentication needed

Executive Producer

# Request Format

No Request Body is sent.

# Response Format

```js
{
    "movie_id": int,
    "success": bool
}
```

# Request Example

No Request Body is sent.

# Response Example

```js
{
    "movie_id": 11,
    "success": true
}
```

# Example CUrl request

```bash
curl - X Delete - H "Authorization <executive producer JWT>"  http: // localhost: 5000 / api / movies / 11
```



# <a name="migration">Creating Database Migrations</a>

Database Migrations are used with Castify to make it easier to manage database versions. Any change to the database schema should use the following steps

1. If no db migrations have been performed, if there is no `/ backend / migrations` folder, run `npm run db - init` to create the migrations folder.
2. Make a change to the database schema by editing one of the files in `/models`. For example, in the following code, we've added release date as a column to the movie database.

```py
class Movie(db.Model):
    __tablename__='movie'
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String, nullable=False)
    release_date=db.Column(db.DateTime, nullable=False)
```

3. Run `npm run db - migrate` to create a migration script in `/backend / migrations / alembic / versions`. Your output from the command will read as the following:

```
INFO[alembic.autogenerate.compare] Detected added column 'movie.release_date'
```

Notice that running this command alone will not change the schema of the database yet. You can verify this by using a command line tool on your database.

4. Run `npm run db - upgrade` to upgrade the database to the newest version.

You can verify that the column was added by using a command line tool on your database.

5. If the database changes were not as you expected, you can downgrade the database by run `npm run db - downgrade`
