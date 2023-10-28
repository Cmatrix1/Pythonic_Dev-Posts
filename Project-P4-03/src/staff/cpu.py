from core import Resource




class CPU(Resource):
    __slots__ = ("_cores", "_socket", "_power_watts")
    
    def __init__(self, name: str, manufacturer: str, total: int, allocated: int, cores: int, socket: str, power_watts: int):
        super().__init__(name, manufacturer, total, allocated)
        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts
    
    @property
    def cores(self):
        return self._cores
    @property
    def socket(self):
        return self._socket
    @property
    def power_watts(self):
        return self._power_watts