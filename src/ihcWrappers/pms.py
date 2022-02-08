import logging
from typing import List
from .device import DeviceWrapper
from .networkInterfaceTypes import NetworkInterfaceTypesWrapper
from .networkInterface import NetworkInterfaceWrapper

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

import clr
clr.AddReference("System")
clr.AddReference("IHC_PMS_Lib")

from System import Uri
from System import TimeSpan
from System import Nullable
from System import UInt16

from IHC_PMS_Lib import PMS
from IHC_PMS_Lib import EventReceiverException
from IHC_PMS_Lib import ConnectException
from IHC_PMS_Lib import DeviceException
from IHC_PMS_Lib.API import NetworkInterfaceTypes
from IHC_PMS_Lib.Factory import DeviceFactory

if config['IHC']['ODTC'] == "True":
    from IHC_PMS_Lib.Odtc import Odtc 
    from IHC_PMS_Lib.Odtc.Factory import OdtcFactory
    from .odtc import OdtcWrapper

if config['IHC']['SCILA'] == "True":
    from IHC_PMS_Lib.Scila import Scila
    from IHC_PMS_Lib.Scila.Factory import ScilaFactory
    from .scila import ScilaWrapper

class PmsWrapper():
    def __init__(self):
        self.__pms = PMS()
        self.__pms.CacheAssembly = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # if self.__pms is not None:
        #     self.__pms.Dispose()
        pass

    # def Dispose(self):
    #     if self.__pms is not None:
    #         self.__pms.Dispose()


    def IpAddressIndex(self, index: int):
        """IP address index of interface
        
        Multihomed network interface e.g. VPN address (Linux)
        """
        self.__pms.IpAddressIndex = index
 
    def StartEventReceiver(self, nicId: str = None, port: int = None, path: str = None) -> str:
        try:
            if port == None:
                uri = self.__pms.StartEventReceiver(nicId, None, path)
            else:
                uri = self.__pms.StartEventReceiver(nicId, Nullable[UInt16](port), path)
            #logging.debug(uri)
            return uri.ToString()
        except EventReceiverException as ex:
            logging.error(ex.Message)
            raise

    def StopEventReceiver(self):
        try:
            self.__pms.StopEventReceiver()
        except EventReceiverException as ex:
            logging.error(ex.Message)
            # uri = pms.StartEventReceiver(res[0].Id, None, "ihc")
            # print(uri)
            raise

    def Create(self, wsdlUri: str):# -> DeviceWrapper:
        try:
            device = DeviceFactory.Create(self.__pms, Uri(wsdlUri), TimeSpan.FromSeconds(10), None, None)
            if config['IHC']['ODTC'] == "True":
                if type(device) is Odtc:
                    return OdtcWrapper(device)
            if config['IHC']['SCILA'] == "True":
                if type(device) is Scila:
                    return ScilaWrapper(device)
        except ConnectException as ex:
            logging.error(ex.Message)
            raise
        except DeviceException as ex:
            logging.error(ex.Message)
            raise
        
    if config['IHC']['ODTC'] == "True":
        def CreateOdtc(self, wsdlUri: str) -> OdtcWrapper:
            try:
                odtc = OdtcFactory.Create(self.__pms, Uri(wsdlUri), TimeSpan.FromSeconds(10), None, None)
                return OdtcWrapper(odtc)
            except ConnectException as ex:
                logging.error(ex.Message)
                raise
            except DeviceException as ex:
                logging.error(ex.Message)
                raise

    if config['IHC']['SCILA'] == "True":
        def CreateScila(self, wsdlUri: str) -> ScilaWrapper:
            try:
                scila = ScilaFactory.Create(self.__pms, Uri(wsdlUri), TimeSpan.FromSeconds(10), None, None)
                return ScilaWrapper(scila)
            except ConnectException as ex:
                logging.error(ex.Message)
                raise
            except DeviceException as ex:
                logging.error(ex.Message)
                raise

    @staticmethod
    def GetNIC(nicId: str) -> None:
        return PMS.GetNIC(nicId)

    @staticmethod
    def SupportedNICs(types: NetworkInterfaceTypesWrapper = 0) -> List[NetworkInterfaceWrapper]:
        if types == 0:
            return PMS.SupportedNICs()
        else:
            return PMS.SupportedNICs(types)

    def GetSupportedNICs(self, types: NetworkInterfaceTypesWrapper = 0) -> List[NetworkInterfaceWrapper]:
        if types == 0:
            return self.__pms.GetSupportedNICs()
        else:
            return self.__pms.GetSupportedNICs(types)
