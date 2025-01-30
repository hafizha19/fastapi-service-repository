from repositories.holiday_repository import create, delete, detail, list, update, check_is_holiday
from fastapi import HTTPException

def create_holiday_service(requests):
    data = create(requests)

    return data


def get_holiday_service():
    data = list()

    return data


def get_holiday_by_id_service(id: str):
    data = detail(id)
    if data is None:
        raise HTTPException(
            status_code=404, detail=f"Holiday with id {id} does not exist."
        )
    
    return data


def delete_holiday_service(id: str):
    data = delete(id)

    return data


def update_holiday_service(requests, id: str):
    data = update(requests, id)

    return data


def check_is_holiday_service(date):
    data = check_is_holiday(date)
    return data