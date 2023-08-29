import configparser
config = configparser.ConfigParser()
config.read('config.ini')
import os
from pythonnet import load
load("coreclr", runtime_config=os.path.join(config['IHC']['LibraryPath'], "pmssh.runtimeconfig.json"))
import clr
clr.AddReference("System")
clr.AddReference(os.path.join(config['IHC']['LibraryPath'], "IhcPmsLib.dll"))
if config['IHC']['ODTC'] == "True":
    clr.AddReference(os.path.join(config['IHC']['LibraryPath'], "IhcPmsLib.Odtc.dll"))
    clr.AddReference(os.path.join(config['IHC']['LibraryPath'], "System.ServiceModel.Http.dll"))
    from .odtcFinder import OdtcFinderWrapper
    from .odtc import DataEventOdtcSensorValue, OdtcWrapper
    from .odtcConfigXml import OdtcConfigXmlWrapper
    from .odtcParamsXml import OdtcParamsXmlWrapper
    from .odtcDownloader import OdtcDownloaderWrapper
if config['IHC']['SCILA'] == "True":
    clr.AddReference(os.path.join(config['IHC']['LibraryPath'], "IhcPmsLib.Scila.dll"))
    from .scila import ScilaWrapper
    from .scilaFinder import ScilaFinderWrapper
    from .scilaConfigXml import ScilaConfigXmlWrapper
    from .scilaParamsXml import ScilaParamsXmlWrapper
    from .scilaDownloader import ScilaDownloaderWrapper
from .pms import PmsWrapper
from .device import DeviceWrapper
from .status import StatusWrapper
from .deviceIdentification import DeviceIdentificationWrapper
#from .networkInterface import NetworkInterfaceWrapper,
from .networkInterfaceTypes import NetworkInterfaceTypesWrapper
from .statusEventArgs import StatusEventArgsWrapper
from .ftpItem import FtpItemWrapper
