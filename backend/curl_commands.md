The following is a list of curl commands that can be used to test an endpoint:
| method | endpoint | command |
|---|---|---|
| POST | `/api/movies` | `curl -X post 127.0.0.1:5000/api/movies -d '{"title":"test","release_date":"2020-09-05 17:07:43"}' -H "Content-Type: application/json"` |
| PATCH | `/api/movies/<id>` | `curl -X patch 127.0.0.1:5000/api/movies/9 -d '{"title":"test-update"}' -H "Content-Type: application/json"` |