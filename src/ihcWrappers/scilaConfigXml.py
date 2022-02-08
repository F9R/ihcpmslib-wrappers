import configparser
config = configparser.ConfigParser()
config.read('config.ini')
if config['IHC']['SCILA'] != "True":
    pass

import clr
clr.AddReference("IHC_PMS_Lib.Scila")

# rom System import Nullable
from System import DateTime
from IHC_PMS_Lib.Inheco import NetworkType
from IHC_PMS_Lib.Scila import ScilaConfigXml

class ScilaConfigXmlWrapper:
    def __init__(self) -> None:
        self.__cx = ScilaConfigXml()

    @property
    def LogLevel(self) -> str:
        return self.__cx.LogLevel.ToString()

    # @LogLevel.setter
    # def LogLevel(self, value: LogLevel):
    #     self.__cx.LogLevel = Nullable[LogLevel](value)

    @property
    def NetworkConfig(self) -> str:
        return self.__cx.NetworkConfig.GetXml()

    @NetworkConfig.setter
    def NetworkConfig(self, value: str):
        self.__cx.NetworkConfig = NetworkType.Deserialize(value)

    @property
    def SoapCompression(self) -> bool:
        return self.__cx.SoapCompression

    @SoapCompression.setter
    def SoapCompression(self, value: bool):
        self.__cx.SoapCompression = value

    @property
    def SysDateTime(self) -> str:
        self.__cx.SysDateTime.ToString()

    @SysDateTime.setter
    def SysDateTime(self, value: str):
        self.__cx.SysDateTime = DateTime.Parse(value)

    @property
    def UseDeviceClassDateTime(self) -> bool:
        return self.__cx.UseDeviceClassDateTime

    @UseDeviceClassDateTime.setter
    def UseDeviceClassDateTime(self, value: bool):
        self.__cx.UseDeviceClassDateTime = value

    def GetParamsXml(self) -> str:
        return self.__cx.GetParamsXml()

    def ImportNetworkConfigXml(self, path: str) -> None:
        self.__cx.ImportNetworkConfigXml(path)

# class LogLevel(Enum):
#     ALL = 0
#     DEBUG = 1
#     INFO = 2
#     WARN = 3
#     ERROR = 4
#     FATAL = 5
#     OFF = 6