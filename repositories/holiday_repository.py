from datetime import datetime
from typing import List

from bson import ObjectId
from fastapi import HTTPException
from mongoengine import DoesNotExist

from models.holiday import Holiday


def create(data: dict) -> Holiday:
    try:
        holiday = Holiday(**data)
        holiday.save()
        return holiday
    except HTTPException as e:
        error_message = f"Type error occurred: {str(e)}"
        raise HTTPException(status_code=500, detail=error_message)


def list() -> List[Holiday]:
    holidays = Holiday.objects.all()
    return holidays


def detail(oid: ObjectId) -> Holiday:
    try:
        return Holiday.objects.get(_id=oid)
    except DoesNotExist:
        return None


def delete(id: str) -> Holiday:
    holiday = detail(ObjectId(id))
    holiday["deleted_at"] = datetime.now
    holiday.save()
    return holiday


def update(data: dict, id: str) -> Holiday:
    holiday = detail(ObjectId(id))

    for key, value in data:
        setattr(holiday, key, value)

    holiday.save()
    return holiday
