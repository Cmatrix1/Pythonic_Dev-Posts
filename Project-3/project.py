from collections import namedtuple, defaultdict


def clean_line(line: str) -> list:
    return line.strip("\n").split(",")

def clean_fields_name(line: str) -> str:
    fields = clean_line(line)
    return [field.replace(" ", "_").lower() for field in fields]

def file_iterator(file):
    with open(file) as f:
        clean_fields = clean_fields_name(next(f))
        Car = namedtuple("Car", clean_fields)
        for line in f:
            data = clean_line(line)
            yield Car(*data)



iterator = file_iterator("nyc_parking_tickets_extract.csv")
car_brands = defaultdict(int)
for i in iterator:
    brand = i.vehicle_make
    car_brands[brand] += 1

print({k:v for k, v in sorted(car_brands.items(), key=lambda x: x[1], reverse=True)})