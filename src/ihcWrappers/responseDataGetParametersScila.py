from .responseData import ResponseDataWrapper


class ResponseDataGetParametersScilaWrapper(ResponseDataWrapper):
    def __init__(self, responseData) -> None:
        super().__init__(responseData)

    @property
    def Position(self) -> int:
        return self._rd.Position

    @property
    def WorkstationMode(self) -> bool:
        return self._rd.WorkstationMode
