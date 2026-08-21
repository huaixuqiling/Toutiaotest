from fastapi import HTTPException
from utils.exeption import http_exception_handler,IntegrityError,integrity_error_handle,SQLAlchemyError,sql_error_handle,general_exception_handler


def register_exception_handlers(app):
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(IntegrityError, integrity_error_handle)
    app.add_exception_handler(SQLAlchemyError,sql_error_handle)
    app.add_exception_handler(Exception,general_exception_handler)
