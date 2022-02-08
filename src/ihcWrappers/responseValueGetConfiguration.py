from .responseValue import ResponseValueWrapper
from .responseDataGetConfiguration import ResponseDataGetConfigurationWrapper


class ResponseValueWrapperGetConfiguration(ResponseValueWrapper):
    def __init__(self, responseValue) -> None:
        super().__init__(responseValue)

    @property
    def ResponseData(self) -> ResponseDataGetConfigurationWrapper:
        return ResponseDataGetConfigurationWrapper(self._rv.ResponseData)