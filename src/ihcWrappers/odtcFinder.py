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

    @staticmethod
    def SearchDevices(nic: NetworkInterface = None, timeout: int = 2000) -> List[FinderResultWrapper]:
        """Seraches for ODTCs in local subnet.

        nic -- Searches on specific network interface or all (None-value) (default None)
        timeout -- timeout in ms (default 2000)

        Returns -- List of FinderResult
        """
        if nic == None:
            fr = OdtcFinder.SearchDevices(timeout)
            res = []
            for val in fr:
                res.append(FinderResultWrapper(val))
            return res
        else:
            fr = OdtcFinder.SearchDevices(nic, timeout)
            res = []
            for val in fr:
                res.append(FinderResultWrapper(val))
            return res

    @staticmethod
    def SearchDevicesExtended(nic: NetworkInterface = None, timeout: int = 2000) -> List[FinderResultWrapper]:
        """Seraches for ODTCs in broadcast domain. Connection to device(s) might not be possible.

        nic -- Searches on specific network interface or all (None-value) (default None)
        timeout -- timeout in ms (default 2000)

        Returns -- List of FinderResult
        """
        if nic == None:
            fr = OdtcFinder.SearchDevicesExtended(None, timeout)
            res = []
            for val in fr:
                res.append(FinderResultWrapper(val))
            return res
        else:
            fr = OdtcFinder.SearchDevicesExtended(nic, timeout)
            res = []
            for val in fr:
                res.append(FinderResultWrapper(val))
            return res
