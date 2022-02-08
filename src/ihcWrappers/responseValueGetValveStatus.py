from .responseDataGetValveStatus import ResponseDataGetValveStatusWrapper
from .responseValue import ResponseValueWrapper


class ResponseValueWrapperGetValveStatus(ResponseValueWrapper):
    def __init__(self, responseValue) -> None:
        super().__init__(responseValue)

    @property
    def ResponseData(self) -> ResponseDataGetValveStatusWrapper:
        return ResponseDataGetValveStatusWrapper(self._rv.ResponseData)