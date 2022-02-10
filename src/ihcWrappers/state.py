from enum import Enum


class StateWrapper(Enum):
    Startup = 0
    Resetting = 1
    Standby = 2
    Initializing = 3
    Idle = 4
    Busy = 5
    Paused = 6
    ErrorHandling = 7
    InError = 8