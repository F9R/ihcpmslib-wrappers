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
        """Seraches for SCILAs in local subnet.

        nic -- Searches on specific network interface or all (None-value) (default None)
        timeout -- timeout in ms (default 2000)

        Returns -- List of FinderResult
        """
        if nic == None:
            fr = ScilaFinder.SearchDevices(timeout)
            res = []
            for val in fr:
                res.append(FinderResultWrapper(val))
            return res
        else:
            fr = ScilaFinder.SearchDevices(nic, timeout)
            res = []
            for val in fr:
                res.append(FinderResultWrapper(val))
            return res

    @staticmethod
    def SearchDevicesExtended(nic: NetworkInterface = None, timeout: int = 2000) -> List[FinderResultWrapper]:
        """Seraches for SCILAs in broadcast domain. Connection to device(s) might not be possible.

        nic -- Searches on specific network interface or all (None-value) (default None)
        timeout -- timeout in ms (default 2000)

        Returns -- List of FinderResult
        """
        if nic == None:
            fr = ScilaFinder.SearchDevicesExtended(None, timeout)
            res = []
            for val in fr:
                res.append(FinderResultWrapper(val))
            return res
        else:
            fr = ScilaFinder.SearchDevicesExtended(nic, timeout)
            res = []
            for val in fr:
                res.append(FinderResultWrapper(val))
            return res
