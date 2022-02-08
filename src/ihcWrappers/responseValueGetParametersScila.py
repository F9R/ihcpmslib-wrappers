from .responseValue import ResponseValueWrapper
from .responseDataGetParametersScila import ResponseDataGetParametersScilaWrapper


class ResponseValueWrapperGetParametersScila(ResponseValueWrapper):
    def __init__(self, responseValue) -> None:
        super().__init__(responseValue)

    @property
    def ResponseData(self) -> ResponseDataGetParametersScilaWrapper:
        return ResponseDataGetParametersScilaWrapper(self._rv.ResponseData)