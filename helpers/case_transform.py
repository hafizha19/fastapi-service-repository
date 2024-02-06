from stringcase import camelcase, snakecase


def camel_to_snake_case(inp: dict):
    out = {}
    for key, value in inp.items():
        snake_key = snakecase(key)
        out[snake_key] = value
    return out


def snake_to_camel_case(inp: dict):
    out = {}
    for key, value in inp.items():
        if key == "_id":
            out[key] = str(value)
        else:
            camel_key = camelcase(key)
            out[camel_key] = value
    return out
