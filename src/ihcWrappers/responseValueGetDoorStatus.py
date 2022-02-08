from .responseDataGetDoorStatus import ResponseDataGetDoorStatusWrapper
from .responseValue import ResponseValueWrapper


class ResponseValueWrapperGetDoorStatus(ResponseValueWrapper):
    def __init__(self, responseValue) -> None:
        super().__init__(responseValue)

    @property
    def ResponseData(self) -> ResponseDataGetDoorStatusWrapper:
        return ResponseDataGetDoorStatusWrapper(self._rv.ResponseData)