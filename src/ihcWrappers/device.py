import logging
from typing import List, Tuple

from .silaReturnValue import SiLAReturnValueWrapper
from .responseValue import ResponseValueWrapper
from .status import StatusWrapper
from .deviceIdentification import DeviceIdentificationWrapper

import clr
from System import Nullable
from System import Int32
from IHC_PMS_Lib import SiLARequestException
from IHC_PMS_Lib import SiLAResponseException
from IHC_PMS_Lib import CommandException


class DeviceWrapper:
    def __init__(self, device) -> None:
        self._d = device
        self._sDel = None
        logging.debug("DeviceWrapper ctor")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self._d is not None:
            self._d.Dispose()

    def Dispose(self):
        if self._d is not None:
            self._d.Dispose()

    def RegisterStatusEventCallback(self, delegate):
        self._sDel = delegate

    @property
    def ContractName(self) -> str:
        return self._d.ContractName

    @property
    def DeviceEndpointUri(self) -> str:
        return self._d.DeviceEndpointUri.ToString()

    @property
    def DeviceId(self) -> str:
        return self._d.DeviceId

    @property
    def DeviceName(self) -> str:
        return self._d.DeviceName

    @property
    def DeviceState(self) -> str: #TODO enum
        return self._d.DeviceState.ToString()

    @property
    def EventReceiverUri(self) -> str:
        return self._d.EventReceiverUri

    @property
    def LockId(self) -> str:
        return self._d.LockId

    @LockId.setter
    def LockId(self, value):
        self._d.LockId = value

    @property
    def PMSId(self) -> str:
        return self._d.PMSId

    @property
    def ResponseTimeout(self) -> int:
        return self._d.ResponseTimeout

    @ResponseTimeout.setter
    def ResponseTimeout(self, value):
        self._d.ResponseTimeout = value

    @property
    def SerialNumber(self) -> str:
        return self._d.SerialNumber

    @property
    def Version(self) -> str:
        return self._d.Version

    def Close(self) -> None:
        self._d.Close()

    def Execute(self, commandId: str, parameter: List[str]) -> ResponseValueWrapper: 
        try:
            return ResponseValueWrapper(self._d.Execute(commandId, parameter))
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    '''ISynchronousCommands'''

    def GetStatus(self) -> Tuple[SiLAReturnValueWrapper, StatusWrapper]:
        [r, s] = self._d.GetStatus(None)
        return (SiLAReturnValueWrapper(r), StatusWrapper(s))

    def GetDeviceIdentification(self) -> Tuple[SiLAReturnValueWrapper, DeviceIdentificationWrapper]:
        [r, di] = self._d.GetDeviceIdentification(None)
        return (SiLAReturnValueWrapper(r), DeviceIdentificationWrapper(di))

    '''IMandatoryCommands'''

    def Abort(self) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.Abort())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def DoContinue(self) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.DoContinue())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def Initialize(self) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.Initialize())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def LockDevice(self) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.LockDevice())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def Pause(self) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.Pause())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def Reset(self) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.Reset())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def UnlockDevice(self) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.UnlockDevice())
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise
    
    '''Common Commands'''

    def SetConfiguration(self, configXml:str, configLevel:int = None, password:str = None) -> ResponseValueWrapper:
        try:
            if configLevel == None:
                return ResponseValueWrapper(self._d.SetConfiguration(None, password, configXml))
            else:
                return ResponseValueWrapper(self._d.SetConfiguration(Nullable[Int32](configLevel), password, configXml))
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise

    def SetParameters(self, paramsXml:str) -> ResponseValueWrapper:
        try:
            return ResponseValueWrapper(self._d.SetParameters(paramsXml))
        except SiLARequestException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except SiLAResponseException as ex:
            logging.warn(ex.Message)
            return ResponseValueWrapper(ex.ResponseValue)
        except CommandException as ex:
            logging.error(ex.Message)
            raise