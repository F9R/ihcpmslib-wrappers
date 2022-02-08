class SensorValuesWrapper:
    def __init__(self, sensorValues) -> None:
        self.__sv = sensorValues

    def __str__(self):
        return self.__sv.ToString()

    @property
    def Ambient(self) -> int:
        return self.__sv.Ambient

    @property
    def Mount(self) -> int:
        return self.__sv.Mount
    
    @property
    def MountMonitor(self) -> int:
        return self.__sv.MountMonitor

    @property
    def Heatsink(self) -> int:
        return self.__sv.Heatsink

    @property
    def HeatsinkTec(self) -> int:
        return self.__sv.HeatsinkTec

    @property
    def Lid(self) -> int:
        return self.__sv.Lid

    @property
    def LidMonitor(self) -> int:
        return self.__sv.LidMonitor

    @property
    def Pcb(self) -> int:
        return self.__sv.Pcb

    @property
    def Timestamp(self) -> str:
        return self.__sv.STimestamp