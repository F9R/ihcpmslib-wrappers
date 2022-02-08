import configparser
config = configparser.ConfigParser()
config.read('config.ini')
if config['IHC']['ODTC'] != "True":
    pass

import clr
clr.AddReference("IHC_PMS_Lib.Odtc")

from IHC_PMS_Lib.Odtc import OdtcParamsXml
from IHC_PMS_Lib.Odtc.MethodXML import MethodSet


class OdtcParamsXmlWrapper:
    def __init__(self) -> None:
        self.__px = OdtcParamsXml()

    @property
    def CSVSeparatorCharacter(self) -> chr:
        return self.__px.CSVSeparatorCharacter

    @CSVSeparatorCharacter.setter
    def CSVSeparatorCharacter(self, value: chr):
        self.__px.CSVSeparatorCharacter = value

    @property
    def DynamicPreMethodDuration(self) -> bool:
        return self.__px.DynamicPreMethodDuration

    @DynamicPreMethodDuration.setter
    def DynamicPreMethodDuration(self, value: bool):
        self.__px.DynamicPreMethodDuration = value

    @property
    def ExecuteMethodDataEvent(self) -> bool:
        return self.__px.ExecuteMethodDataEvent

    @ExecuteMethodDataEvent.setter
    def ExecuteMethodDataEvent(self, value: bool):
        self.__px.ExecuteMethodDataEvent = value

    @property
    def MatchLidTemperatures(self) -> bool:
        return self.__px.MatchLidTemperatures

    @MatchLidTemperatures.setter
    def MatchLidTemperatures(self, value: bool):
        self.__px.MatchLidTemperatures = value

    @property
    def MethodsXML(self) -> str:
        ms = self.__px.MethodsXML
        if ms != None:
            return ms.GetXml()
        else:
            return None

    @MethodsXML.setter
    def MethodsXML(self, methodSet: str):
        self.__px.MethodsXML = MethodSet.Deserialize(methodSet)

    def GetParamsXml(self) -> str:
        return self.__px.GetParamsXml()

    def ImportMethodSetXml(self, path: str) -> None:
        self.__px.MethodsXML = MethodSet.GetMethodSet(path)