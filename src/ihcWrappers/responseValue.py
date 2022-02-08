import logging
from .silaReturnValue import SiLAReturnValueWrapper


class ResponseValueWrapper:

    def __init__(self, responseValue) -> None:
        self._rv = responseValue
        #logging.debug("ResponseValueWrapper ctor")

    @property
    def Aborted(self) -> bool:
        return self._rv.Aborted()

    @property
    def ExpectedDuration(self) -> str:
        return self._rv.ExpectedDuration.ToString()

    @property
    def RequestId(self) -> int:
        return self._rv.RequestId

    @property
    def CommandId(self) -> str:
        return self._rv.CommandId

    @property
    def Message(self) -> str:
        return self._rv.Message

    @property
    def Success(self) -> bool:
        return self._rv.Success

    @property
    def ResponseData(self):
        return self._rv.ResponseData

    @property
    def ResponseDuration(self) -> str:
        return self._rv.ResponseDuration.ToString()

    @property
    def ReturnValue(self) -> SiLAReturnValueWrapper:
        return SiLAReturnValueWrapper(self._rv.ReturnValue)

    @property
    def SynchronousDuration(self) -> str:
        return self._rv.SynchronousDuration.ToString()