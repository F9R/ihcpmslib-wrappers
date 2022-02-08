import configparser
config = configparser.ConfigParser()
config.read('config.ini')
if config['IHC']['ODTC'] != "True":
    pass

from enum import Enum
import clr
clr.AddReference("IHC_PMS_Lib.Odtc")

from System import DateTime
from IHC_PMS_Lib.Inheco import NetworkType
from IHC_PMS_Lib.Odtc import OdtcConfigXml

class OdtcConfigXmlWrapper:
    def __init__(self) -> None:
        self.__cx = OdtcConfigXml()

    @property
    def LogLevel(self) -> str:
        return self.__cx.LogLevel.ToString()

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