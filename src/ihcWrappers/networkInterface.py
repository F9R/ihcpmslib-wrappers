import clr
clr.AddReference("System.Net")

class NetworkInterfaceWrapper:
    def __init__(self, networkInterface) -> None:
        self.__ni = networkInterface
    
    @property
    def Id(self) -> str:
        return self.__ni.Id

    @property
    def Description(self) -> str:
        return self.__ni.Description

    @property
    def Name(self) -> str:
        return self.__ni.Name

    