from .responseValue import ResponseValueWrapper
from .responseDataGetParametersOdtc import ResponseDataGetParametersOdtcWrapper


class ResponseValueWrapperGetParametersOdtc(ResponseValueWrapper):
    def __init__(self, responseValue) -> None:
        super().__init__(responseValue)

    @property
    def ResponseData(self) -> ResponseDataGetParametersOdtcWrapper:
        ##return super().ResponseData
        return ResponseDataGetParametersOdtcWrapper(self._rv.ResponseData)