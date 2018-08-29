from enum import Enum


class OCRError(Enum):
    NO_CONF = 0
    LOW_CONF = 1
    EMPTY_VAL = 2
    BAD_PRED = 3
