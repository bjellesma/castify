The following is a list of curl commands that can be used to test an endpoint:

## Movie

| method | endpoint | command |
|---|---|---|
| POST | `/api/movies` | `curl -X post 127.0.0.1:5000/api/movies -d '{"title":"test","release_date":"2020-09-05 17:07:43"}' -H "Content-Type: application/json"` |
| PATCH | `/api/movies/<id>` | `curl -X patch 127.0.0.1:5000/api/movies/9 -d '{"title":"test-update"}' -H "Content-Type: application/json"` |

## Genres

| method | endpoint | command |
|---|---|---|
| POST | `/api/genres` | `curl -X post 127.0.0.1:5000/api/genres -d '{"name":"test-genre"}' -H "Content-Type: application/json"` |

## Actors

| method | endpoint | command |
|---|---|---|
| GET | `/api/actors` | `curl -X get 127.0.0.1:5000/api/actors` |
| POST | `/api/actors` | `curl -X post 127.0.0.1:5000/api/actors -d '{"name":"test","age":25,"gender":"male"}' -H "Content-Type: application/json"` |

## Links

| method | endpoint | command |
|---|---|---|
| POST | `/api/links/movie_actor` | `curl -X post 127.0.0.1:5000/api/links/movie_actor -d '{"movie_id":10,"actor_id":1}' -H "Content-Type: application/json"`