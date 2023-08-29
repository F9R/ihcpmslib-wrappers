import configparser
config = configparser.ConfigParser()
config.read('config.ini')
if config['IHC']['ODTC'] != "True":
    pass

import logging
from typing import List
from .ftpItem import FtpItemWrapper

from System import Array
from IhcPmsLib.Odtc.Logs import OdtcDownloader

class OdtcDownloaderWrapper:
    
    def __init__(self) -> None:
        self.__od = OdtcDownloader()

    def GetItems(self, host: str, path: str) -> List[FtpItemWrapper]:
        i = []
        try:
            tmp = self.__od.GetItems(host, path)
            for value in tmp:
                i.append(FtpItemWrapper(value))
            return i
        except Exception as ex:
            logging.error(ex.Message)
            raise

    def DownloadFtpItems(self, ftpItems: List[FtpItemWrapper], directory: str) -> str:
        if ftpItems == None:
            pass
        aFtpItems = Array.CreateInstance(ftpItems[0]._fi.GetType(), len(ftpItems))
        for idx, item in enumerate(ftpItems):
            aFtpItems[idx] = item._fi
        try:
            error = self.__od.DownloadFtpItems(aFtpItems, directory)
            if error is not None: # WebException
                logging.error(error)
            return error
        except Exception as ex:
            logging.error(ex.Message)
            raise
