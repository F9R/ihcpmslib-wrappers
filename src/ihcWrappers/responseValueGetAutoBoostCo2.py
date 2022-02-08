from .responseDataGetAutoBoostCo2 import ResponseDataGetAutoBoostCo2Wrapper
from .responseValue import ResponseValueWrapper


class ResponseValueWrapperGetAutoBoostCo2(ResponseValueWrapper):
    def __init__(self, responseValue) -> None:
        super().__init__(responseValue)

    @property
    def ResponseData(self) -> ResponseDataGetAutoBoostCo2Wrapper:
        return ResponseDataGetAutoBoostCo2Wrapper(self._rv.ResponseData)