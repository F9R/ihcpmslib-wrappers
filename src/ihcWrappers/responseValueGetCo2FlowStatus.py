from .responseDataGetCo2FlowStatus import ResponseDataGetGetCo2FlowStatusWrapper
from .responseValue import ResponseValueWrapper


class ResponseValueWrapperGetCo2FlowStatus(ResponseValueWrapper):
    def __init__(self, responseValue) -> None:
        super().__init__(responseValue)

    @property
    def ResponseData(self) -> ResponseDataGetGetCo2FlowStatusWrapper:
        return ResponseDataGetGetCo2FlowStatusWrapper(self._rv.ResponseData)