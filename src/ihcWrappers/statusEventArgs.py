import logging
from .device import DeviceWrapper
from .eventDescription import EventDescriptionWrapper
from .silaReturnValue import SiLAReturnValueWrapper

class StatusEventArgsWrapper: # FOR: do not call it StatusEventArgs
    def __init__(self, statusEventArgs) -> None:
        self.__sea = statusEventArgs
        logging.debug("StatusEventArgsWrapper ctor")

    @property
    def Device(self) -> DeviceWrapper:
        return DeviceWrapper(self.__sea.Device)

    @property
    def ReturnValue(self) -> SiLAReturnValueWrapper:
        return SiLAReturnValueWrapper(self.__sea.ReturnValue)

    @property
    def EventDescription(self) -> EventDescriptionWrapper:
        return EventDescriptionWrapper(self.__sea.EventDescription)
