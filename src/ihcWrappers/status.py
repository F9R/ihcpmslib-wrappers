from typing import List
from .state import StateWrapper
from .commandDescription import CommandDescriptionWrapper


class StatusWrapper:
    def __init__(self, status) -> None:
        self.__s = status

    @property
    def CurrentTime(self) -> str:
        return self.__s.CurrentTime.ToString()

    @property
    def DeviceId(self) -> str:
        return self.__s.DeviceId

    @property
    def Locked(self) -> bool:
        return self.__s.Locked

    @property
    def PMSId(self) -> str:
        return self.__s.PMSId

    @property
    def State(self) -> str:
        return StateWrapper(self.__s.State).name

    @property
    def SubStates(self) -> List[CommandDescriptionWrapper]:
        ss = []
        tmp =  self.__s.SubStates
        for value in tmp:
            ss.append(CommandDescriptionWrapper(value))
        return ss

