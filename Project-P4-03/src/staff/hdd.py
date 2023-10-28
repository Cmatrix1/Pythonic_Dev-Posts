from staff.utils import Storages



class HDD(Storages):
    __slots__ = ('size', 'rpm')

    def __init__(self, name: str, manufacturer: str, total: int, allocated: int, size: int, rpm: float):
        super().__init__(name, manufacturer, total, allocated)
        self._size = size
        self._rpm = rpm

