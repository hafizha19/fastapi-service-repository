from fastapi import APIRouter, HTTPException

from data.requests.holiday_request import Holiday as holiday_request
from data.responses.holiday_response import Holiday as holiday_response
from helpers.case_transform import camel_to_snake_case
from helpers.format_response import format_response_data, format_response_success
from services.holiday_service import (
    create_holiday_service,
    delete_holiday_service,
    get_holiday_by_id_service,
    get_holiday_service,
    update_holiday_service,
)

route = APIRouter()


@route.post("/create")
async def create_holiday(requests: holiday_request):
    try:
        data = camel_to_snake_case(requests.model_dump())
        created_data = create_holiday_service(data)

        return format_response_success(holiday_response, created_data)
    except HTTPException as exc:
        raise HTTPException(500, exc)


@route.get("/")
async def get_holidays():
    try:
        holidays = get_holiday_service()
        data = []
        for holiday in holidays:
            if holiday.deleted_at is None:
                data.append(format_response_data(holiday_response, holiday))

        return format_response_success(data=data)
    except HTTPException as exc:
        raise HTTPException(500, exc)


@route.get("/{id}")
async def get_holiday_by_id(id: str):
    holiday = get_holiday_by_id_service(id)
    
    return format_response_success(holiday_response, holiday)


@route.delete("")
async def delete_holiday(id: str):
    get_holiday_by_id_service(id)

    try:
        deleted_data = delete_holiday_service(id)

        return format_response_success(holiday_response, deleted_data)
    except HTTPException as exc:
        raise HTTPException(500, exc)


@route.put("/{id}")
async def update_holiday(holiday: holiday_request, id: str):
    get_holiday_by_id_service(id)

    try:
        updated_data = update_holiday_service(holiday, id)

        return format_response_success(holiday_response, updated_data)
    except HTTPException as exc:
        raise HTTPException(500, exc)


@route.get("/check")
async def get_holiday(date: str):
    try:
        data = check_is_holiday_service(date)

        return format_response_success(data=data)
    except HTTPException as exc:
        raise HTTPException(500, exc)