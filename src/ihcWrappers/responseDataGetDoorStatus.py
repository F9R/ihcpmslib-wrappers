from .responseData import ResponseDataWrapper


class ResponseDataGetDoorStatusWrapper(ResponseDataWrapper):
    def __init__(self, responseData) -> None:
        super().__init__(responseData)

    @property
    def Drawer1(self) -> str:
        return self._rd.Drawer1

    @property
    def Drawer2(self) -> str:
        return self._rd.Drawer2
    
    @property
    def Drawer3(self) -> str:
        return self._rd.Drawer3
    
    @property
    def Drawer4(self) -> str:
        return self._rd.Drawer4
