import logging
from typing import List

class EventDescriptionWrapper:
    def __init__(self, eventDescription) -> None:
        self.__ed = eventDescription
        #logging.debug("EventDescriptionWrapper ctor")

    def __str__(self):
        return self.__ed.ToString()

    @property
    def CurrentValue(self) -> str:
        return self.__ed.CurrentValue

    @property
    def DeviceId(self) -> str:
        return self.__ed.DeviceId

    @property
    def DeviceState(self) -> str: # TODO enum
        return self.__ed.DeviceState.ToString()

    @property
    def DeviceURI(self) -> str:
        return self.__ed.DeviceURI

    @property
    def Extensions(self) -> List[str]:
        # exts = List[str]
        # for val in self.__ed.Extensions:
        #     exts.append(val)
        #return exts
        return self.__ed.Extensions

    @property
    def FaultCorrectionsHints(self) -> str:
        return self.__ed.FaultCorrectionHints

    @property
    def Raw(self) -> str:
        return self.__ed.Raw

    @property
    def StatusMessage(self) -> str:
        return self.__ed.StatusMessage

    @property
    def Classification(self) -> str:
        return self.__ed.Classification

    @property
    def InternalCode(self) -> int:
        return self.__ed.InternalCode

    @property
    def InternalCodeName(self) -> str:
        return self.__ed.InternalCodeName

    @property
    def InternalCodeDescription(self) -> str:
        return self.__ed.InternalCodeDescription