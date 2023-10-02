import json
from datetime import date, datetime
from decimal import Decimal

from models import Stock, Trade


activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22),
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22),
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22),
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],

    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12),
              'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5),
              'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}


class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(indent=4)

    def default(self, arg):
        if isinstance(arg, (Trade, Stock)):
            data = vars(arg).copy()
            data.update({'type': arg.__class__.__name__.lower()})
            return data
        elif isinstance(arg, Decimal):
            return f"Decimal-{arg}"
        elif isinstance(arg, (datetime, date)):
            return arg.isoformat()
        else:
            return super().default(arg)


class CustomDecoder(json.JSONDecoder):
    types = [datetime.fromisoformat]
    extra_types = {"trade": Trade, "stock": Stock}

    def decode(self, arg):
        obj = self.load_obj(arg)

        if isinstance(obj, dict):
            obj_type = obj.pop('type', None)

            for key, val in obj.items():
                if isinstance(val, (dict, list)):
                    obj[key] = self.decode(val)
                elif isinstance(val, str):
                    obj[key] = self.convert_str_to_type(val)

            if obj_type:
                obj = self.extra_types[obj_type](**obj) 

        elif isinstance(obj, list):
            for index, data in enumerate(obj):
                obj[index] = self.decode(data)

        return obj

    def convert_str_to_type(self, arg):
        if isinstance(arg, str) and "Decimal-" in arg:
            return Decimal(arg.strip("Decimal-"))
        try:    
            return datetime.fromisoformat(arg)
        except:
            return arg
        

    def load_obj(self, arg):
        try:
            return json.loads(arg)
        except:
            return arg


encoder = CustomEncoder()
endcode_activity = encoder.encode(activity)

decoder = CustomDecoder()
print(decoder.decode(endcode_activity))



