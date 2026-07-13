from fastapi import Request
from fastapi.responses import JSONResponse

from .not_found_errors import NotFoundError

def value_error_handler(request: Request, error: ValueError):
    return JSONResponse(
        status_code=400,
        content={ 'message': repr(error) }
    )

def not_found_error_handler(request: Request, error: NotFoundError):
    return JSONResponse(
        status_code=404,
        content='Not found'
    )