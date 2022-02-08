import configparser
config = configparser.ConfigParser()
config.read('config.ini')
if config['IHC']['SCILA'] != "True":
    pass

import clr
clr.AddReference("IHC_PMS_Lib.Scila")

from System import Nullable
from System import Int32
from System import Boolean
from IHC_PMS_Lib.Scila import ScilaParamsXml


class ScilaParamsXmlWrapper:
    def __init__(self) -> None:
        self.__px = ScilaParamsXml()

    @property
    def Position(self) -> int:
        return self.__px.Position

    @Position.setter
    def Position(self, value: int):
        if value == None:
            self.__px.Position = None
        else:
            self.__px.Position = Nullable[Int32](value)

    @property
    def WorkstationMode(self) -> bool:
        return self.__px.WorkstationMode

    @WorkstationMode.setter
    def WorkstationMode(self, value: bool):
        if value == None:
            self.__px.WorksationMode = None
        else:
            self.__px.WorkstationMode = Nullable[Boolean](value)

    def GetParamsXml(self) -> str:
        return self.__px.GetParamsXml()
