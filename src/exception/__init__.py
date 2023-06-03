import logging
from flask.json import jsonify

from src.constant import INTERNAL_SERVER_ERROR, INVALID_REQUEST, RESOURCE_NOT_FOUND

log = logging.getLogger(__name__)


def global_exception_handler(error):
    if isinstance(error, RecordNotFoundException):
        log.exception("Resource not found: %s", error)
        status_code = 404
        message = RESOURCE_NOT_FOUND
    elif isinstance(error, InvalidRequestException):
        log.exception("Invalid request: %s", error)
        status_code = 400
        message = INVALID_REQUEST
    elif isinstance(error, EntitySaveException) or isinstance(error, EntityUpdateException):
        log.exception("Save/Update failed: %s", error)
        status_code = 500
        message = INTERNAL_SERVER_ERROR
    else:
        log.exception("Internet Server Error: %s", error)
        status_code = 500
        message = INTERNAL_SERVER_ERROR

    return handle_error(status_code, message, str(error))


def handle_error(status_code, message=None, errors=None):
    response = {'message': message}
    if errors:
        response['errors'] = errors
    return jsonify(response), status_code


class InvalidRequestException(Exception):
    pass

class RecordNotFoundException(Exception):
    pass


class EntitySaveException(Exception):
    pass


class EntityUpdateException(Exception):
    pass
