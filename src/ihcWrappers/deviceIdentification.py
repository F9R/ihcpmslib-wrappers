from typing import List


class DeviceIdentificationWrapper:
    def __init__(self, deviceIdentification) -> None:
        self.__di = deviceIdentification

    @property
    def DeviceFirmwareVersion(self) -> str:
        return self.__di.DeviceFirmwareVersion

    @property
    def DeviceManufacturer(self) -> str:
        return self.__di.DeviceManufacturer

    @property
    def DeviceName(self) -> str:
        return self.__di.DeviceName

    @property
    def DeviceSerialNumber(self) -> str:
        return self.__di.DeviceSerialNumber

    @property
    def SiLADeviceClass(self) -> int:
        return self.__di.SiLADeviceClass

    @property
    def SiLADeviceClassVersion(self) -> str:
        return self.__di.SiLADeviceClassVersion

    @property
    def SiLAInterfaceVersion(self) -> str:
        return self.__di.SiLAInterfaceVersion

    @property
    def SiLASubDeviceClass(self) -> List[int]:
        return self.__di.SiLASubDeviceClass
    
    @property
    def Wsdl(self) -> str:
        return self.__di.Wsdl
        