import configparser
config = configparser.ConfigParser()
config.read('config.ini')
if config['IHC']['SCILA'] != "True":
    pass

import clr
clr.AddReference("IHC_PMS_Lib.Scila")
from System.Net.NetworkInformation import NetworkInterface
from IHC_PMS_Lib.Scila.Finder import ScilaFinder
from typing import List
from .finderResult import FinderResultWrapper

class ScilaFinderWrapper:

    @staticmethod
    def SearchDevices(nic: NetworkInterface = None, timeout: int = 2000) -> List[FinderResultWrapper]:
        return ScilaFinder.SearchDevices(timeout)

    @staticmethod
    def SearchDevicesExtended(nic: NetworkInterface = None, timeout: int = 2000) -> List[FinderResultWrapper]:
        return ScilaFinder.SearchDevicesExtended(timeout)
