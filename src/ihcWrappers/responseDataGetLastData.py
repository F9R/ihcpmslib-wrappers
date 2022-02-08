from .responseData import ResponseDataWrapper


class ResponseDataGetLastDataWrapper(ResponseDataWrapper):
    def __init__(self, responseData) -> None:
        super().__init__(responseData)

    @property
    def Data(self) -> str:
        return self._rd.Data

    @property
    def Name(self) -> str:
        return self._rd.Name
