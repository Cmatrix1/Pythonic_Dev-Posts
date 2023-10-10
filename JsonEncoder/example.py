import json
from datetime import datetime

class CustomDecoder(json.JSONDecoder):
    def decode(self, json_string):
        # Decode the JSON string using the default decoder
        obj = super().decode(json_string)
        
        # Modify the decoded object as needed
        if isinstance(obj, dict) and 'date' in obj:
            obj['date'] = datetime.strptime(obj['date'], '%Y-%m-%d')
        
        return obj


json_string = '{"name": "John Doe", "age": 30, "date": "2022-10-03"}'
custom_decoder = CustomDecoder()
data = json.loads(json_string, cls=custom_decoder)
print(data)
# Output: {'name': 'John Doe', 'age': 30, 'date': datetime.datetime(2022, 10, 3, 0, 0)}
