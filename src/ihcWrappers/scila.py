import configparser
config = configparser.ConfigParser()
config.read('config.ini')
if config['IHC']['SCILA'] != "True":
    pass

import logging
import clr
clr.AddReference("IHC_PMS_Lib.Scila")

from .device import DeviceWrapper
from .responseValue import ResponseValueWrapper
from .statusEventArgs import StatusEventArgsWrapper
from .responseValueGetConfiguration import ResponseValueWrapperGetConfiguration
from .responseValueGetParametersScila import ResponseValueWrapperGetParametersScila
from .responseValueGetAutoBoostCo2 import ResponseValueWrapperGetAutoBoostCo2
from .responseValueGetCo2FlowStatus import ResponseValueWrapperGetCo2FlowStatus
from .responseValueGetDoorStatus import ResponseValueWrapperGetDoorStatus
from .responseValueGetLiquidLevel import ResponseValueWrapperGetLiquidLevel
from .responseValueGetTemperature import ResponseValueWrapperGetTemperature
from .responseValueGetValveStatus import ResponseValueWrapperGetValveStatus

#from System import Uri
from System import TimeSpan
from System import Nullable
from System import Int32
from System import Double
from System import Boolean

from IHC_PMS_Lib import SiLARequestException
from IHC_PMS_Lib import SiLAResponseException
from IHC_PMS_Lib import CommandException
from IHC_PMS_Lib.Scila import Scila


class ScilaWrapper(DeviceWrapper):
    def __init__(self, scila):
        super(ScilaWrapper, self).__init__(scila)
        self._d.StatusEvent += self.__StatusEvent
        logging.debug("ScilaWrapper ctor")

    def __StatusEvent(self, sender, sea):
        logging.debug("StatusEvent>>")
        if self._sDel is not None:
            #logging.debug("Calling StatusEvent Callback")
            self._sDel(StatusEventArgsWrapper(sea))

    def BoostCo2(self, boostDuration: int) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.BoostCo2(boostDuration))
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

    def Delay(self, duration: int) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.Delay(TimeSpan.FromSeconds(duration)))
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def GetAutoBoostCo2(self) -> ResponseValueWrapperGetAutoBoostCo2:
        try:
            return ResponseValueWrapperGetAutoBoostCo2(self._d.GetAutoBoostCo2())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def GetCo2FlowStatus(self) -> ResponseValueWrapperGetCo2FlowStatus:
        try:
            return ResponseValueWrapperGetCo2FlowStatus(self._d.GetCo2FlowStatus())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

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

    def GetDoorStatus(self) -> ResponseValueWrapperGetDoorStatus:
        try:
            return ResponseValueWrapperGetDoorStatus(self._d.GetDoorStatus())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def GetLiquidLevel(self) -> ResponseValueWrapperGetLiquidLevel:
        try:
            return ResponseValueWrapperGetLiquidLevel(self._d.GetLiquidLevel())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def GetParameters(self) -> ResponseValueWrapperGetParametersScila:
        try:
            return ResponseValueWrapperGetParametersScila(self._d.GetParameters())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def GetTemperature(self) -> ResponseValueWrapperGetTemperature:
        try:
            return ResponseValueWrapperGetTemperature(self._d.GetTemperature())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def GetValveStatus(self) -> ResponseValueWrapperGetValveStatus:
        try:
            return ResponseValueWrapperGetValveStatus(self._d.GetValveStatus())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def Maintenance(self) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.Maintenance())
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

    def PrepareForInput(self, position: int):
        try:
            return ResponseValueWrapper(self._d.PrepareForInput(Nullable[Int32](position)))
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def PrepareForOutput(self, position: int):
        try:
            return ResponseValueWrapper(self._d.PrepareForOutput(Nullable[Int32](position)))
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def RetrieveByPositionId(self, position: int):
        try:
            return ResponseValueWrapper(self._d.RetrieveByPositionId(position)) # CommandException!
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def SetAutoBoostCo2(self, autoBoostCo2: bool) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.SetAutoBoostCo2(autoBoostCo2))
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def SetCo2NormalFlow(self, co2NormalFlow: bool) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.SetCo2NormalFlow(co2NormalFlow))
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def SetTemperature(self, targetTemperature: float, temperatureControl: bool) -> ResponseValueWrapper:
        try:
            if targetTemperature == None and temperatureControl != None:
                return ResponseValueWrapper(self._d.SetTemperature(None, Nullable[Boolean](temperatureControl)))
            elif targetTemperature != None and temperatureControl == None:
                return ResponseValueWrapper(self._d.SetTemperature(Nullable[Double](targetTemperature), None))
            elif targetTemperature == None and temperatureControl == None:
                return ResponseValueWrapper(self._d.SetTemperature(None, None))
            else:
                return ResponseValueWrapper(self._d.SetTemperature(Nullable[Double](targetTemperature), Nullable[Boolean](temperatureControl)))
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def StoreAtPosition(self, position: int):
        try:
            return ResponseValueWrapper(self._d.StoreAtPosition(position))
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
        return Scila.GetVersion()


# from .eventDescription import EventDescription

# class StatusEventArgs:
#     def __init__(self, statusEventArgs) -> None:
#         self.__sea = statusEventArgs

#     @property
#     def ReturnValue(self) -> SiLAReturnValue:
#         return SiLAReturnValue(self.__sea.ReturnValue)

#     @property
#     def EventDescription(self) -> EventDescription:
#         return EventDescription(self.__sea.EventDescritption)

#     # ODTC + SCILA
#     @property
#     def ErrorClassification(self) -> str:
#         return self.__sea.ErrorClassification

#     # ODTC + SCILA
#     @property
#     def InternalErrorCode(self) -> int:
#         return self.__sea.InternalErrorCode