import functools

from flask import make_response, json
import werkzeug.exceptions as exc
from werkzeug.wrappers import BaseResponse

def jsonify(func):
    """
    If we decorate a view function with jsonify, we wrap our success message around
    it and return the jsonified data. If we catch a werkzeug HTTPException, we pull
    the status code out of it, and return the response with the found code.
    """

    @functools.wraps(func)
    def convert(*args, **kwargs):

        success = True
        code = 200      # default status code - success!

        try:
            result = func(*args, **kwargs)

            if isinstance(result, BaseResponse):
                return result

        except exc.HTTPException as ex:
            # i'd like to be able to just re-raise e here, but the body of the
            # response is e.get_body() instead of e.description - so we have to
            # just set up the response ourselves
            result  = { 'message' : ex.description }
            code    = ex.code

        except Exception as ex:
            result = { 'message' : 'Internal Server Error', 'system_message' : ex.message }
            code = 500

        # build a response object, and change the content type header to json
        response = make_response(json.dumps(result))
        response.headers['Content-Type'] = 'application/json'
        response.status_code = code

        return response

    # return the function that is taking the place of (or masquerading as) our decorated function
    return convert
