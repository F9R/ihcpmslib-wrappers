import logging


class SiLAReturnValueWrapper:
    def __init__(self, returnValue) -> None:
        self.__rv = returnValue
        #logging.debug("SiLAReturnValueWrapper ctor")

    @property
    def DeviceClass(self) -> int:
        return self.__rv.DeviceClass

    @property
    def Duration(self) -> str:
        return self.__rv.Duration

    @property
    def Message(self) -> str:
        return self.__rv.Message
    
    @property
    def ReturnCode(self) -> int:
        return self.__rv.ReturnCode