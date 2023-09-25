

template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}

data = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
    },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27,
        },
        'birthplace': {
            'test':23,
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare',
        }
    }
}


class WrongTypeException(Exception):
    pass


class WrongKeyException(Exception):
    pass


def check_keys(template_key, data_key):
    if not template_key == data_key:
        raise WrongKeyException(f"Template Key: {template_key} Given Key: {data_key}") 

def validate(data, template, last_key=""):
    template_keys = template.keys()
    data_items = data.items()
    if len(template_keys) != data_items:
        raise WrongKeyException(len(template_keys), len(data_items))

    for ((t_key), (key, value)) in zip(template_keys, data_items):

        # print(((t_key), (key, value)))
        full_key = f"{last_key}.{key}" if last_key else key
        temp_key = f"{last_key}.{t_key}" if last_key else t_key
        check_keys(temp_key, full_key)

        if isinstance(value, dict):
            print(value)
            validate(value, template[key], full_key)
        else:
            print(key, value)
            result = isinstance(value, template[key])
            if not result:
                raise WrongTypeException(False, last_key)
    return True, ""

print(validate(data, template))
