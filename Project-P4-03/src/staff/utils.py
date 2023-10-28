from core import Resource


class Storages(Resource):
    __slots__ = ('capacity_gb', )
    def __init__(self, name, manufacturer, total, allocated, capacity_gb):
        super().__init__(name, manufacturer, total, allocated)
        self._capacity_gb = capacity_gb