class ResponseDataWrapper:
    def __init__(self, responseData) -> None:
        self._rd = responseData

    @property
    def Raw(self) -> str:
        return self._rd.Raw