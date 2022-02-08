from typing import List


class FinderResultWrapper:
    def __init__(self, finderResult) -> None:
        self.__fr = finderResult

    def __str__(self):
        return self.__fr.ToString()

    @property
    def Build(self) -> str:
        return self.__fr.Build

    @property
    def DhcpEnabled(self) -> bool:
        return self.__fr.DhcpEnabled

    @property
    def Dns(self) -> List[str]:
        dns = List[str]
        for val in self.__fr.Dns:
            dns.append(val.ToString())
        return dns

    @property
    def Frimware(self) -> str:
        return self.__fr.Firmware

    @property
    def IPv4Address(self) -> str:
        return self.__fr.IPv4Address.ToString()

    @property
    def IPv4Gateway(self) -> str:
        return self.__fr.IPv4Gateway.ToString()

    @property
    def IPv4Mask(self) -> str:
        return self.__fr.IPv4Mask.ToString()

    @property
    def Mac(self) -> str:
        return self.__fr.Mac.ToString()

    @property
    def Name(self) -> str:
        return self.__fr.Name

    @property
    def SoapServicePort(self) -> int:
        return self.__fr.SoapServicePort

    @property
    def Type(self) -> str:
        return self.__fr.Type

    @property
    def WsdlUri(self) -> str:
        return self.__fr.WsdlUri.ToString()
