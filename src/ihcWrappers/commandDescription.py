class CommandDescriptionWrapper:
    def __init__(self, commandDescription) -> None:
        self.__cd = commandDescription

    @property
    def CommandName(self) -> str:
        return self.__cd.CommandName

    @property
    def CurrentState(self) -> str:
        return self.__cd.CurrentState

    @property
    def DataWaiting(self) -> int:
        return self.__cd.DataWaiting

    @property
    def QueuePosition(self) -> int:
        return self.__cd.QueuePosition # nullable

    @property
    def RequestId(self) -> int:
        return self.__cd.RequestId

    @property
    def StartedAt(self) -> str:
        sa = self.__cd.StartedAt # nullable
        if sa is None:
            return None
        else:
            return self.__cd.StartedAt.ToString() 