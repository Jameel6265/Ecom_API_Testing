from jsonschema import validate,ValidationError
from utils.logger import log_error


def validate_schema(response_json,schema):
    try:
        validate(instance=response_json,schema=schema)
        return True
    except ValidationError as er:
        log_error(f"Schema validation failed: {er.message}")
        return False