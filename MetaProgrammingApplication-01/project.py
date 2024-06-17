

class BaseCustomType(type):
    def __new__(cls, cls_name, bases, cls_dict):
        instanec = super().__new__(cls, cls_name, bases, cls_dict)
        instanec.__slots__ = [f"_{field}" for field in instanec._fields]
        instanec.__eq__ = cls._base_eq
        instanec.__hash__ = cls._base_hash
        instanec.__repr__ = cls._base_repr
        for field in instanec._fields:
            slot = f'_{field}'
            setattr(
                instanec,
                field,
                property(fget=lambda self, attrib=slot: getattr(instanec, slot))
            )
        return instanec

    @staticmethod
    def _base_eq(instance, other):
        assert type(instance) == type(other)
        for slot in instance.__slots__:
            if getattr(instance, slot) != getattr(other, slot):
                return False
        return True

    @staticmethod
    def _base_hash(instance):
        data = tuple(getattr(instance, slot) for slot in instance.__slots__)
        return hash(data)

    @staticmethod
    def _base_repr(instance):
        data = list(str(getattr(instance, slot))
                    for slot in instance.__slots__)
        return f'{instance.__class__.__name__}({", ".join(data)})'


class Point2D(metaclass=BaseCustomType):
    _fields = ['x', 'y']

    def __init__(self, x, y):
        self._x = x
        self._y = y


class Point3D(metaclass=BaseCustomType):
    _fields = ['x', 'y', 'z']

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z


point = Point2D(1, 2)
point_2 = Point2D(2, 2)

print(point, point_2)
print(point == point_2)
print(hash(point))
print(point.x)
