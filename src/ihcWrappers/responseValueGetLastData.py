from .responseDataGetLastData import ResponseDataGetLastDataWrapper
from .responseValue import ResponseValueWrapper


class ResponseValueWrapperGetLastData(ResponseValueWrapper):
    def __init__(self, responseValue) -> None:
        super().__init__(responseValue)

    @property
    def ResponseData(self) -> ResponseDataGetLastDataWrapper:
        ##return super().ResponseData
        return ResponseDataGetLastDataWrapper(self._rv.ResponseData)