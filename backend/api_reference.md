# Introduction

Castify is a backend API to help producers create movies by casting actors to movie. Authenticated producers will simply call endpoints to create movies and assign actors. It's. That. Simple.

# Getting Started 

* The base URL for all requests is `http://localhost:5000`

# Errors

The following table lists some of the error codes that you may receive. The response may also include an `additional_information` string to provide additional information that may be helpful to the user. For example, If no movies are found for the GET request to `/api/movies`, The response will be 

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
| 404 | Not Found | `{"success": False, "error": 404,"message": "Not Found"}` | The resource requested was not found on the server. This can be an invalid URL or accessing a book that's not in the database. |
| 405 | Method Not allowed | `{"success": False, "error": 405,"message": "Method Not Allowed"}` | The HTTP method was not allowed for the endpoint. Check your HTTP Method against the documentation for the endpoint and ensure that it's accepted
| 422 | Unprocessable | `{"success": False, "error": 422,"message": "Cannot process"}` | The server cannot process the data that it was given. Check the documentation to make sure that your request has the correct data types. |
| 500 | Internal Server Error | `{"success": False, "error": 500,"message": Internal Server Error"}` | The server is unable to process the request due to a bug on our end. Send a bug report support@localhost.com complete with the exact steps to replicate the bug. |

# Creating test scripts

If your contribution to the api involves making a change to the structure of the database, you may need to make changes to the test database. Because unit testing will generate a test database from `agency.psql`, you will need to make changes to the script. The following is a quick set of instructions to change this script correctly without needing to know sql:

1. Get the database to a point that you're happy with to create a test. Even though this is possible through using API calls alone, using sql may prove to be faster and easier.
2. In a command line, navigate to `/backend` of this project.
3. Run `npm run create-test` to generate a new `agency.psq` file.
    * **Note** This will overwrite the current `agency.psql` file which may make testing, and any planned contributions, unusable. Please only proceed if you understand the risks involved.