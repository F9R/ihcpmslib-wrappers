from .responseData import ResponseDataWrapper


class ResponseDataGetTemperatureWrapper(ResponseDataWrapper):
    def __init__(self, responseData) -> None:
        super().__init__(responseData)

    @property
    def CurrentTemperature(self) -> float:
        return self._rd.CurrentTemperature

    @property
    def TargetTemperature(self) -> float:
        return self._rd.TargetTemperature

    @property
    def TemperatureControl(self) -> bool:
        return self._rd.TemperatureControl
