from helpers.case_transform import snake_to_camel_case


def format_response_success(
    response_dto=None, model_obj=None, data=None, message="Success"
):
    if data is None:
        data = format_response_data(response_dto, model_obj)

    response_body = {
        "meta": {"code": 200, "status": "success", "message": message},
        "data": data,
    }
    return response_body


def format_response_data(response_dto, model_obj):
    if isinstance(model_obj, dict):
        return response_dto(**snake_to_camel_case(model_obj)).dict(by_alias=False)

    return response_dto(**snake_to_camel_case(model_obj.to_mongo())).dict(
        by_alias=False
    )


def format_response_error(message: str = "Server Error", code: int = 500):
    response_body = {
        "meta": {"code": code, "status": "error", "message": message},
        "data": None,
    }
    return response_body
