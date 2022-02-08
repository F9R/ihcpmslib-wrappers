from .responseData import ResponseDataWrapper


class ResponseDataGetConfigurationWrapper(ResponseDataWrapper):
    def __init__(self, responseData) -> None:
        super().__init__(responseData)

    @property
    def LogLevel(self) -> str:
        return self._rd.LogLevelRaw

    @property
    def NetworkConfig(self) -> str:
        return self._rd.NetworkConfigRaw

    @property
    def SoapCompression(self) -> str:
        return self._rd.SoapCompressionRaw

    @property
    def SysDateTime(self) -> str:
        return self._rd.SysDateTimeRaw

    @property
    def UseDeviceClassDateTime(self) -> str:
        return self._rd.UseDeviceClassDateTimeRaw