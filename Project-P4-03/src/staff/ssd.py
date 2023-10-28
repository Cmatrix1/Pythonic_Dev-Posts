from staff.utils import Storages


class SSD(Storages):
    __slots__ = ('interface', )

    def __init__(self, name: str, manufacturer: str, total: int, allocated: int, interface: str):
        super().__init__(name, manufacturer, total, allocated)
        self._interface = interface

    