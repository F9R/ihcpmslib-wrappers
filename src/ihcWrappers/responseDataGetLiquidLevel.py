from .responseData import ResponseDataWrapper


class ResponseDataGetLiquidLevelWrapper(ResponseDataWrapper):
    def __init__(self, responseData) -> None:
        super().__init__(responseData)

    @property
    def LiquidLevel(self) -> str:
        return self._rd.LiquidLevelRaw
