from repositories.holiday_repository import create, delete, detail, list, update


def create_holiday_service(requests):
    data = create(requests)
    return data


def get_holiday_service():
    data = list()
    return data


def get_holiday_by_id_service(id: str):
    data = detail(id)
    return data


def delete_holiday_service(id: str):
    data = delete(id)
    return data


def update_holiday_service(requests, id: str):
    data = update(requests, id)
    return data
