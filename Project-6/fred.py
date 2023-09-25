import csv

def parse_data(f_name):
    f = open(f_name)
    try:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        next(f)  # skip header row
        yield from csv.reader(f, dialect=dialect)
    finally:
        f.close()


def coroutine(fn):
    def inner(*args, **kwargs):
        coro = fn(*args, **kwargs)
        next(coro)
        return coro
    return inner

@coroutine
def filter_data(filter_pred, target):
    while True:
        row = yield
        if filter_pred(row):
            target.send(row)

@coroutine
def save_csv(f_name):
    with open(f_name, 'w', newline='') as f:
        writer = csv.writer(f)
        while True:
            row = yield
            writer.writerow(row)

@coroutine
def pipeline_coro(out_file, name_filters):
    save = save_csv(out_file)
    
    target = save
    for name_filter in name_filters:
        target = filter_data(lambda d, v=name_filter: v in d[0], target)
        # warning: we have to use the trick above because
        # lambdas are actually closures and the free variable name_filter
        # is a shared free variable - we have seen this problem before!
    while True:
        received = yield
        target.send(received)

from contextlib import contextmanager

@contextmanager
def pipeline(out_file, name_filters):
    p = pipeline_coro(out_file, name_filters)
    try:
        yield p
    finally:
        p.close()


with pipeline('out.csv', ('Chevrolet', 'Landau', 'Carlo')) as p:
    for row in parse_data('cars.csv'):
        p.send(row)
