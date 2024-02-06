import json

from fastapi.responses import JSONResponse

from config import logger
from helpers.format_response import format_response_error


async def exception_handler_middleware(exception, request):
    logger.info(exception.detail)
    logger.info(f"headers: {json.dumps(dict(request.headers))}")
    logger.info(f"query_params: {request.query_params}")

    return JSONResponse(
        content=format_response_error(exception.detail, exception.status_code),
        status_code=exception.status_code,
    )
    # try:
    #     return await call_next(request)
    # except HTTPException as e:
    #     logger.info("astagfirulloh")
    #     return format_response_error(request)
