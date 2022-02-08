from .responseData import ResponseDataWrapper
from .sensorValues import SensorValuesWrapper


class ResponseDataReadActualTemperatureWrapper(ResponseDataWrapper):
    def __init__(self, responseData) -> None:
        super().__init__(responseData)

    @property
    def SensorValues(self) -> SensorValuesWrapper:
        return SensorValuesWrapper(self._rd.SensorValues)
