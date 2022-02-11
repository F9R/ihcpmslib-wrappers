import configparser
config = configparser.ConfigParser()
config.read('config.ini')
if config['IHC']['ODTC'] == "True":
    from .odtcFinder import OdtcFinderWrapper
    from .odtc import DataEventOdtcSensorValue, OdtcWrapper
    from .odtcConfigXml import OdtcConfigXmlWrapper
    from .odtcParamsXml import OdtcParamsXmlWrapper
if config['IHC']['SCILA'] == "True":
    from .scila import ScilaWrapper
    from .scilaFinder import ScilaFinderWrapper
    from .scilaConfigXml import ScilaConfigXmlWrapper
    from .scilaParamsXml import ScilaParamsXmlWrapper
from .pms import PmsWrapper
from .device import DeviceWrapper
from .status import StatusWrapper
from .deviceIdentification import DeviceIdentificationWrapper
from .networkInterfaceTypes import NetworkInterfaceTypesWrapper
from .statusEventArgs import StatusEventArgsWrapper
