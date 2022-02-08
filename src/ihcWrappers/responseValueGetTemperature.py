from .responseDataGetTemperature import ResponseDataGetTemperatureWrapper
from .responseValue import ResponseValueWrapper


class ResponseValueWrapperGetTemperature(ResponseValueWrapper):
    def __init__(self, responseValue) -> None:
        super().__init__(responseValue)

    @property
    def ResponseData(self) -> ResponseDataGetTemperatureWrapper:
        return ResponseDataGetTemperatureWrapper(self._rv.ResponseData)