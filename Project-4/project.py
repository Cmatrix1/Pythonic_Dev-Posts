from csv import reader
from collections import namedtuple, defaultdict
from itertools import groupby
from datetime import datetime


def data_type_converter(data):
    types = [lambda x : datetime.strptime(x, '%Y-%m-%dT%H:%M:%Sz'), int, float, str]
    for type_class in types:
        try:
            return type_class(data)
        except ValueError:
            continue
    return data


def read_csv_file(file_name: str):
    with open(file_name) as f:
        yield from reader(f)


def get_fields_without_repeat(lines): # I don't use set because of order 
    fields = []
    for line in lines:
        for field in line:
            if not field in fields:
                fields.append(field)
    return fields


def combine_csv_data(files):
    file_iterator = list(map(read_csv_file, files))
    iterators = zip(*file_iterator)
    Person = namedtuple("Person", get_fields_without_repeat(next(iterators)))
    for lines in iterators:
        line = get_fields_without_repeat(lines)
        clean_data = list(map(data_type_converter, line))
        yield Person(*clean_data)


def group_by_gender_make(datas):
    counter = defaultdict(int)
    for data in datas:
        counter[f"{data.gender} {data.vehicle_make}"] += 1
    cnts = list(counter.items())
    cnts.sort(key=lambda x: x[1])
    return cnts

# I don't Understand Why This Method Not Work
def group_by_gender_make(datas):
    datas = sorted(datas, key=lambda x: (x.gender, x.vehicle_make))
    groupby_data = groupby(datas, lambda x: (x.gender, x.vehicle_make))
    yield from groupby_data

datas = combine_csv_data(
    ["personal_info.csv", "employment.csv", "update_status.csv", "vehicles.csv"])

grouped = group_by_gender_make(datas)
for i in grouped:
    print(i[0], len(list(i[1])))