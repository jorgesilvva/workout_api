from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

def handle_integrity_error(exc: IntegrityError, detail: str) -> HTTPException:
    return HTTPException(status_code=status.HTTP_303_SEE_OTHER, detail=detail)
