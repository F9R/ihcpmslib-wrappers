import configparser
config = configparser.ConfigParser()
config.read('config.ini')
if config['IHC']['ODTC'] != "True":
    pass

import logging

from .responseValue import ResponseValueWrapper
from .responseValueGetLastData import ResponseValueWrapperGetLastData

from .device import DeviceWrapper
from .responseValueReadActualTemperature import ResponseValueWrapperReadActualTemperature
from .responseValueGetConfiguration import ResponseValueWrapperGetConfiguration
from .responseValueGetParametersOdtc import ResponseValueWrapperGetParametersOdtc
from .statusEventArgs import StatusEventArgsWrapper

import clr
clr.AddReference("IHC_PMS_Lib.Odtc")

from System import Nullable
from System import Int32
from IHC_PMS_Lib import SiLARequestException
from IHC_PMS_Lib import SiLAResponseException
from IHC_PMS_Lib import CommandException
from IHC_PMS_Lib.Odtc import Odtc

class OdtcWrapper(DeviceWrapper):
    def __init__(self, odtc):
        super(OdtcWrapper, self).__init__(odtc)
        self.__odtc = odtc
        self.__dDel = None
        self._d.StatusEvent += self.__StatusEvent
        self.__odtc.DataEvent += self.__DataEvent
        logging.debug("OdtcWrapper ctor")


    def RegisterDataEventCallback(self, delegate):
        self.__dDel = delegate

    def __StatusEvent(self, sender, sea):
        logging.debug("StatusEvent>>")
        #logging.debug(sea.Device.DeviceName + " " + sea.ErrorClassification + " " + str(sea.InternalErrorCode))
        if self._sDel is not None:
            self._sDel(StatusEventArgsWrapper(sea))

    # def HasStatusEvent(self) -> bool:
    #     return len(self.__lSe) != 0

    # def GetStatusEvent(self):
    #     try:
    #         return self.__lSe.pop()
    #     except IndexError:
    #         pass

    def __DataEvent(self, sender, dea):
        logging.debug("DataEvent>>")
        values = dea.GetSensorValues()
        values2 = []
        for val in values:
            values2.append(DataEventOdtcSensorValue(val))
        if self.__dDel is not None:
            self.__dDel(values2)

    def GetConfiguration(self, configLevel: int = None, password: str = None) -> ResponseValueWrapperGetConfiguration:
        try:
            if configLevel == None:
                return ResponseValueWrapperGetConfiguration(self._d.GetConfiguration(None, password))
            else:
                return ResponseValueWrapperGetConfiguration(self._d.GetConfiguration(Nullable[Int32](configLevel), password))
            
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def GetParameters(self) -> ResponseValueWrapperGetParametersOdtc:
        try:
            return ResponseValueWrapperGetParametersOdtc(self._d.GetParameters())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def OpenDoor(self) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.OpenDoor())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def CloseDoor(self) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.CloseDoor())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def ReadActualTemperature(self) -> ResponseValueWrapperReadActualTemperature:
        # res = self._d.ReadActualTemperature()
        # return SensorValues(res.ResponseData.SensorValues)
        try:
            return ResponseValueWrapperReadActualTemperature(self._d.ReadActualTemperature())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def ExecuteMethod(self, methodName, priority=1) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.ExecuteMethod(methodName, priority))
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def StopMethod(self) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.StopMethod())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def GetLastData(self) -> ResponseValueWrapperGetLastData:
        try:
            return ResponseValueWrapperGetLastData(self._d.GetLastData())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    
    @staticmethod
    def GetAssemblyVersion() -> str:
        return Odtc.GetVersion()


class DataEventOdtcSensorValue:
    def __init__(self, sensorValue) -> None:
        self.__sv = sensorValue

    def __str__(self):
        return str(self.__sv.Time) + " " + self.__sv.Name + " " + str(self.__sv.Value)

    def _get_name(self) -> str:
        return self.__sv.Name
    name = property(_get_name)

    def _get_value(self) -> float:
        return self.__sv.Value
    value = property(_get_value)

    def _get_duration(self) -> float:
        return self.__sv.Time
    duration = property(_get_duration)
