import json
from datetime import datetime

def custom_object_hook(obj):
    if 'date' in obj:
        obj['date'] = datetime.strptime(obj['date'], '%Y-%m-%d')
    return obj

json_string = '{"name": "John Doe", "age": 30, "date": "2022-10-03"}'
data = json.loads(json_string, object_hook=custom_object_hook)
print(data)
# Output: {'name': 'John Doe', 'age': 30, 'date': datetime.datetime(2022, 10, 3, 0, 0)}


def custom_parse_float(value):
    return round(float(value), 2)

json_string = '{"price": 10.123456}'
data = json.loads(json_string, parse_float=custom_parse_float)
print(data)
# Output: {'price': 10.12}

class CustomDecoder(json.JSONDecoder):
    def decode(self, json_string):
        obj = super().decode(json_string)
        if isinstance(obj, dict) and 'date' in obj:
            obj['date'] = datetime.strptime(obj['date'], '%Y-%m-%d')
        return obj

json_string = '{"name": "John Doe", "age": 30, "date": "2022-10-03"}'
custom_decoder = CustomDecoder()
data = json.loads(json_string, cls=custom_decoder)
print(data)
# Output: {'name': 'John Doe', 'age': 30, 'date': datetime.datetime(2022, 10, 3, 0, 0)}
