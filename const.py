from enum import Enum

class CalcType(Enum):
    SingleThread = 0
    MultiThread = 1
    MultiPrecess = 2
    PyCoroutine = 3