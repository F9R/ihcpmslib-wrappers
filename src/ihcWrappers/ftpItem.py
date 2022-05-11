class FtpItemWrapper:
    def __init__(self, ftpItem) -> None:
        self._fi = ftpItem

    @property
    def Value(self) -> str:
        return self._fi.Value

    @property
    def URL(self) -> str:
        return self._fi.URL

    @property
    def IsDirectory(self) -> bool:
        return self._fi.IsDirectory    
        
    @property
    def Size(self) -> int:
        return self._fi.Size

    @property
    def DateTime(self):
        return self._fi.DateTime

    @property
    def Download(self) -> bool:
        return self._fi.Download
    
    @Download.setter
    def Download(self, download: bool):
        self._fi.Download = download

    @property
    def IsTrace(self) -> bool:
        return self._fi.IsTrace
