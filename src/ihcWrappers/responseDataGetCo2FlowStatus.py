from .responseData import ResponseDataWrapper


class ResponseDataGetGetCo2FlowStatusWrapper(ResponseDataWrapper):
    def __init__(self, responseData) -> None:
        super().__init__(responseData)

    @property
    def CO2FlowStatus(self) -> str:
        return self._rd.CO2FlowStatus
