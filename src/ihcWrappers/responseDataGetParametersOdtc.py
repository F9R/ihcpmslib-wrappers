from typing import List
from .responseData import ResponseDataWrapper


class ResponseDataGetParametersOdtcWrapper(ResponseDataWrapper):
    def __init__(self, responseData) -> None:
        super().__init__(responseData)

    @property
    def CSVSeparatorCharacter(self) -> str:
        return self._rd.CSVSeparatorCharacterRaw

    @property
    def DynamicPreMethodDuration(self) -> bool:
        return self._rd.DynamicPreMethodDuration

    @property
    def ExecuteMethodDataEvent(self) -> bool:
        return self._rd.ExecuteMethodDataEvent

    @property
    def MatchLidTemperatures(self) -> bool:
        return self._rd.MatchLidTemperatures

    @property
    def MethodsXML(self) -> str:
        return self._rd.MethodsXMLRaw

    def GetPreMethodNames(self) -> List[str]:
        return self._rd.GetPreMethodNames()

    def GetMethodNames(self) -> List[str]:
        return self._rd.GetMethodNames()