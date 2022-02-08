from .responseDataReadActualTemperature import ResponseDataReadActualTemperatureWrapper
from .responseValue import ResponseValueWrapper


class ResponseValueWrapperReadActualTemperature(ResponseValueWrapper):
    def __init__(self, responseValue) -> None:
        super().__init__(responseValue)

    @property
    def ResponseData(self) -> ResponseDataReadActualTemperatureWrapper:
        return ResponseDataReadActualTemperatureWrapper(self._rv.ResponseData)