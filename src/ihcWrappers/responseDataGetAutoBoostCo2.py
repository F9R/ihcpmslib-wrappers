from .responseData import ResponseDataWrapper


class ResponseDataGetAutoBoostCo2Wrapper(ResponseDataWrapper):
    def __init__(self, responseData) -> None:
        super().__init__(responseData)

    @property
    def AutoBoostCO2(self) -> bool:
        return self._rd.AutoBoostCO2

    @property
    def BoostState(self) -> str:
        return self._rd.BoostStateString
