import configparser
config = configparser.ConfigParser()
config.read('config.ini')
if config['IHC']['ODTC'] == "True":
    from .odtcFinder import OdtcFinderWrapper
    from .odtc import DataEventOdtcSensorValue, OdtcWrapper
    from .odtcConfigXml import OdtcConfigXmlWrapper
    from .odtcParamsXml import OdtcParamsXmlWrapper
if config['IHC']['SCILA'] == "True":
    from .scilaFinder import ScilaFinderWrapper
    from .scilaConfigXml import ScilaConfigXmlWrapper
    from .scilaParamsXml import ScilaParamsXmlWrapper
from .pms import PmsWrapper
from .networkInterfaceTypes import NetworkInterfaceTypesWrapper
from .statusEventArgs import StatusEventArgsWrapper
