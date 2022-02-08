from .responseDataGetLiquidLevel import ResponseDataGetLiquidLevelWrapper
from .responseValue import ResponseValueWrapper


class ResponseValueWrapperGetLiquidLevel(ResponseValueWrapper):
    def __init__(self, responseValue) -> None:
        super().__init__(responseValue)

    @property
    def ResponseData(self) -> ResponseDataGetLiquidLevelWrapper:
        return ResponseDataGetLiquidLevelWrapper(self._rv.ResponseData)