import configparser
config = configparser.ConfigParser()
config.read('config.ini')
if config['IHC']['ODTC'] != "True":
    pass

import clr
clr.AddReference("IHC_PMS_Lib.Odtc")
from System.Net.NetworkInformation import NetworkInterface
from IHC_PMS_Lib.Odtc.Finder import OdtcFinder
from typing import List
from .finderResult import FinderResultWrapper

class OdtcFinderWrapper:
    # def __init__(self) -> None:
    #     self.__f = OdtcFinder()

    @staticmethod
    def SearchDevices(nic: NetworkInterface = None, timeout: int = 2000) -> List[FinderResultWrapper]:
                # res = List[FinderResultWrapper]
        # res2 = OdtcFinder.SearchDevices(timeout)
        # for val in res2:
        #     res.append(val)
        return OdtcFinder.SearchDevices(timeout)
        # return res

    @staticmethod
    def SearchDevicesExtended(nic: NetworkInterface = None, timeout: int = 2000) -> List[FinderResultWrapper]:
        return OdtcFinder.SearchDevicesExtended(timeout)
