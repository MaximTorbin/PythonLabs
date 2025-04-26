import json
from jsonschema import validate, ValidationError, FormatChecker

with open('ex_1.json') as f:
    data = json.load(f)

with open('scheme.json') as f:
    schema = json.load(f)

try:
    validate(instance=data, schema=schema, format_checker=FormatChecker())
    print("JSON passed validation!")
except ValidationError as e:
    print("Validation error:")
    print(e.message)