import csv

def corutine(fn):
    def wrapper(*args, **kwargs):
        g = fn(*args, **kwargs)
        next(g)
        return g
    return wrapper


def read_data(fname):
    with open(fname) as file:
        dialect = csv.Sniffer().sniff(file.read(2000))
        file.seek(0)
        next(file)
        reader = csv.reader(file, dialect=dialect)
        yield from reader

@corutine
def write_data(fname):
    with open(fname, "w") as file:
        while True:
            data: list = yield
            line = " ".join(data) + "\n"
            file.write(line)

@corutine
def check_filters(filter_words):
    result = None
    while True:
        data = yield result
        for word in filter_words:
            result = all(list(map(word, lambda w: word in data)))

def main():
    file_name = "cars.csv"
    file_reader = read_data(file_name)

    filters = "Chevrolet", "Carlo", "Landau"
    filters_method = check_filters(filters)

    file_writer = write_data("filter_1.csv")

    for data in file_reader:
        result = filters_method.send(data[0])
        if result:
            file_writer.send(data)