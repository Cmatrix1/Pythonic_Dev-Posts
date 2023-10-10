from types import MappingProxyType

original_dict = {'a': 1, 'b': 2, 'c': 3}
read_only_dict = MappingProxyType(original_dict)

read_only_dict['a'] = 5
# TypeError: 'mappingproxy' object does not support item assignment
