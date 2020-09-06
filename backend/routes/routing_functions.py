from flask import abort

def validate_against_api(data, schema, request, optional=False):
    """Validate data sent to an api endpoint

    Args:
        data (object): decoded json object sent to the endpoint
        schema (object): voluptous schema object. Project available at https://github.com/alecthomas/voluptuous
        request (object): flask request object to make calls on
        optional (bool): if optional flag is set. requirement errors will be passed over.
            This is mostly to deal with PATCH methods so that the user can update only one field

    Returns:
        string list: list of string error messages to send back to the endpoint to handle.
    """
    api_errors = []
    try:
        data = schema(data)
    except Exception as errors:
        for err in errors.errors:
            if err.msg == "required key not provided":
                if not optional:
                    api_errors.append(f'{err.path[0]} was required and not provided for call to {request.path} as {request.method}. Please consult the documentation for this endpoint.')
            elif 'expected' in err.msg:
                api_errors.append(f'{err.path[0]} was in the incorrect format for call to {request.path} as {request.method}. Please consult the documentation for this endpoint.')
    return api_errors

def flask_abort(status_code, message="This call was aborted and no additional information is available"):
    """Function to abort client call. Housed in routing functions so that we don't expose flask commands to the models.

    Args:
        status_code (int): http code causing the abort
        message (str): optional message to send to the user
    """
    abort(status_code, description=message)