from .responseData import ResponseDataWrapper


class ResponseDataGetValveStatusWrapper(ResponseDataWrapper):
    def __init__(self, responseData) -> None:
        super().__init__(responseData)

    @property
    def Gas_Boost(self) -> str:
        return self._rd.Gas_Boost_Raw

    @property
    def Gas_Normal(self) -> str:
        return self._rd.Gas_Normal_Raw

    @property
    def H2O(self) -> str:
        return self._rd.H2O_Raw
